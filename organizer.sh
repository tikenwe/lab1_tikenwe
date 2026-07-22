#!/usr/bin/env bash

# organizer.sh
# Archives grades.csv into an archive/ folder with a timestamped name,
# resets the workspace with a fresh empty grades.csv, and logs the action.

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

# 1. Ensure the archive directory exists
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created archive directory: $ARCHIVE_DIR"
fi

# 2. Guard: make sure there is a grades.csv to archive
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found in the current directory. Nothing to archive."
    exit 1
fi

# 3. Generate a timestamp (e.g., 20251105-170000)
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
NEW_NAME="grades_${TIMESTAMP}.csv"

# 4. Move the original file into the archive directory with its new name
mv "$SOURCE_FILE" "$ARCHIVE_DIR/$NEW_NAME"

# 5. Reset the workspace: create a fresh, empty grades.csv
touch "$SOURCE_FILE"

# 6. Log the operation (append so entries accumulate across runs)
echo "$TIMESTAMP | original: $SOURCE_FILE | archived as: $ARCHIVE_DIR/$NEW_NAME" >> "$LOG_FILE"

echo "Archived '$SOURCE_FILE' as '$ARCHIVE_DIR/$NEW_NAME'."
echo "A fresh, empty '$SOURCE_FILE' has been created."
echo "Logged this operation to '$LOG_FILE'."
