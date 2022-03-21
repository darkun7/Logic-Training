import textScore as ts

def contentOrdering(keyword, articles):
    articleScore = []
    articleAmount = len(articles)
    for _ in range(articleAmount):
        articleScore.append({
            "id"    : _,
            "score" : ts.textScore(keyword, articles[_]),
        })
    print(articleScore)
    for i in range(len(articleScore)-1):
        for j in range(0, len(articleScore)-i-1):
            if articleScore[j]["score"] > articleScore[j + 1]["score"] :
                articles[j], articles[j + 1] = articles[j + 1], articles[j]
    print(articles)


print(contentOrdering('cat and dog', 
[
  'When a dog chases Tom, it looks funny like a classic cat and dog story',
  'Sometimes Tom ate dog food and because of that the Dog was very angry and chased after Tom',
  'At home I have a cat and dog the cat named Tom and the dog named Dog. My cat and dog are so cute',
  'Tom is a ignorant cat and a dog is a calm animal. When Tom with other cats are like the king of cats',
  'Dog are usually quiet except when it comes to food'
]))
