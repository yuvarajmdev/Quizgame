print("welcome to computer quize game ! ".capitalize())
print("enter yes or no".upper())
score=0
user=input()
if user =="yes":
    print("let's play :)")
else:
    print("bye!")
print("1.most runs in ipl ?")
print("a.virat kholi")
print("b.suresh raina")
print("c.rohit sharma")
user=input()
if user=="a" or user == "virat kholi":
    print("correct")
    score+=1
else:
    print("incorrect")
print("2.most fours in ipl ?")
print("a.Gayle")
print("b.warner")
print("c.dhawan")
user=input()
if user=="c" or user == "dhawan":
    print("correct")
    score+=1

else:
    print("incorrect")
print("3.most six in ipl ?")
print("a.Rohit sharma")
print("b.chris gayle")
print("c.ms dhoni")
user=input()
if user=="b" or user == "chris gayle":
    print("correct")
    score+=1
else:
    print("incorrect")
print("4.hishest score in ipl ?")
print("a.chris gayle")
print("b.brendon mccullum")
print("c.virat kholi")
user=input()
if user=="a" or user == "chris gayle":
    print("correct")
    score+=1

else:
    print("incorrect")
print("5.best strike rate in ipl ?")
print("a.sunil narine")
print("b.andre russell")
print("c.krishappa gowtham ")
user=input()
if user=="c" or user == "krishnappa gowtham":
    print("correct")
    score+=1

else:
    print("incorrect")
print("6.most wickets in ipl ?")
print("a.lasith malinga")
print("b.bhaveneshwar kumar")
print("c.dj bravo")
user=input()
if user=="a" or user == "lasith malinga":
    print("correct")
    score+=1

else:
    print("incorrect")
print("7.best bowlling figuresin ipl ?")
print("a.Rashid khan")
print("b.lasith malinga")
print("c.alzarri joseph")
user=input()
if user=="c" or user == "alzharri joseph":
    print("correct")
    score+=1

else:
    print("incorrect")
print("8.best bowling averege in ipl ?")
print("a.dj bravo")
print("b.lungi ngidi")
print("c.imran thair")
user=input()

if user=="b" or user == "lungi ngidi":
    print("correct")
    score+=1

else:
    print("incorrect")
print("9.best economy in ipl ?")
print("a.rashid khan")
print("b.r aswin")
print("c.lasith malinga")
user=input()
if user=="a" or user == "rashid khan":
    print("correct")
    score+=1

else:
    print("incorrect")
print("10.most dots in ipl ?")
print("a.sandeep sharma")
print("b.sunil narine")
print("c.bhuvneshwar kumar")
user=input()

if user=="c" or user == "bhuvneshwar kumar":
    print("correct")
    score+=1

else:
    print("incorrect")
    
if score<=3:
    print("bad knowldge of cricket")
elif score>3 and score<=5:
    print("avarage knowlede of cricket")
elif score>5 and score<=8:
    print("good knowledge of cricket ")
elif score>8 and score<=10:
    print("excellent knowledge of cricket :)")
else:
    quit()
print("your total score = "+str((score/10)*100)+"%")
print("do you see correct answer ?   yes or no ")
user=input()
if user=="yes":
    print("(1).a.virat kholi")
    print("(2).c.dhawan")
    print("(3).b.chris gayle")
    print("(4).a.chris gayle")
    print("(5).c.krishappa gowtham ")
    print("(6).a.lasith malinga")
    print("(7).c.alzarri joseph")
    print("(8).b.lungi ngidi")
    print("(9).a.rashid khan")
    print("(10).c.bhuvneshwar kumar")
else:
    quit()

