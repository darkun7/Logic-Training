def getKeyWord(sentence):
    sentenceGroup = sentence.split(" ");
    combinations = [];
    value = '';
    for h in range(0,len(sentenceGroup)):
        slice = sentenceGroup[h:]
        value = ' '.join(slice)
        if (value not in combinations and len(value) > 1):
            combinations.append(value)
        for t in range(len(slice), 0, -1):
            value = ' '.join(sentenceGroup[h:t])
            if (value not in combinations and len(value) > 1):
                combinations.append(value)
    for w in sentenceGroup :
        if (w not in combinations and len(w) > 1):
            combinations.append(w)
    return combinations

# print(getKeyWord('clean white paper'))