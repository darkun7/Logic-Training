def challenge2(words):
    number = 0
    lower = 0
    upper = 0
    for _ in words:
        if _.isnumeric():
            number+=1
        elif _.islower():
            lower+=1
        elif _.isupper():
            upper+=1
    print("Number of digits in sentence is %d"% number)
    print("Number of digits in sentence is %d"% int(words.count(" ")+1))
    print("Number of upper case letters in sentence is %d"% upper)
    print("Number of lower case letters in sentence is %d"% lower)

words = input("Enter a string: ")
challenge2(words)