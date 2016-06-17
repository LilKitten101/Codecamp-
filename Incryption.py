
def shrug(plaintext):
    alph = "abcdefghijklmnopqrstuvwxyz0123456789"
    cyphertext = ""
    key = 7
    for char in plaintext:
        pti = alph.find(char)
        cti = pti + key
        cti = cti % len(alph)
        newc = alph[cti]
        print(newc)
        cyphertext = cyphertext + newc
    return cyphertext
shrug(plaintext = "1am2am9am")

