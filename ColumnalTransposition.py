def main():
    myMessage = "Common sense is not so common."
    myKey = 8

    cipherText = encryptMessage(myKey, myMessage)
    print(cipherText + "|")


def encryptMessage(key, message):
    cipherText = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]

            currentIndex += key
    return ''.join(cipherText)


if __name__ == '__main__':
    main()


