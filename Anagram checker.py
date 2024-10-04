word1=input("enter word 1:").lower()
word2=input("enter word 2:").lower()

word1ActualList=[]
word2ActualList=[]

for letter in word1:
    word1List=[]
    word1List.append(letter)
    word1ActualList += word1List
print(sorted(word1ActualList))

for letter in word2:
    word2List = []
    word2List.append(letter)
    word2ActualList+=word2List
print(sorted(word2ActualList))

if sorted(word1ActualList)==sorted(word2ActualList):
    print("is an anagram!")
else:
    print("no anagram")