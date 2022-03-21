def challenge3(words):
    listWords = []
    for _ in words:
        if _.islower():
            listWords.append(_.upper())
        elif _.isupper():
            listWords.append(_.lower())
        else:
            listWords.append(_)
    print("The modified string is %s"% ''.join(listWords))

words = input("Enter a string: ")
challenge3(words)