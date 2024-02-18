#!/bin/bash

source sync_config.conf

if [ ! -d "$DESTINATION_PATH" ]; then
    echo "Destination path does not exist. Please create it first."
    exit 1
fi

for path in "${SOURCE_PATHS[@]}"
do
    rsync -avz --progress "$path" "$DESTINATION_PATH"
done

echo
echo "Sync completed successfully."
echo

df -h
