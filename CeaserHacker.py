while True:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuuvwxyz1234567890 !?.'

    message = input("enter text to be decrypted...\n")

    for key in range(len(SYMBOLS)):

        translated = ''
        for digit in message:

            if digit in SYMBOLS:

                translatedIndex = SYMBOLS.find(digit) - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                else:
                    pass

                translated = translated + SYMBOLS[translatedIndex]

            else:
                translated = translated + digit

        print("key #%s: %s" % (key, translated))