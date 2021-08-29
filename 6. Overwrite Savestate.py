#text file writing reading then replacing
#!!!Problem: dont want to write the file completely new only replace the word searched
#else I could just f.write (...) at the bottom 

with open("6. Write and Read.txt", "w+") as f:
    f.write("You are Caleb" )
    f.seek(0)

    fr = f.read()
    wordSearching = "Caleb"
    wordReplace = "Tim"
    
    #for the replacement
    lengthWord = len(wordSearching)
    found = False

    #me testing the different ways for the problem at the bottom
    print(fr)
    print(lengthWord)
    print(fr.count(wordSearching))
    print(fr.find(wordSearching))
    
    start = fr.find(wordSearching)
    finish = start + lengthWord 
    replacedWord = fr[start:finish]
    print(replacedWord)
    
    #if the word exists
    if fr.count(wordSearching) > 0:
        found = True
        if found:
            #this should replace the last word but I dont know how and didn't find a solution
            f[replacedWord].write(wordReplace)
            
        else:
            pass
    else:
        print("Word not found")
        

    
