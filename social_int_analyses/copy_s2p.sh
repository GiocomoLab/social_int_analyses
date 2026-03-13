#!/bin/bash

# Source base directory
src_base="Z:/giocomo/candong/social_interaction_data/calcium_imaging/social-0058-3"

# Destination base directory
dest_base="Z:/giocomo/esay/hipposs/social_interaction_data/2PData/social-0058-3"

# Iterate over each MOUSE folder
for date_dir in "$src_base"/*; do
    if [ -d "$date_dir" ]; then
        date=$(basename "$date_dir")

        # Full path to the source combined folder
        src_combined="$date_dir/combined/suite2p/combined"

        # Check if the directory exists
        if [ -d "$src_combined" ]; then
            # Construct destination path
            dest_combined="$dest_base/$date/suite2p/combined"

            echo "Copying:"
            echo "  $src_combined"
            echo "to:"
            echo "  $dest_combined"

            # Create destination folder
            mkdir -p "$dest_combined"

            # Copy contents
            cp -r "$src_combined/"* "$dest_combined/"
        fi
    fi
done
# fi
# done

echo "Done."
