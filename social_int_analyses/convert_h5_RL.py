# RUN in the terminal: cd ....; uv run batch_sleap_tracking.py
import os
import glob
import subprocess
from tqdm import tqdm

# --- CONFIGURATION ---
ROOT_DIR = r"C:\Users\esay\data\social_interaction\social_preference\EKS_longH"
# MODEL_CENTROID = r"C:\Users\esay\data\social_interaction\social_preference\EKS_longH\models\260515_133457.centroid.n=911"
# MODEL_CENTERED = r"C:\Users\esay\data\social_interaction\social_preference\EKS_longH\models\260515_160603.centered_instance.n=911"
BATCH_SIZE = 16

# 1. Find all matching videos recursively
video_list = glob.glob(os.path.join(ROOT_DIR, "predictions_*.slp"), recursive=True)
video_list.sort()

print(f"Found {len(video_list)} prediction files. Starting batch tracking...")

for video_path in tqdm(video_list, desc="Overall Progress"):
    # Extract directory and ID
    base_name=os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(ROOT_DIR, f"{base_name}.h5")
    # 3. Construct your exact verified command
    # This uses the specific multi-model approach you confirmed works
    # cmd = [
    #     "sleap-nn-track",
    #     "--data_path", video_path,
    #     "--model_paths", MODEL_CENTROID,
    #     "--model_paths", MODEL_CENTERED,
    #     "-o", output_path,
    #     "--batch_size", str(BATCH_SIZE),
    #     "--max_instances", "1"
    # ]

    cmd = [
        "sleap-convert", 
        video_path,
        "--format", "analysis",
        "-o", output_path,
    ]

    # 4. Execute via subprocess
    try:
        # Standard run: progress will print directly to your terminal
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Tracking failed for {base_name}: {e}")
        continue

print("\n[+] All conversion jobs finished.")
