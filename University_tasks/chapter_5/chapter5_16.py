word = "ZZZZZWWWWWQQQQQRRRRRYYYYYUUUUU"
latters = {}

# count how many latters in word and if isnt exsist add to dict
for i in word:
    if i not in latters:
        latters[i] = 1
    else:
        latters[i] += 1

# make the word
for i in latters:
    print(i * latters[i], end="")


