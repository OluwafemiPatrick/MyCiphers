while True:

    message = input('enter your message...\n')

    key: int = 8

    mode = input("enter 'e' to encrypt or 'd' to decrypt message \n")

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex: int = 0

            if mode == 'e':
                translatedIndex = symbolIndex + key
            elif mode == 'd':
                translatedIndex = symbolIndex - key
            else:
                print("ERROR! mode can only be 'e' or 'd' ")
                break

            """
                The translatedIndex is the index of the digit in SYMBOL plus
                the key in use. If translatedIndex > 67 which is the len(SYMBOLS),
                SYMBOLS[translatedIndex], which is the index of translated in
                SYMBOLS now return a string index out of range error.
                To handle this we do the following...
            """
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol

    print(translated)