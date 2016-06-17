speech = {"hello":"arrrr","friend":"matey","people":"scallywags"}
def engtopirate(englishstring):
    englishlist = englishstring.split(" ")

    piratese = ""

    for word in englishlist:
        print("Right now I'm looking at word <%s>" %word)
        if word in speech:
            print("I found the word! Piratese now is:")
            piratese = piratese + " " + speech[word]
            
        else:
            piratese = piratese  + word
    return piratese
piratephrase = engtopirate("hello my people friend")
print(piratephrase)
            
             
