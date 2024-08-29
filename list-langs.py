import gtts


def main():
    for shortcut, lang in gtts.tts.tts_langs().items():
        print(f'{lang} ({shortcut})')


if __name__ == '__main__':
    main()
