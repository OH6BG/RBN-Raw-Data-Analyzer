# RBN-Raw-Data-Analyzer
Rudimentary Reverse Beacon Network (RBN) Raw Data Analyzer (Python)

'''

A rudimentary RBN raw data analyzer. (c) Jari Perkiömäki OH6BG

This Python script processes the RBN raw data CSV files one by one,
and writes output to corresponding TXT files.

This script assumes that a Python 3 interpreter is installed on your computer.
Download the Python software at www.python.org; it's free.

HOW TO USE THIS SCRIPT

1. Download all the raw data files you wish to analyze from RBN
2. Unzip the files into a common folder
3. Put this script into the same folder
4. Under *nix/Linux, make this script executable: chmod u+x rbn.py
5. Run at the command prompt: ./rbn.py &
6. Under Windows, double-clicking the icon of this file should launch
   the Python interpreter by file association, and run the script.
5. If you want to have statistics from a specific skimmer or specific
   skimmers, enter the list of skimmers (separated by a comma) when prompted.
   You can also enter just one skimmer. If you just press ENTER at that point,
   statistics from ALL skimmers will be reported.
6. Processing of the files will be shown on the screen.

12 Jul 2016: Moved to GitHub.

06 Jul 2016: Added choice of skimmers. Processing info will be displayed
on the screen. Added automatic unzipping of the RBN raw data ZIP files.

05 Jul 2016: Initial release. Developed with Python 3.5.2, Windows
Tested with raw data files of more than 3.5 million lines.

'''
