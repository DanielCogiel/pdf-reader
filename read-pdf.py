from PyPDF2 import PdfReader
from gtts import gTTS
import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True, help='PDF file to convert')
    parser.add_argument('-l', '--language', type=str, required=False, help='Language of generated audiobook')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output mp3 filename')

    args = parser.parse_args()
    reader = PdfReader(args.file)

    content = ''
    for page in reader.pages:
        content += page.extract_text() + '\n'

    if content:
        tts = gTTS(content, lang=args.language or 'en')
        tts.save(args.output or f'{os.path.splitext(args.file)[0]}-audiobook.mp3')
    else:
        print('PDF is empty.')


if __name__ == '__main__':
    main()
