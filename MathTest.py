import random
import math
sqrt = math.sqrt
rand = random.randint
INC = 0
grd = ""
pyth = 1
def right(correct):
    if correct:
        print "Correct!\n"
    else:
        print "Wrong, try again.\n"
        INC + 1
    




#The actual program
#This is the first section (pythagorean theorem)
correct = False; #this doesn't work....
while pyth <= 5 or not correct:
    pyth +=1
    my_a = rand(0, 11)
    my_b = rand(0, 33)
    print "If a = ", + my_a, ", and b = ", + my_b, ", then what is c?"
    print "Use the pythagorean theorem."
    print ""
    sda = my_a
    sib = my_b
    print ""
    print "Thank you"
    print ""
    ni = float(input("Type your answer here: "))
    cor = sqrt(pow(sda, 2) + pow(sib, 2))
    coru = cor + 1
    corl = cor - 1
    correct = (ni <= coru and ni >= corl)
    right(correct)
print "Now, on to functions."

#the next section(not pythagorean theorem)
varx = rand(1, 20)
print "If the function is y = 2x + 5, and x = ", varx, "what is y?"
print "There are 2 other function questions. You will be given them after this one."
y = (2 * varx) + 5
yu = y + 1
yl = y - 1
questOne = float(input("Enter your answer here:   "))
correct = (questOne <= yu and questOne >= yl)
right(correct)
varh = rand(10, 30)
print "Next question: If the function is e = 15h, and h =", varh,  "what is e?"
e = 15 * varh
eu = e + 1
el = e - 1
questTwo = float(input("Enter your answer here:   "))
correct = (questTwo <= eu and questTwo >= el)
right(correct)
vark = rand(1, 10)
print "Next question: If the function is j = 3k + 9, and k =", vark, "what is j?"
j = (3 * vark) + 9
ju = j + 1
jl = j - 1
questThree = float(input("Enter your answer here:   "))
correct = (questThree <= ju and questThree >= jl)
right(correct)




#the third section ()
print "This is the final section of the math test."
print "You will be given a grade on your abilities in these three sections after you finsh this one."
print ""
print "This section is on multidigit multiplication. there are 4 questions. Good luck!"
print ""
print ""
allqsyea = rand(1, 2000)
print "1.  What is ", allqsyea, "*", allqsyea, "?\n"
qNO = 123 * 1345
qNOu = qNO + 5
qNOl = qNO - 5
ansonefloat(input("Type your answer here:  "))
correct = (ansone <= qNOu and ansone >= qNOl)
right(correct)
print "2.  What is ", allqsyea, "*", allqsyea, "?\n"
qNT = 1500 * 5
qNTu = qNT + 2
qNTl = qNT - 2
anstwo = float(input("Type your answer here:  "))
correct = (anstwo <= qNTu and anstwo >= qNTl)
right(correct)
print "3.  What is ", allqsyea, "*", allqsyea, "?\n"
qNTh = 550.345 * 0.0001
qNThu = qNTh + 2
qNThl = qNTh - 2
ansthree = float(input("Type your answer here:  "))
correct = (ansthree <= qNThu and ansthree >= qNThl)
right(correct)
print







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

print "You got", INC, "questions wrong.\n"
print "Grade: " + grd
