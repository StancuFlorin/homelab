#!/bin/bash

# Read configuration from sync_config.conf
source sync_config.conf

# Function to get folder size
get_folder_size() {
    du -s "$1" | awk '{print $1}'
}

# Function to get size of destination path
get_destination_size() {
    du -s "$DESTINATION_PATH" | awk '{print $1}'
}

# Get size of destination path before sync
destination_size_before=$(get_destination_size)

# Perform the sync using rsync
for path in "${SOURCE_PATHS[@]}"
do
    rsync -avz --progress --relative "$path" "$DESTINATION_PATH"
done

# Get size of destination path after sync
destination_size_after=$(get_destination_size)

# Calculate size of data synced during the current run
current_sync_size=$((destination_size_after - destination_size_before))

# Get current date
sync_datetime=$(date "+%Y-%m-%d %H:%M:%S")

# Create JSON data
json_data=$(cat <<EOF
{
  "time_of_sync": "$sync_datetime",
  "destination_path_size": $destination_size_after,
  "current_sync_size": $current_sync_size
}
EOF
)

# Write JSON data to file
echo "$json_data" > ../nginx/static/sync_info.json

echo "Sync completed successfully."