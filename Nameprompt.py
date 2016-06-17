#prompt making/survey Lily Ahluwalia 6/14/2016
#asking survey questions
namemessage = input("what is your name?    ")
agemessage = input("how old are you?   ")
colormessage = input ("what is your favorite color?   ")
animalmessage = input("what is your favorite animal?     ")
#doing math to calculate double the age number and how old they would be in dog years
print ("This will be how old you are when you're double your age.")
print(int(agemessage)*2)
print("This is how old you would be in dog years")
print(int(agemessage)*7)
print("Wow, you would be a very old dog!")
#picking a number that "determines" their future
numbermessage = input("What is your favorite number?(Only put a number between 1 and 29.)    ")
print("Now I will tell you're future!")
namemessage
#Uses if and elif statements to determine the future
numbermessage = int(numbermessage)
if  numbermessage < 10:
    print("You will have a horrible future! You will live a very bad life, but you will still have the next two years before your life turns bad. Be careful not to make bad choices!:)")

elif 10 < numbermessage < 20:
    print("You will live a very boring life. You will have no regrets, but will never be happy. You will never find somthing you'll love,wilol end up spending most of your days, lying on the couch,watching TV")
elif 20 < numbermessage < 30:
    print("You will have an amazing life! You will have a job you'll enjoy, you'll live in a mansion that's your favorite color with a million of your favorite animal,and you'll have no regrets at all.")
#Thanks them for playing the game

print("Thank you for playing Lily's fortune telling game. I hope you are satisfied with your future.:)")
likeitmessage = input("Did you like the game?    ")
#Asks for their opinion
print("Thank you for your opinion. Please tell your friends")
