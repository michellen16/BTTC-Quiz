# Final Project
# CS 111, Reckinger, August 4, 2023
# This program was made by Michelle Nguyen and Stephanie Quintana. The program acts as small self assessment 
# to persuade the user to join Break Through Tech.
# The user will explore Computer Science, women in STEM, and more about Break Through Tech. 

# Libraries needed for program to run 
import turtle
import random
import matplotlib.pyplot as plt

# setup of turtle and screen
t = turtle.Turtle()
s = turtle.Screen()

# adding shapes and buttons
turtle.addshape("square.gif")
turtle.addshape("enterbutton.gif")
turtle.addshape("yesbutton.gif")
turtle.addshape("nobutton.gif")
turtle.addshape("answer.gif")
turtle.addshape("facts.gif")
turtle.addshape("next.gif")
turtle.addshape("fact1.gif")
turtle.addshape("fact2.gif")
turtle.addshape("fact3.gif")
turtle.addshape("fact4.gif")
turtle.addshape("womenbutton.gif")
turtle.addshape("menbutton.gif")
turtle.addshape("backbutton.gif")
turtle.addshape("plot.gif")
turtle.addshape("Adalovelace.gif")
turtle.addshape("Hedylamarr.gif")
turtle.addshape("Gracehopper.gif")
turtle.addshape("adafact.gif")
turtle.addshape("hedyfact.gif")
turtle.addshape("gracefact.gif")
turtle.addshape("begin.gif")

# background function
def background():
    s.bgcolor("midnight blue")
    square = turtle.Turtle()
    square.shape("square.gif")
    square.goto(0, 0)

# sets up answer screen function 
def answerscreen():
    answer = turtle.Turtle()
    answer.shape("answer.gif")
    answer.goto(-5, -10)

# formats text function 
def textinfo(x, y, text1, text2, text3, text4, text5):
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(text1, align = text2, font = (text3, text4, text5))

# welcome screen function
def welcomescreen():
    turtle.clearscreen()
    background()
    textinfo(0, 200, "Welcome!", "center", "Times", 70, "bold")
    textinfo(0, 150, "Before starting this interactive quiz, what is your name/nickname?", "center", "Times", 19, "normal")
    textinfo(0, -50, "___________", "center", "Times", 80, "normal")
    enter = turtle.Turtle()
    enter.shape("enterbutton.gif")
    enter.hideturtle()
    enter.penup()
    enter.goto(28, -150)
    enter.showturtle()
    print("Please enter name/nickname:")
    name = input() # Tells the user to input name 
    done = False
    while not done: # Loop where user must enter a name to continue with program
        if name == "":
            print("Please enter name/nickname:")
            name = input()
        else:
            print("Hello!")
            done = True
    textinfo(0, -25, name, "center", "Times", 45, "normal")
    enter.onclick(enterbutton) # When user clicks enter button, the next function occurs
    return(name)

# Function to bypass the parameters 
def gotofirstquestion(): 
    firstquestion(0,0)

# Start up screen when user first clicks the event driven component 
def enterbutton(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 20, "Thank you " + name + ".", "center", "Times", 50, "bold")
    textinfo(0, -40, "We hope you will enjoy this interactive quiz! :D", "center", "Times", 25, "normal")
    s.ontimer(gotofirstquestion, 3000)

# First question screen function 
def firstquestion(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 100, "QUESTION 1", "center", "Times", 50, "bold")
    textinfo(0, 30, "Do you have any prior knowledge about Computer Science?", "center", "Times", 21, "normal")
    yesbutton = turtle.Turtle()
    yesbutton.shape("yesbutton.gif")
    yesbutton.hideturtle()
    yesbutton.penup()
    yesbutton.goto(-10, -100)
    yesbutton.showturtle()
    yesbutton.onclick(yesresponse_q1) # If user clicks yes button, it moves on to a function
    nobutton = turtle.Turtle()
    nobutton.shape("nobutton.gif")
    nobutton.hideturtle()
    nobutton.penup()
    nobutton.goto(-10, -250)
    nobutton.showturtle()
    nobutton.onclick(noresponse_q1) # If user clicks no button, it moves on to a different function

# Function to bypass the parameters 
def gotofactscreen():
    factscreen(0, 0)

# Function for user to be taken to facts screen where there are multiple button setups. 
def factscreen(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 250, "Computer Science Facts!", "center", "Times", 45, "bold")
    fact1 = turtle.Turtle()
    fact1.shape("fact1.gif")
    fact1.hideturtle()
    fact1.penup()
    fact1.goto(-170, 150)
    fact1.showturtle()
    fact2 = turtle.Turtle()
    fact2.shape("fact2.gif")
    fact2.hideturtle()
    fact2.penup()
    fact2.goto(170, 150)
    fact2.showturtle()
    fact3 = turtle.Turtle()
    fact3.shape("fact3.gif")
    fact3.hideturtle()
    fact3.penup()
    fact3.goto(-170, 0)
    fact3.showturtle()
    fact4 = turtle.Turtle()
    fact4.shape("fact4.gif")
    fact4.hideturtle()
    fact4.penup()
    fact4.goto(170, 0)
    fact4.showturtle()
    next1 = turtle.Turtle()
    next1.shape("next.gif")
    next1.hideturtle()
    next1.penup()
    next1.goto(170, -290)
    next1.showturtle()
    backbutton1 = turtle.Turtle()
    backbutton1.shape("backbutton.gif")
    backbutton1.hideturtle()
    backbutton1.penup()
    backbutton1.goto(-170, -290)
    backbutton1.showturtle()
    textinfo(0, -150, "When you're done, move on to the next question.", "center", "Times", 20, "bold")
    textinfo(0, -200, "Or you can go back to first question.", "center", "Times", 20, "bold")
# Multiple event driven choices based on which fact button user clicks 
    fact1.onclick(fact1screen)
    fact2.onclick(fact2screen)
    fact3.onclick(fact3screen)
    fact4.onclick(fact4screen)
    next1.onclick(secondquestion)
    backbutton1.onclick(firstquestion)

# If fact 1 button is clicked, this function runs
def fact1screen(x, y):
    answerscreen()
    textinfo(0, 100, "FACT 1:", "center", "Times", 80, "bold")
    textinfo(0, 0, "Computer science is the study and principle", "center", "Times", 30, "normal")
    textinfo(0, -80, "of computers and computational system.", "center", "Times", 30, "normal")
    s.ontimer(gotofactscreen, 5000) # Timer for user to see fact 1

# If fact 2 button is clicked, this function runs 
def fact2screen(x, y):
    answerscreen()
    textinfo(0, 100, "FACT 2:", "center", "Times", 80, "bold")
    textinfo(0, 0, "There are various programming languages that are included", "center", "Times", 25, "normal")
    textinfo(0, -80, "but not limited to: Python, JavaScript, C++, Java, HTML, etc.", "center", "Times", 25, "normal")
    s.ontimer(gotofactscreen, 5000) # Timer for user to see fact 2

# If fact 3 button is clicked, this function runs 
def fact3screen(x, y):
    answerscreen()
    textinfo(0, 100, "FACT 3:", "center", "Times", 80, "bold")
    textinfo(0, 0, "Computer science is a booming market! It has many different career", "center", "Times", 22, "normal")
    textinfo(0, -80, "paths: Software/Web developer, Programmers, UI/UX Designers, and more.", "center", "Times", 22, "normal")
    s.ontimer(gotofactscreen, 5000) # Timer for user to see fact 3

# If fact 4 button is clicked, this function runs
def fact4screen(x, y):
    answerscreen()
    textinfo(0, 100, "FACT 4:", "center", "Times", 80, "bold")
    textinfo(-400, 0, "You can do so many things in", "left", "Times", 20, "normal")
    textinfo(-400, -50, "Computer Science! For example, we can", "left", "Times", 20, "normal")
    textinfo(-400, -100, "create a program to draw flowers.", "left", "Times", 20, "normal")
    flower() # Calls the flower function 
    s.ontimer(gotofactscreen, 7000) # Timer for user to see fact 4

# Function using turtle graphics where user will see a flower being drawn
def flower(): 
    turtle.speed(10)
    turtle.width(10)
    for i in range(7):
        turtle.color("midnight blue")
        turtle.fillcolor("midnight blue")
        turtle.penup()
        turtle.goto(240, -50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(100, 80)
        turtle.left(100)
        turtle.circle(100, 80)
        turtle.end_fill()
    turtle.color("green yellow")
    turtle.fillcolor("green yellow")
    turtle.penup()
    turtle.goto(250, -80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()

# Function that will be used if user clicks "Yes" on the first question
def yesresponse_q1(x, y):
    answerscreen()
    textinfo(0, 30, "That's great!", "center", "Times", 80, "bold")
    textinfo(0, -15, "You can choose to learn some CS facts for fun, or, move on to the next question.", "center", "Times", 20, "normal")
    facts = turtle.Turtle()
    facts.shape("facts.gif")
    facts.hideturtle()
    facts.penup()
    facts.goto(-200, -90)
    facts.showturtle()
    facts.onclick(factscreen) # User is given the choice to go to facts screen 
    next1 = turtle.Turtle()
    next1.shape("next.gif")
    next1.hideturtle()
    next1.penup()
    next1.goto(210, -125)
    next1.showturtle()
    next1.onclick(secondquestion) # User is given the choice to go to the next question

# Function that will be used if user clicks "No" on the first question
def noresponse_q1(x, y):
    answerscreen()
    textinfo(0, 30, "That's OK!", "center", "Times", 80, "bold")
    textinfo(0, -15, "Here are some interesting computer science facts.", "center", "Times", 30, "normal")
    facts = turtle.Turtle()
    facts.shape("facts.gif")
    facts.hideturtle()
    facts.penup()
    facts.goto(0, -90)
    facts.showturtle()
    facts.onclick(factscreen) # User can click on facts button which will go to the facts screen function

# Function where the user will see the second question of the program 
def secondquestion(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 100, "QUESTION 2", "center", "Times", 50, "bold")
    textinfo(0, 30, "Do you identify as either female or nonbinary?", "center", "Times", 25, "normal")
    yesbutton = turtle.Turtle()
    yesbutton.shape("yesbutton.gif")
    yesbutton.hideturtle()
    yesbutton.penup()
    yesbutton.goto(-10, -100)
    yesbutton.showturtle()
    yesbutton.onclick(yesreponse_q2) # If user clicks on a "Yes" button, the second yes function will occur
    nobutton = turtle.Turtle()
    nobutton.shape("nobutton.gif")
    nobutton.hideturtle()
    nobutton.penup()
    nobutton.goto(-10, -250)
    nobutton.showturtle()
    nobutton.onclick(noreponse_q2) # If user click on a "No" button, the second no function will occur

# If user clicks "Yes" for the second question, this function will occur 
def yesreponse_q2(x, y):
    answerscreen()
    textinfo(0, 30, "It was great learning more about you!", "center", "Times", 40, "bold")
    textinfo(0, -30, "Let's further explore gender in the Computer Science field.", "center", "Times", 25, "normal")
    s.ontimer(thirdquestion, 3000) # User will automatically be taken to the third question

# If user clicks "No" for the second question, this function will occur
def noreponse_q2(x, y):
    answerscreen()
    textinfo(0, 150, "Thank you for playing our interactive quiz!", "center", "Times", 35, "bold")
    textinfo(0, 90, "Unfortunately, Break Through Tech Chicago focuses on gender", "center", "Times", 20, "normal")
    textinfo(0, 40, "diversity for women and nonbinary students. However, there are plenty of", "center", "Times", 20, "normal")
    textinfo(0, -10, "clubs and programs to join for Computer Science. You can use this", "center", "Times", 20, "normal")
    textinfo(0, -60, "link here: (https://cs.uic.edu/undergraduate/student-organizations/).", "center", "Times", 20, "normal")
    textinfo(0, -150, "If you know anyone interested in CS and identifies as nonbinary or a woman, they can", "center", "Times", 18, "normal")
    textinfo(0, -200, "join BTTC linked here: (https://chicago.breakthroughtech.org/get-involved/membership/).", "center", "Times", 18, "normal")
    print("CS clubs: https://cs.uic.edu/undergraduate/student-organizations/ ")
    print("BTTC link for your friend: https://chicago.breakthroughtech.org/get-involved/membership/")
    # User is not taken to another screen and the program will print out links

# function where the user will see the third question
def thirdquestion():
    turtle.clearscreen()
    background()
    textinfo(0, 100, "QUESTION 3", "center", "Times", 50, "bold")
    textinfo(0, 50, "Now we are going to look at Google Trends!", "center", "Times", 21, "normal")
    textinfo(0, 0, "Which Google search term do you think is the most", "center", "Times", 21, "normal")
    textinfo(0, -50, "popular within the past 90 days?", "center", "Times", 21, "normal")
    womenbutton = turtle.Turtle()
    womenbutton.shape("womenbutton.gif")
    womenbutton.hideturtle()
    womenbutton.penup()
    womenbutton.goto(0, -125)
    womenbutton.showturtle()
    # when user clicks on this turtle it will go to the womencs function screen
    womenbutton.onclick(womencs)
    menbutton = turtle.Turtle()
    menbutton.shape("menbutton.gif")
    menbutton.hideturtle()
    menbutton.penup()
    menbutton.goto(0, -250)
    menbutton.showturtle()
    # when user clicks on this it will go to the mencs function screen
    menbutton.onclick(mencs)

# this the function the user will see if they clicked the womenbutton turtle
def womencs(x, y):
    answerscreen()
    textinfo(0, 30, "Actually, that's incorrect.", "center", "Times", 60, "bold")
    textinfo(0, -15, "You would think 'Women in CS' would be more popular", "center", "Times", 25, "normal" )
    textinfo(0, -50, "but unfortunately that is not the case. Most men still dominate", "center", "Times", 25, "normal")
    textinfo(0, -90, "CS and tech related fields. Let's look at the data.", "center", "Times", 25, "normal")
    # this function will go to the dataplot function after a certain time
    s.ontimer(dataplot, 5000)

def mencs(x, y):
    answerscreen()
    textinfo(0, 30, "That's correct!", "center", "Times", 60, "bold")
    textinfo(0, -15, "What a bummer... Let's look at the data.", "center", "Times", 25, "normal" )
    # this function will go to the dataplot function after a certain time
    s.ontimer(dataplot, 3000)

# this function helps clean the data by getting rid of values less than 1 and replacing it with 0
def clean_data(list):
    for i in range(len(list)):
        if list[i] == "<1\n" or list[i] == "<1":
            list[i] = 0
        else:
            list[i] = int(list[i])

# this function sets up the graph using the data from the txt files
def dataplot():
    answerscreen()
    # Opening Data Below
    # opens file
    file1 = open("MenData.txt")
    # turns the file into a list
    list1 = file1.readlines()
    # calls this function to clean the data
    clean_data(list1)
    # will plot the data and change the line appearance
    plt.plot(list1, '--')
    # opens file
    file2 = open("WomenData.txt")
    # turns it into a list
    list2 = file2.readlines()
    # calls function to clean the data
    clean_data(list2)
    # plots the data and changes line appearance
    plt.plot(list2, '-')
    # gives the graph a title
    plt.title("Gender in CS Search Trends (of the Last 90 Days)")
    # labels the y-axis of the graph
    plt.ylabel("Number of Searches")
    # labels the x-axis of the graph
    plt.xlabel("Time")
    # adds a key identifying which line is which
    plt.legend(["Men in CS", "Women in CS"])
    # lines 387-389 formats the ticks on the x axis better (labels each tick and puts the desired amount of ticks)
    date_list = ["4.30.23", "5.22.23", "6.13.23", "7.5.23" ]
    ticks = range(0, 88, 22)
    plt.xticks(ticks, date_list)
    # saves an image of the graph, allows us to then convert it to a gif and place it where we want on the screen
    plt.savefig("plot.png")
    # this where we use that saved image of the graph
    showplt = turtle.Turtle()
    showplt.shape("plot.gif")
    showplt.hideturtle()
    showplt.penup()
    showplt.goto(-150, 0)
    showplt.showturtle()
    textinfo(280, 100, "When you're done,", "center", "Times", 22, "bold")
    textinfo(280, 50, "you can move on to", "center", "Times", 22, "bold")
    textinfo(280, 0, "the next question.", "center", "Times", 22, "bold")
    next2 = turtle.Turtle()
    next2.shape("next.gif")
    next2.hideturtle()
    next2.penup()
    next2.goto(280, -100)
    next2.showturtle()
    # when the user clicks this turtle, it goes to the fourthquestion function
    next2.onclick(fourthquestion)
    
# this is where the user will see the fourth question function
def fourthquestion(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 250, "MATCHING GAME", "center", "Times", 50, "bold")
    textinfo(0, 150, "Although women are hardly represented", "center", "Times", 25, "normal")
    textinfo(0, 100, "in Computer Science and tech, they have played", "center", "Times", 25, "normal")
    textinfo(0, 50, "a huge role in the history of Computer Science!", "center", "Times", 25, "normal")
    textinfo(0, -50, "You will now learn more about these influential", "center", "Times", 25, "normal")
    textinfo(0, -100, "women, by playing a match game! Match the", "center", "Times", 25, "normal")
    textinfo(0, -150, "name to the correct fact.", "center", "Times", 25, "normal")
    beginbutton = turtle.Turtle()
    beginbutton.shape("begin.gif")
    beginbutton.hideturtle()
    beginbutton.penup()
    beginbutton.goto(0, -280)
    beginbutton.showturtle()
    # when the user clicks this turtle, it will go to the match1 function
    beginbutton.onclick(match1)

# this function is to bypass parameters
def gotomatch1():
    match1(0, 0)

# this function is for when the user clicks the correct turtle, this will appear
def round1correct(x, y):
    answerscreen()
    textinfo(0, 80, "CORRECT!", "center", "Times", 60, "bold")
    textinfo(0, 40, "Augusta Ada Lovelace is known as the first computer programmer", "center", "Times", 22, "normal")
    textinfo(0, 10, "since she was able to take data which was translated into information.", "center", "Times", 22, "normal")
    textinfo(0, -20, " Her work led to the development of a general computer. ", "center", "Times", 22, "normal")
    nextround = turtle.Turtle()
    nextround.shape("next.gif")
    nextround.hideturtle()
    nextround.penup()
    nextround.goto(0, -100)
    nextround.showturtle()
    # when the user clicks this, it will go to the match2 function (2nd round of game)
    nextround.onclick(match2)

# this function is for when the user chooses the wrong turtle, this will appear
def round1incorrect(x, y):
    answerscreen()
    textinfo(0, 30, "INCORRECT!", "center", "Times", 80, "bold")
    textinfo(0, -70, "Try Again.", "center", "Times", 40, "normal")
    # after a certain amount of time, it will go back to the match1 function
    s.ontimer(gotomatch1, 2000)

# this function is where the user will see round 1 of the game
def match1(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 250, "ROUND 1", "center", "Times", 60, "bold")
    adalovelace = turtle.Turtle()
    adalovelace.shape("Adalovelace.gif")
    adalovelace.hideturtle()
    adalovelace.penup()
    adalovelace.goto(-200, 0)
    adalovelace.showturtle()
    adafact = turtle.Turtle()
    adafact.shape("adafact.gif")
    adafact.hideturtle()
    adafact.penup()
    adafact.goto(200, 150)
    adafact.showturtle()
    gracefact = turtle.Turtle()
    gracefact.shape("gracefact.gif")
    gracefact.hideturtle()
    gracefact.penup()
    gracefact.goto(200, -50)
    gracefact.showturtle()
    hedyfact = turtle.Turtle()
    hedyfact.shape("hedyfact.gif")
    hedyfact.hideturtle()
    hedyfact.penup()
    hedyfact.goto(200, -250)
    hedyfact.showturtle()
    # when the user clicks this turtle, it will go to the correct function
    adafact.onclick(round1correct)
    # if the user clicks the other two turtles, it will go to the incorrect function
    gracefact.onclick(round1incorrect)
    hedyfact.onclick(round1incorrect)

# function to bypass parameters
def gotomatch2():
    match2(0,0)

# this function will appear if the user clicks the correct turtle for round 2 of the game
def round2correct(x, y):
    answerscreen()
    textinfo(0, 80, "CORRECT!", "center", "Times", 60, "bold")
    textinfo(0, 40, "Grace Hopper had two degrees in mathematics. She became", "center", "Times", 22, "normal")
    textinfo(0, 10, "interested in computer science once she realized that programming", "center", "Times", 22, "normal")
    textinfo(0, -20, "involved the usage of numerical code. Thus, she realized that", "center", "Times", 22, "normal")
    textinfo(0, -50, "programming would be accessible if it were in a universal language.", "center", "Times", 22, "normal")
    nextround = turtle.Turtle()
    nextround.shape("next.gif")
    nextround.hideturtle()
    nextround.penup()
    nextround.goto(0, -150)
    nextround.showturtle()
    # when the user clicks this turtle, it will go to the match3 function, round 3 of game
    nextround.onclick(match3)

# this function will appear if the user clicks the wrong turtles in round 2 of the game
def round2incorrect(x, y):
    answerscreen()
    textinfo(0, 30, "INCORRECT!", "center", "Times", 80, "bold")
    textinfo(0, -70, "Try Again.", "center", "Times", 40, "normal")
    # after a certain amount of time, it will go back to the match2 function
    s.ontimer(gotomatch2, 2000)

# this function is what the user sees for round 2 of the matching game
def match2(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 250, "ROUND 2", "center", "Times", 60, "bold")
    gracehopper = turtle.Turtle()
    gracehopper.shape("Gracehopper.gif")
    gracehopper.hideturtle()
    gracehopper.penup()
    gracehopper.goto(-200, 0)
    gracehopper.showturtle()
    gracefact = turtle.Turtle()
    gracefact.shape("gracefact.gif")
    gracefact.hideturtle()
    gracefact.penup()
    gracefact.goto(200, 100)
    gracefact.showturtle()
    hedyfact = turtle.Turtle()
    hedyfact.shape("hedyfact.gif")
    hedyfact.hideturtle()
    hedyfact.penup()
    hedyfact.goto(200, -100)
    hedyfact.showturtle()
    # if the user clicks this turtle, it will go to the correct function
    gracefact.onclick(round2correct)
    # if the user clicks this turtle, it will go to the incorrect function
    hedyfact.onclick(round2incorrect)

# this function will appear when the user clicks the correct turtle in round 3 of the game
def round3correct(x, y):
    answerscreen()
    textinfo(0, 80, "CORRECT!", "center", "Times", 60, "bold")
    textinfo(0, 40, "Hedy was an immigrant, actress, and inventor. She led the development of", "center", "Times", 21, "normal")
    textinfo(0, 10, "Wi-Fi, GPS, and Bluetooth technology systems. Her developments helped with", "center", "Times", 21, "normal")
    textinfo(0, -20, "war efforts by creating new communication systems for guiding torpedoes.", "center", "Times", 21, "normal")
    nextround = turtle.Turtle()
    nextround.shape("next.gif")
    nextround.hideturtle()
    nextround.penup()
    nextround.goto(0, -100)
    nextround.showturtle()
    # when the user clicks this turtle, it will go to the completegame function
    nextround.onclick(completegame)

# this is the function the user will see for round 3 of the game
def match3(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 250, "ROUND 3", "center", "Times", 60, "bold")
    hedylamarr = turtle.Turtle()
    hedylamarr.shape("Hedylamarr.gif")
    hedylamarr.hideturtle()
    hedylamarr.penup()
    hedylamarr.goto(-200, 0)
    hedylamarr.showturtle()
    hedyfact = turtle.Turtle()
    hedyfact.shape("hedyfact.gif")
    hedyfact.hideturtle()
    hedyfact.penup()
    hedyfact.goto(200, 0)
    hedyfact.showturtle()
    # when the user clicks this turtle, it will go to the correct function for round 3
    hedyfact.onclick(round3correct)

# this function is what the user will see after they have completed the matching game 
def completegame(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 200, "Congrats!", "center", "Times", 80, "bold")
    textinfo(0, 0, "You've completed the game!", "center", "Times", 30, "normal")
    textinfo(0, -50, "Let's move on to the next question.", "center", "Times", 30, "normal")
    # after a certain amount of time, it will go to the gotofifthquestion function
    s.ontimer(gotofifthquestion, 3000)

# this function is to bypass parameters
def gotofifthquestion():
    fifthquestion(0, 0)

# this function is what the user sees for the fifth question
def fifthquestion(x, y):
    turtle.clearscreen()
    background()
    textinfo(0, 100, "QUESTION 5", "center", "Times", 50, "bold")
    textinfo(0, 30, "Have you heard about Break Through Tech?", "center", "Times", 25, "normal")
    yesbutton = turtle.Turtle()
    yesbutton.shape("yesbutton.gif")
    yesbutton.hideturtle()
    yesbutton.penup()
    yesbutton.goto(-10, -100)
    yesbutton.showturtle()
    # if the user clicks this turtle, it will go to the yesresponse for question5 function
    yesbutton.onclick(yesreponse_q5)
    nobutton = turtle.Turtle()
    nobutton.shape("nobutton.gif")
    nobutton.hideturtle()
    nobutton.penup()
    nobutton.goto(-10, -250)
    nobutton.showturtle()
    # if the userclicks this turtle, it will go to the noresponse for question5 function
    nobutton.onclick(noreponse_q5)

# this function is what the user will see when they click yes from the question5 function
def yesreponse_q5(x, y):
    answerscreen()
    textinfo(0, 30, "Happy to hear about that!", "center", "Times", 60, "bold")
    textinfo(0, -15, "Their mission is to work with women and non-binary students", "center", "Times", 25, "normal")
    textinfo(0, -50, " through academics and the work industry to complete computing ", "center", "Times", 25, "normal")
    textinfo(0, -90, "degreees and have tech careers. They value prize over privilege", "center", "Times", 25, "normal")
    textinfo(0, -125, "and focus on building a more inclusive tech ecosystem.", "center", "Times",  25, "normal")
    # after a certain amount of time, it will go to the finalquestion function
    s.ontimer(finalquestion, 5000)

# this function will appear when the user clicks no from the question5 function
def noreponse_q5(x, y):
    answerscreen()
    textinfo(0, 60, "That's alright! :D", "center", "Times", 60, "bold")
    textinfo(0, 15, "We can tell you more about Break Through Tech. They focus on", "center", "Times", 25, "normal" )
    textinfo(0, -20, "women and non-binary students to achieve computing degrees", "center", "Times", 25, "normal")
    textinfo(0, -55, "and have tech careers through academics and programs. They offer", "center", "Times", 25, "normal")
    textinfo(0, -90, "Sprinternships, a tuition free 8 week to understand the basics of CS,", "center", "Times", 25, "normal")
    textinfo(0, -125, "Tech in Residence and so much more. More information could be", "center", "Times", 25, "normal")
    textinfo(0, -160, "found here: https://chicago.breakthroughtech.org/programs/", "center", "Times", 25, "normal")
    print("Programs : https://chicago.breakthroughtech.org/programs/")
    # after a certain amount of time, it will go to the finalquestion function
    s.ontimer(finalquestion, 6000)

# this function is what the user will see for the final question of this quiz
def finalquestion():
    turtle.clearscreen()
    background()
    textinfo(0, 250, "Thank you so much! :D", "center", "Times", 50, "bold")
    textinfo(0, 150, "If you found the information in the quiz", "center", "Times", 25, "normal")
    textinfo(0, 100, "interesting, join Break Through Tech to make a", "center", "Times", 25, "normal")
    textinfo(0, 50, "difference in Computer Science! We need more", "center", "Times", 25, "normal")
    textinfo(0, 0, "representation to have an inclusive environment", "center", "Times", 25, "normal")
    textinfo(0, -50, "in tech! We would apperciate having you with us.", "center", "Times", 25, "normal")
    textinfo(0, -100, "To join, please follow the link:", "center", "Times", 25, "normal")
    textinfo(0, -150, "https://chicago.breakthroughtech.org/get-involved/membership/", "center", "Times", 20, "normal")
    # the print statement allows users to actually click the link and go to it
    print("https://chicago.breakthroughtech.org/get-involved/membership/")

# MAIN CODE
# calls the welcomescreen() function and returns the name from the input so it can be used in other functions
name = welcomescreen()

# just here just in case
s.listen()
s.mainloop()