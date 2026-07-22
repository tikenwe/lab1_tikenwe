# Lab 1: Grade Evaluator & Archiver

## Overview
This project has two parts:
1. `grade-evaluator.py` — reads a CSV of assignment grades, validates the
   data, calculates a final GPA, determines a Pass/Fail status, and reports
   which formative assignment(s) are eligible for resubmission.
2. `organizer.sh` — archives `grades.csv` into an `archive/` folder with a
   timestamped filename, resets the workspace with a fresh empty
   `grades.csv`, and logs every run to `organizer.log`.

## Requirements
- Python 3
- Bash (Linux / Git Bash on Windows)

## 1. Running the Python Grade Evaluator

From the project directory, run:

    python3 grade-evaluator.py

You'll be prompted to enter the name of the CSV file to process:

    Enter the name of the CSV file to process (e.g., grades.csv): grades.csv

The script will then print:
- The Formative and Summative category percentages
- The overall Total Grade (out of 100) and final GPA (out of 5.0)
- The final status: PASSED or FAILED
- Any failed formative assignment(s) eligible for resubmission (the
  failed formative assignment(s) with the highest weight)

### Expected CSV format

    assignment,group,score,weight
    Quiz,Formative,85,20
    Group Exercise,Formative,40,20
    Functions and Debugging Lab,Formative,45,20
    Midterm Project - Simple Calculator,Summative,70,20
    Final Project - Text-Based Game,Summative,60,20

- `group` must be either Formative or Summative
- Formative weights must sum to exactly 60
- Summative weights must sum to exactly 40
- All scores must be between 0 and 100

If the file is missing, empty, has out-of-range scores, or the weights
don't add up correctly, the script prints a clear error message instead
of crashing.

## 2. Running the Shell Organizer

Make sure the script is executable, then run it from the same directory
as grades.csv:

    chmod +x organizer.sh
    ./organizer.sh

Each run will:
1. Create an archive/ directory if it doesn't already exist.
2. Move grades.csv into archive/ renamed with the current timestamp
   (e.g., grades_20251105-170000.csv).
3. Create a brand-new, empty grades.csv in the project directory.
4. Append a line to organizer.log recording the timestamp, the
   original filename, and the new archived filename.

You can run ./organizer.sh as many times as you like — organizer.log
will accumulate one entry per run.
