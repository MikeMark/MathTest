import random
import math
sqrt = math.sqrt
rand = random.randint
INC = 0
grd = ""
pyth = 1
    




#The actual program
#This is the first section (pythagorean theorem)
while pyth <= 5:
    pyth +=1
    print "If a = ", + rand(0, 11), ", and b = ", + rand(0, 33), ", then what is c?"
    print "Use the pythagorean theorem."
    print ""
    sda = float(input("Enter the length of side a: "))
    sib = float(input("Enter the length of side b: "))
    print ""
    print "Thank you"
    print ""
    ni = float(input("Type your answer here: "))
    cor = sqrt(pow(sda, 2) + pow(sib, 2))
    coru = cor + 1
    corl = cor - 1
    if ni<=coru and ni>=corl:
        print "Correct!"
        break
        print ""
        print ""
        print ""
    else:
        print "Wrong, try again."
        INC + 1
        print ""
        print ""
        print ""
print "Now, on to functions."

#the next section(not pythagorean theorem)
print "If the function is y = 2x + 5, and x = ", rand(1, 20), "what is y?"
print "There are 2 other function questions. You will be given them after this one."
x = float(input("Enter the number you were given here:   "))
y = (2 * x) + 5
yu = y + 1
yl = y - 1
questOne = float(input("Enter your answer here:   "))
if questOne <= yu and questOne >= yl:
    print "Correct!"
else:
    print "Incorrect!"
    INC + 1
print "Next question: If the function is e = 15h, and h =", rand(10, 30),  "what is e?"
h = float(input("Enter the number you were given here:   "))
e = 15 * h
eu = e + 1
el = e - 1
questTwo = float(input("Enter your answer here:   "))
if questTwo <= eu and questTwo >= el:
    print "Correct!"
else:
    print "Incorrect!"
    INC + 1
print "Next question: If the function is j = 3k + 9, and k =", rand(1, 10), "what is j?"
k = float(input("Enter the number you were given here:   "))
j = (3 * k) + 9
ju = j + 1
jl = j - 1
questThree = float(input("Enter your answer here:   "))
if questThree <= ju and questThree >= jl:
    print "Correct!"
else:
    print "Incorrect!"
    INC + 1




#the third section ()
print "This is the final section of the math test."
print "You will be given a grade on your progress in these three sections after you finsh this one."
print ""
print "This section is on inear and nonlinear functions. You will be assessed on your ability to properly find a linear or nonlinear function. There are 4 questions."
print ""
print ""
print "Question 1: the function is b = x cubed. Is the function linear or nonlinear?"





#the grades
if INC <= 1:
    grd = "A+"
elif INC <= 3:
    grd = "B"
elif INC <= 6:
    grd = "C-"
elif INC <= 8:
    grd = "D"
elif INC >= 9:
    grd = "F"

print "you got", INC, "questions wrong. You get a(n)" + grd + "."
