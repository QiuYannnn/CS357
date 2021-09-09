
def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list


tweets = ["Happy #IlliniFriday!",
  "It is a pretty campus, isn't it, #illini?",
  "Diving into the last weekend of winter break like... #ILLINI #JoinTheFight",
  "Are you wearing your Orange and Blue today, #Illini Nation?"]

#change every character into lower case
tweets_lower = []
for s in tweets:
    tweets_lower.append(s.lower())

words = []
for i in range(len(tweets_lower)):
    words.append(tweets_lower[i].split())

wordsList = flatten(words)

res = []

#print(wordsList)
for i in range(len(wordsList)):
    if wordsList[i][0] == '#':
        myTuple = ()
        cnt = 0
        myTuple = (wordsList[i], 1)
        res.append(myTuple)
#print(res)
finalres=[]
count = []
for i in range(len(res)):
    count.append(res.count(res[i]))
    myTuple = (res[i][0],count[i])
    finalres.append(myTuple)
    
result = []
result = (set(finalres))

result_a=sorted(result,key=lambda t:t[0])

hashtag_counts=sorted(result_a,key=lambda t:t[1],reverse = True)
