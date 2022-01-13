import re 
import keywords as kw

def score(keywords, found):
    split = len(keywords.split())**2
    return split*found

def textScore(keyword, text):
    point = 0
    text = text.lower()
    keyword = keyword.lower()
    keywords = kw.getKeyWord(keyword)
    for keyword in keywords:
        pattern = re.compile(r'('+keyword+')')
        match = len(pattern.findall(text))
        point += score(keyword,match)
    text = "Point final {}\n".format(point)
    return point

# keywords = 'cat and dog'
# article = 'At home I have a cat and dog the cat named Tom and the dog named Dog. My cat and dog are so cute'
# print(textScore(keywords, article))
  
