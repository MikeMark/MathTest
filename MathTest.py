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
        correct = True
    else:
        print "Wrong.\n"
        INC + 1
    




#The actual program
#This is the first section (pythagorean theorem)
correct = False
print "THIS IS THE FIRST SECTION: PYTHAGOREAN THEOREM\n"
while pyth <= 5 or correct==False:
    my_a = rand(0, 11)
    my_b = rand(0, 33)
    print "If a = ", + my_a, ", and b = ", + my_b, ", then what is c?\n"
    print "Use the pythagorean theorem.\n\n"
    sda = my_a
    sib = my_b
    ni = float(input("Type your answer here: "))
    cor = sqrt(pow(sda, 2) + pow(sib, 2))
    coru = cor + 1
    corl = cor - 1
    correct = (ni <= coru and ni >= corl)
    right(correct)
    if correct is True:
        pyth += 5
    else:
        pyth += 1
print "NOW, ON TO FUNCTIONS.\n"

#the next section(not pythagorean theorem)
varx = rand(1, 20)
print "If the function is y = 2x + 5, and x = ", varx, "what is y?\n"
print "There are 2 other function questions. You will be given them after this one.\n"
y = (2 * varx) + 5
yu = y + 1
yl = y - 1
questOne = float(input("Enter your answer here(number only):   "))
correct = (questOne <= yu and questOne >= yl)
right(correct)
varh = rand(10, 30)
print "\nNext question: If the function is e = 15h, and h =", varh,  "what is e?\n"
e = 15 * varh
eu = e + 1
el = e - 1
questTwo = float(input("Enter your answer here(number only):   "))
correct = (questTwo <= eu and questTwo >= el)
right(correct)
vark = rand(1, 10)
print "\nNext question: If the function is j = 3k + 9, and k =", vark, "what is j?\n"
j = (3 * vark) + 9
ju = j + 1
jl = j - 1
questThree = float(input("Enter your answer here(number only):   "))
correct = (questThree <= ju and questThree >= jl)
right(correct)




#the third section ()
print "\nTHIS IS THE FINAL SECTION."
print "\nYou will be given a grade on your abilities in these three sections after you finsh this one."
print ""
print "\nThis section is on multidigit multiplication. there are 4 questions. Good luck!"
print ""
print ""
print "1.  What is 123 * 1,345?\n"
qNO = 123 * 1345
qNOu = qNO + 5
qNOl = qNO - 5
ansone = float(input("Type your answer here:  "))
correct = (ansone <= qNOu and ansone >= qNOl)
right(correct)
print "\n2.  What is 1,500 * 5?\n"
qNT = 1500 * 5
qNTu = qNT + 2
qNTl = qNT - 2
anstwo = float(input("Type your answer here:  "))
correct = (anstwo <= qNTu and anstwo >= qNTl)
right(correct)
print "\n3.  What is 550.345 * 0.0001?\n"
qNTh = 550.345 * 0.0001
qNThu = qNTh + 2
qNThl = qNTh - 2
ansthree = float(input("Type your answer here:  "))
correct = (ansthree <= qNThu and ansthree >= qNThl)
right(correct)
print "\n4.  What is 934 * 313?\n"
qNF = 934 * 313
qNFu = qNF + 3
qNFl = qNF - 3
ansfour = float(input("Type your answer here:  "))
correct = (ansfour <= qNFu and ansfour >= qNFl)
right(correct)







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

print "\n\n\nYou got", INC, "questions wrong.\n"
print "Grade: " + grd

