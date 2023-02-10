s = input()

def listofstr_reverse(s:str):
    words = []

    word = ""

    for c in s:
        if c == ' ':
            words.append(word)
            word = ""
        else:
            word += c

    words.append(word)
    words.reverse()

    return words

thislist = listofstr_reverse(s)

for x in thislist:
    print(x, end=' ')
