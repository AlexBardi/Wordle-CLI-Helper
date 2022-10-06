def main():
    print("What are the black letters?")
    blackIn = input(">")
    blackSet = set()
    if blackIn != '':
        for letter in blackIn:
            blackSet.add(letter)

    print("What are the yellows? Write the letter and position in this format (0 indexed):")
    print("a0,b1,c2,d3,e4")
    yellowIn = input(">") 
    yellowSet = set()
    yellowPairs = []
    if yellowIn != '':
        for point in yellowIn.split(','):
            yellowSet.add(point[0])
            yellowPairs.append(point)

    print("What are the greens? Write the letter and position in this format (0 indexed):")
    print("a0,b1,c2,d3,e4")
    greenIn = input(">") 
    greenSet = set()
    greenPos = {}
    if greenIn != '':
        for point in greenIn.split(','):
            greenSet.add(point[0])
            greenPos[point[0]] = int(point[1])

    blackSet.difference_update(yellowSet)
    blackSet.difference_update(greenSet) # removes any letters that were accidentally added 


    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"}
    special = {"-", ".", "!", "'", "0", "1",
            "2", "3", "4", "5", "6", "7", "8", "9"}

    words = open("english_words.txt")

    wordlist = set(())
    for word in words:
        wordlist.add(str(word).lower()[:-1])
    for word in wordlist:
        if len(word) == 5:
            if all(letter in alphabet for letter in word) == True:
                if any(letter in special for letter in word) == False:
                    if any(letter in blackSet for letter in word) == False:
                        if all(letter in word for letter in yellowSet) == True:
                            if all(letter in word for letter in greenSet) == True:
                                if not yellowPairs or any(pair[0] == word[int(pair[1])] for pair in yellowPairs) == False:
                                    if not greenPos or all(letter == word[greenPos[letter]] for letter in greenPos) == True:
                                        print(word)


main()


