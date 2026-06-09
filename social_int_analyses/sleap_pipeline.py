"""
SLEAP Social Interaction Pipeline
==================================
Unified pipeline to:
  1. Rename raw camera videos (cam_XXXXX -> {animal}_pov_face / _pov_tunnel)
  2. Auto-rename DAY[N] folders to dd_mm_yyyy dates using social_int_sess_deets
  3. Run SLEAP inference (sleap-nn-track) on all tunnel videos
  4. Convert .slp predictions -> .h5 analysis files
  5. Reorganize .h5 files (move & rename to social_{condition}.h5 under day folder)
  6. Build session .pkl files via make_session_pkl logic

Usage (from your terminal with SLEAP env active):
    python sleap_pipeline.py [--steps 1,2,3,4,5,6] [--animal social-8564-2] [--dry-run]

All paths are configured in the CONFIG block below.
"""

import os
import glob
import shutil
import argparse
import subprocess
from datetime import datetime
from tqdm import tqdm


# ─────────────────────────────────────────────
#  CONFIG  ← edit these paths once
# ─────────────────────────────────────────────
CONFIG = {
    # Root that holds per-animal folders, each containing DAY[N] or dd_mm_yyyy sub-folders
    "SLEAP_RAW_ROOT": r"C:\Users\esay\data\social_interaction\SLEAP\SLEAP_raw",

    # Sub-folder under SLEAP_RAW_ROOT for the current cohort (leave "" to use root directly)
    "COHORT_SUBDIR": "test_dir",

    # Camera serial numbers → view names
    "CAM_FACE":   "cam_23175601",
    "CAM_TUNNEL": "cam_23199174",

    # SLEAP model paths for sleap-nn-track
    "MODEL_CENTROID": r"C:/Users/esay/data/social_interaction/SLEAP/models/250127_164147.single_instance.n=2844",
    # "MODEL_CENTERED":  r"C:\Users\esay\data\social_interaction\social_preference\EKS_longH\models\260515_160603.centered_instance.n=911",

    "SLP_OUTPUT_ROOT": r"C:\Users\esay\data\social_interaction\SLEAP\test",


    "SESSION_DEETS_MODULE": "social_int_analyses.social_int_sess_deets",

    "PKL_ROOT": r"C:\Users\esay\data\social_interaction\SessPkls",

    "BATCH_SIZE": 16,
}


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def cohort_root():
    root = CONFIG["SLEAP_RAW_ROOT"]
    sub = CONFIG["COHORT_SUBDIR"]
    return os.path.join(root, sub) if sub else root


def iter_animals(animal_filter=None):
    root = cohort_root()
    for name in sorted(os.listdir(root)):
        if not os.path.isdir(os.path.join(root, name)):
            continue
        if animal_filter and name != animal_filter:
            continue
        yield name


def iter_days(animal):
    animal_path = os.path.join(cohort_root(), animal)
    for name in sorted(os.listdir(animal_path)):
        if os.path.isdir(os.path.join(animal_path, name)):
            yield name


def iter_conditions(animal, day):
    day_path = os.path.join(cohort_root(), animal, day)
    for name in sorted(os.listdir(day_path)):
        if os.path.isdir(os.path.join(day_path, name)):
            yield name


# ─────────────────────────────────────────────
#  STEP 1 – Rename raw camera videos
# ─────────────────────────────────────────────

def step_rename_videos(animal_filter=None, dry_run=False):
    """
    Rename cam_XXXXX.{ext} → {animal}_pov_face.{ext} / {animal}_pov_tunnel.{ext}
    inside every condition folder.
    """
    print("\n=== STEP 1: Rename camera videos ===")
    cam_face   = CONFIG["CAM_FACE"]
    cam_tunnel = CONFIG["CAM_TUNNEL"]
    renamed = 0

    for animal in iter_animals(animal_filter):
        for day in iter_days(animal):
            for condition in iter_conditions(animal, day):
                cond_path = os.path.join(cohort_root(), animal, day, condition)
                for fname in os.listdir(cond_path):
                    parts = fname.split(".")
                    if len(parts) < 2:
                        continue
                    stem, ext = parts[0], ".".join(parts[1:])
                    src = os.path.join(cond_path, fname)

                    new_name = None
                    if cam_face in fname:
                        new_name = f"{animal}_pov_face.{ext}"
                    elif cam_tunnel in fname:
                        new_name = f"{animal}_pov_tunnel.{ext}"

                    if new_name and fname != new_name:
                        dst = os.path.join(cond_path, new_name)
                        if os.path.exists(dst):
                            print(f"  [SKIP] destination exists: {dst}")
                            continue
                        print(f"  {'[DRY]' if dry_run else 'Rename'}: {fname} → {new_name}")
                        if not dry_run:
                            os.rename(src, dst)
                        renamed += 1

    print(f"  Done. {renamed} file(s) renamed.")


# ─────────────────────────────────────────────
#  STEP 2 – THIS DOES  NOT WORK - MUST MANUALLY RENAME ALL DATE DIRS
# ─────────────────────────────────────────────

def step_rename_day_folders(animal_filter=None, dry_run=False):
    """
    Rename DAY[N] style folders to dd_mm_yyyy by looking up the date in
    social_int_sess_deets.social_VR_sessions[animal][day_index].
    Falls back gracefully if the module is unavailable or the animal/day is missing.
    """
    print("\n=== STEP 2: Rename DAY[N] folders to dates ===")

    module_name = CONFIG.get("SESSION_DEETS_MODULE")
    if not module_name:
        print("  SESSION_DEETS_MODULE not configured – skipping.")
        return

    try:
        import importlib
        deets = importlib.import_module(module_name)
        sessions = deets.social_VR_sessions
    except Exception as e:
        print(f"  Could not import {module_name}: {e}\n  Skipping step 2.")
        return

    renamed = 0
    for animal in iter_animals(animal_filter):
        if animal not in sessions:
            print(f"  [SKIP] {animal} not found in session deets.")
            continue
        animal_sessions = sessions[animal]  # list or dict keyed by day index

        for day_folder in list(iter_days(animal)):  # snapshot so rename doesn't break iteration
            # Try to parse a numeric index from folder names like DAY1, DAY2, day_1, etc.
            day_num = None
            for prefix in ("DAY", "Day", "day", "day_", "Day_", "DAY_"):
                if day_folder.upper().startswith("DAY"):
                    suffix = day_folder[3:].lstrip("_").lstrip(" ")
                    if suffix.isdigit():
                        day_num = int(suffix)
                        break

            if day_num is None:
                # Already in date format or unrecognized – skip
                continue

            # Look up date in session deets; day indices may be 0-based or 1-based
            date_str = None
            offset=-1
            idx = day_num + offset
                
            if isinstance(animal_sessions, dict) and idx in animal_sessions:
                date_str = animal_sessions[idx].get("date")
                break

            if not date_str:
                print(f"  [SKIP] No date found for {animal}/{day_folder} (day index {day_num}).")
                continue

            # Normalise to dd_mm_yyyy
            for fmt in ("%m_%d_%y", "%m_%d_%Y", "%d_%m_%Y", "%Y-%m-%d", "%m/%d/%y"):
                try:
                    dt = datetime.strptime(date_str, fmt)
                    date_str = dt.strftime("%d_%m_%Y")
                    break
                except ValueError:
                    pass  # already in target format or unknown – use as-is

            old_path = os.path.join(cohort_root(), animal, day_folder)
            new_path = os.path.join(cohort_root(), animal, date_str)

            if os.path.exists(new_path):
                print(f"  [SKIP] destination exists: {new_path}")
                continue

            print(f"  {'[DRY]' if dry_run else 'Rename'}: {animal}/{day_folder} → {date_str}")
            if not dry_run:
                os.rename(old_path, new_path)
            renamed += 1

    print(f"  Done. {renamed} folder(s) renamed.")


# ─────────────────────────────────────────────
#  STEP 3 – SLEAP inference (.mp4 → .slp)
# ─────────────────────────────────────────────

def step_run_sleap_inference(animal_filter=None, dry_run=False):
    """
    Run sleap-nn-track on every *_pov_tunnel.mp4 found under the cohort root.
    Skips videos whose .slp output already exists.
    """
    print("\n=== STEP 3: SLEAP inference ===")
    model_centroid = CONFIG["MODEL_CENTROID"]
    # model_centered  = CONFIG["MODEL_CENTERED"]
    slp_root = CONFIG["SLP_OUTPUT_ROOT"]
    batch_size = CONFIG["BATCH_SIZE"]

    videos = glob.glob(
        os.path.join(cohort_root(), "**", "*_pov_tunnel.mp4"), recursive=True
    )
    # Optionally filter by animal
    if animal_filter:
        videos = [v for v in videos if animal_filter in v]
    videos.sort()
    print(f"  Found {len(videos)} tunnel video(s).")

    for video_path in tqdm(videos, desc="  Inference"):
        video_id = os.path.splitext(os.path.basename(video_path))[0]
        out_dir   = slp_root if slp_root else os.path.dirname(video_path)
        os.makedirs(out_dir, exist_ok=True)
        output_slp = os.path.join(out_dir, f"predictions_{video_id}.slp")

        if os.path.exists(output_slp):
            print(f"  [SKIP] already exists: {os.path.basename(output_slp)}")
            continue

        cmd = [
            "sleap-nn-track",
            "--data_path", video_path,
            "--model_paths", model_centroid,
            # "--model_paths", model_centered,
            "-o", output_slp,
            "--batch_size", str(batch_size),
            "--max_instances", "1",
        ]
        print(f"  {'[DRY]' if dry_run else 'Running'}: {' '.join(cmd)}")
        if not dry_run:
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"  [ERROR] Inference failed for {video_id}: {e}")

    print("  Done.")


# ─────────────────────────────────────────────
#  STEP 4 – Convert .slp → .h5
# ─────────────────────────────────────────────

def step_convert_slp_to_h5(dry_run=False):
    """
    Run sleap-convert on every predictions_*.slp to produce .h5 analysis files.
    Skips if the .h5 already exists.
    """
    print("\n=== STEP 4: Convert .slp → .h5 ===")
    slp_root = CONFIG["SLP_OUTPUT_ROOT"] or cohort_root()

    slp_files = glob.glob(os.path.join(slp_root, "predictions_*.slp"), recursive=False)
    slp_files.sort()
    print(f"  Found {len(slp_files)} .slp file(s).")

    for slp_path in tqdm(slp_files, desc="  Convert"):
        base_name  = os.path.splitext(os.path.basename(slp_path))[0]
        output_h5  = os.path.join(slp_root, f"{base_name}.h5")

        if os.path.exists(output_h5):
            print(f"  [SKIP] already exists: {os.path.basename(output_h5)}")
            continue

        cmd = ["sleap-convert", slp_path, "--format", "analysis", "-o", output_h5]
        print(f"  {'[DRY]' if dry_run else 'Running'}: {' '.join(cmd)}")
        if not dry_run:
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"  [ERROR] Convert failed for {base_name}: {e}")

    print("  Done.")


# ─────────────────────────────────────────────
#  STEP 5 – Reorganize .h5 files into day folders
# ─────────────────────────────────────────────

def _parse_video_id(video_id):
    """
    Extract (animal, day, condition) from a video id like:
      social-8564-2_pov_tunnel.mp4.000_social-8564-2_pov_tunnel
    or from the containing path that was embedded in the predictions filename
    when step 3 used the video path basename directly.

    Returns None if the video_id can't be parsed – the caller will skip it.
    """
    # Fallback: try to find the source video inside the cohort tree and derive metadata
    # from its directory structure: cohort_root/animal/day/condition/video.mp4
    root = cohort_root()
    for animal in os.listdir(root):
        animal_path = os.path.join(root, animal)
        if not os.path.isdir(animal_path):
            continue
        if animal not in video_id:
            continue
        for day in os.listdir(animal_path):
            day_path = os.path.join(animal_path, day)
            if not os.path.isdir(day_path):
                continue
            for condition in os.listdir(day_path):
                cond_path = os.path.join(day_path, condition)
                if not os.path.isdir(cond_path):
                    continue
                expected_video_stem = f"{animal}_pov_tunnel"
                if expected_video_stem in video_id and condition in video_id:
                    return animal, day, condition
    return None


def step_reorganize_h5(animal_filter=None, dry_run=False):
    """
    Move predictions_{video_id}.h5 from SLP_OUTPUT_ROOT into:
      cohort_root/{animal}/{day}/social_{condition}.h5
    Mirrors the logic from move_and_rename_h5 in the rename notebook.
    """
    print("\n=== STEP 5: Reorganize .h5 files ===")
    slp_root = CONFIG["SLP_OUTPUT_ROOT"] or cohort_root()

    h5_files = glob.glob(os.path.join(slp_root, "predictions_*.h5"))
    h5_files.sort()
    print(f"  Found {len(h5_files)} .h5 file(s) to reorganize.")

    for h5_path in h5_files:
        base_name = os.path.splitext(os.path.basename(h5_path))[0]
        # Strip leading "predictions_"
        video_id = base_name[len("predictions_"):]

        parsed = _parse_video_id(video_id)
        if parsed is None:
            print(f"  [SKIP] Could not parse metadata for: {base_name}")
            continue

        animal, day, condition = parsed
        if animal_filter and animal != animal_filter:
            continue

        dest_dir  = os.path.join(cohort_root(), animal, day)
        dest_file = os.path.join(dest_dir, f"social_{condition}.h5")

        if os.path.exists(dest_file):
            print(f"  [SKIP] already exists: {dest_file}")
            continue

        print(f"  {'[DRY]' if dry_run else 'Move'}: {os.path.basename(h5_path)} → {dest_file}")
        if not dry_run:
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(h5_path, dest_file)

    print("  Done.")



ALL_STEPS = {
    1: step_rename_videos,
    2: step_rename_day_folders,
    3: step_run_sleap_inference,
    4: step_convert_slp_to_h5,
    5: step_reorganize_h5,

}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Unified SLEAP social interaction pipeline."
    )
    parser.add_argument(
        "--steps",
        default="1,2,3,4,5",
        help="Comma-separated list of steps to run (default: 1,2,3,4,5).",
    )
    parser.add_argument(
        "--animal",
        default=None,
        help="Process only this animal (e.g. social-8564-2). Default: all animals.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without making any changes.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    steps_to_run = [int(s.strip()) for s in args.steps.split(",")]
    dry_run      = args.dry_run
    animal       = args.animal

    if dry_run:
        print("*** DRY RUN – no files will be moved or renamed ***")

    for step_num in steps_to_run:
        if step_num not in ALL_STEPS:
            print(f"Unknown step {step_num}, skipping.")
            continue
        fn = ALL_STEPS[step_num]
        # Steps 4 (convert) has no animal filter
        if step_num == 4:
            fn(dry_run=dry_run)
        else:
            fn(animal_filter=animal, dry_run=dry_run)

    print("\n✓ Pipeline complete.")


if __name__ == "__main__":
    main()
