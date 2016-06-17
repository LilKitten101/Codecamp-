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
numbermessage = input("What is your favorite number?(Only pick a number between 1 and 99.)    ")
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

elif 30 < numbermessage < 40:
    print("You will leave the life you have now and become a famous singer! You will live the rest of your life with fame and fortune, but it will go to your head. you will become a brat and only your fans who don't know you will like you.")
elif 40 < numbermessage < 50:
    print("You will become a famous chef! You will not have a lot of money, or be famous, but you will love your job.")
elif 50 < numbermessage < 60:
    print("You will become a robber and end up in jail for stealing out of a jewelery store")
elif 60 < numbermessage < 70:
          print("You will become an escaped convict, and live your life on the run. When you are very old you will move to another contenent, and start a new life as a cook in a food truck.")
elif 70 < numbermessage < 80:
          print("You will become a doctor. You will hate your job because you faint at the sight of blood.")
elif 80 < numbermessage < 90:
          print("You will become the world's first time traveler. You will go back to when you were four and remember your dream to become a racecar driver. You follow this dream and you end up being in N.A.S.C.A.R")
            
elif 90 < numbermessage < 100:
          print("You will become very sucsessful lawyer, but will quit your job when your mad that you failed a case")
          
    
#Thanks them for playing the game

print("Thank you for playing Lily's fortune telling game. I hope you are satisfied with your future.:)")
likeitmessage = input("Did you like the game? Say yes or no.    ")
#Asks for their opinion
if likeitmessage = yes:
    print("Thank you so much! Tell your friends!")
if likeitmessage = no:
    print("Wow! That's so mean! Nevr play this game again!")
