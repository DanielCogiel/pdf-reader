# PDF Reader
This Python script allows you to create .mp3 audiobook from provided PDF file.

## Requirements
- Python 3.8 or higher

## Installation
All required dependencies are listed in _requirements.txt_ file. To install them, run:
`pip install -r requirements.txt`.

## How to run
To use this script simply run proper command:
- on Linux: `python3 read-pdf.py -f <pdf_filename> <optional_args>`
- on Windows: `py read-pdf.py -f <pdf_filename> <optional_args>` or `python read-pdf.py -f <pdf_filename> <optional_args>`

#### Command arguments
Provided script accepts arguments listed below:
- `-f <pdf_filename>` or `--file <pdf_filename>` - name of PDF that should be converted into audiobook.
- `-o <output_filename>` or `--output <output_filename>` (optional) - name of output .mp3 audiobook file. If not provided, default output filename format will be used.
- `-l <language>` or `--language <language>` (optional) - language of output audiobook. If not provided, output audiobook language will be English. You can check which languages are available using provided _list-langs.py_ script. Just run `<python3/python/py> list-langs.py`.

Example run of script on Linux: `python3 read-pdf.py -f harry-potter-1.pdf -o potter-audiobook.mp3 -l pl`