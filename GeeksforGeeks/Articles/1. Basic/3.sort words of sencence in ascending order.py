def sortedSenetece(Sentence):
    words = Sentence.split(" ")

    words.sort()

    newSentence = " ".join(words)

    return newSentence


Sentence = 'to learn programming refer geeksforgeeks'
print(sortedSenetece(Sentence))

Sentence = "geeks for geeks"
print(sortedSenetece(Sentence))
