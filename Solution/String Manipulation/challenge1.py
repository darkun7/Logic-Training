import string

def vowelsConsonant(words) -> int:
    amountVowels=0
    amountConsonants=0
    words = words.replace(' ','')
    for char in words:
        if char in "aeiouAEIOU":
            amountVowels+=1
        elif char not in string.punctuation:
            amountConsonants+=1
    return {
        'vowels': amountVowels,
        'consonants': amountConsonants
    }

def challenge1(words):
    vc = vowelsConsonant(words)
    vowel = vc['vowels']
    consonant = vc['consonants']
    print("Total number of Vowels in user entered string is %d"% vowel)
    print("Total number of Consonants in user entered string is %d"% consonant)
    print("Total number of Blanks in user entered string is %d"% words.count(" "))

words = input("Enter a string: ")
challenge1(words)