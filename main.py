print()
print()
print("There has been a recent disappearance of a student on the morning of the first day of high school.")
print()
print("The police cannot find the kidnapper so the user decides to take matters into their own hands.")
print()
print()
print("HELLO WELCOME TO HUNT THE KIDNAPPER")
print()
print("A GAME WHERE YOU WILL BE TASKED TO CATCH YOUR CLASSMATES KIDNAPPER")
print()
print("THE SUSPECTS INCLUDE Mrs Smith, Mr. Liu, Mrs. Kalen, Ms. Garcia, and Mr. Tom ")
print()
print("UPON COMPLETING UNIQUE CHALLENGES AT EACH LEVEL YOU WILL BE GIVEN A CLUE")
print()
print("USE THE CLUES YOUVE EARNED TO CATCH THE KIDNAPPER")
print()
print("BEWARE: THERE IS A CHANCE TO MISS A CLUE IF YOU DO NOT COMPLETE THE LEVEL CORRECTLY")
print()
print()
userName = input("Enter your name official Jr. Detective: ")
print()
print()
print()
print()
print("Now that its official you must begin you investigation at the libaray, where you last saw the victim")
import random
kidnapper = random.randint(1,5)
print()
print()
#Level 1 
print("******* level 1 *******")
print()
print("-----------------------------------------------")
print()
print("Welcome to the library, you should start by asking the librarian Mrs. Smith for help")
print()
print("She has offered a ROLL OF THE DIE for her help")
print()
print("Rules are simple by pressing enter you will roll a pair of dice against Mrs. Smith")
print()
print("If you roll higher than her you will recieve her clue")
print()
print("If she beats you, you will get to reroll until you do revealing her clue")
print()
input("Press enter to roll the die and begin your Investigation")
import random as r
cust1 = r.randint(2,12)
cust2 = r.randint(2,12)
while cust1 < cust2:
    print()
    print("You rolled:", cust1)
    print()
    print("Mrs. Smith rolled: ", cust2)
    print()
    print("O NO! You lost, try again!")
    print()
    input("Press enter to reroll")
    if cust2 > cust1:
        print()
        print("You rolled: ",cust1)
        print()
        print("Mrs. Smith rolled:", cust2)
        print()
        print("O NO! You lost, try again!")
        input("Press enter to reroll")
    elif cust2 == cust1:
        print()
        print("You rolled: ",cust1)
        print()
        print("Mrs. Smith rolled:", cust2)
        print()
        print("Looks like it was a tie")
        input("Press enter to reroll")
    cust1 = r.randint(2,12) 
    cust2 = r.randint(2,12)  
print()
print("Congrtatulations you rolled:", cust1)
print()
print("Mrs. Smith Rolled:", cust2)
print()
print("-----------------------------------------------")
print()
print ("CONGRATS JR DETECTIVE ")
print()
if kidnapper == 1:
    print("They were grading tests all morning.")
else: 
    print("The alibi of Mrs. Smith was late due to dropping off her kids at school.")
    print()
    print("HERE IS WHAT I REMEMBER: THE VICTIM WAS SEEN SPEAKING WITH MR. LIU THE THEATER TEACHER")
#Level 2 
print("******* LEVEL 2 *******")
print()
print("-----------------------------------------------")
print("\nCongratulations on passing the first level, and welcome to level 2.")
print("\nIn this level, Mr. Liu has prepared 3 multiple choice questions for you.")
print("\nAnswer them all correctly, and you will receive the alibi of Mr. Liu that morning")
print("\nYou will have 3 attempts at each question.")
print("\nInput either A, B, C, or D as your response.")
print("\n")
print("\nGood luck")
print("\n")

level2Counter = 1 
class Question:
    def __init__(self):
        self.text = ""
        self.answer = ""
    def setText(self, text):
        self.text = text
    def setAnswer(self, answer):
        self.answer = answer.lower() 
    def checkAnswer(self, response):
        # print(self.answer == response.lower())
        print("")
        return self.answer == response.lower()
        for i in response:
            i = i.strip(',:;."?()')
            i = i.lower()
            i = i.replace(" ", "")
            i = i.strip() 
    def display(self):
        print(self.text)     
class MC(Question):
    def __init__(self):
        self.choices = []
    def addChoice(self, choice):
        self.choices.append(choice)
    def display(self):
        print(self.text)
        for i in range(len(self.choices)):
            print(self.choices[i])            
questionList = [] 
mc1 = MC()
#print("Your score is: ",count)
mc1.setText("Question 1: What is the English translation of this Tagalog sentence? 'Pakibigyan mo ako ng magandang marka?'")
mc1.setAnswer("B") 

mc1.addChoice("A) X marks the spot")
mc1.addChoice("B) Please give me a good grade")
mc1.addChoice("C) I wrote on their face with a marker")
mc1.addChoice("D) The cone marks where to park your car")

questionList.append(mc1)

mc2 = MC()
#print("Your score is: ",count)
mc2.setText("Question 2: What is the name of the pyramid at CSULB?")
mc2.setAnswer("D")

mc2.addChoice("A) Toph Topia")
mc2.addChoice("B) Sokka To-ya")
mc2.addChoice("C) Aang-Bang")
mc2.addChoice("D) Walter Pyramid")
questionList.append(mc2)

mc3 = MC()
#print("Your score is: ",count)
mc3.setText("Question 3: What series is Katniss Everdeen from?")
mc3.setAnswer("B")

mc3.addChoice("A) Divergent")
mc3.addChoice("B) The Hunger Games")
mc3.addChoice("C) Harry Potter")
mc3.addChoice("D) The Maze Runner")
questionList.append(mc3)

mc4 = MC()
#print("Your score is: ",count)
mc4.setText("Question 1: What does Mr. Liu teach?")

mc4.setAnswer("A") 
mc4.addChoice("A) Theater")
mc4.addChoice("B) Math")
mc4.addChoice("C) Social Studies")
mc4.addChoice("D) Science")
questionList.append(mc4)

mc5 = MC()
#print("Your score is: ",count)
mc5.setText("Question 2: What year was the world supposed to end?")
mc5.setAnswer("C") 

mc5.addChoice("A) 2020")
mc5.addChoice("B) 2022")
mc5.addChoice("C) 2012")
mc5.addChoice("D) 2016")
questionList.append(mc5)

mc6 = MC()
#print("Your score is: ",count)
mc6.setText("Question 1: What does Professor Conlon teach?")
mc6.setAnswer("D") 
#mc6.display()
mc6.addChoice("A) Business Law")
mc6.addChoice("B) Business Stats")
mc6.addChoice("C) International Business")
mc6.addChoice("D) Business Programming Application")
questionList.append(mc6)

questions = 3
count = 0
attempts = 0
finalResponse =""
while questions > 0:
    finalResponse =""
    i=""
    question = random.choice(questionList)
    question.display()
    questionCount = 0
    response = input("Please enter a letter: ")
    for i in response:
        i = i.strip(',:;."?!()')
        i = i.lower()
        i = i.replace(" ", "")
        i = i.strip() 
        i = i.strip("efghijklmnopqrstuvwxyz")
        finalResponse += i
    question.checkAnswer(finalResponse) 
    attempts += 1
    check = question.checkAnswer(finalResponse)
   
    while (not question.checkAnswer(finalResponse) and questionCount < 3 and attempts < 3): 
        questionCount+=1
        finalResponse =""
        response =input("\nYour answer is incorrect \nYou have "+ str(3 - questionCount) +" trials left\nPlease enter a letter again: ")
        for i in response:
            i = i.strip(',:;."?!()')
            i = i.lower()
            i = i.replace(" ", "")
            i = i.strip() 
            finalResponse += i
        check = question.checkAnswer(finalResponse)
        attempts += 1
       
        if (check == True):
          print("\nYour answer is correct ")
          print()
          
    if (check == True):
         print("\nYour answer is correct ")
         print()
                      
    if(questionCount < 3):
        count+=1
    questions-=1
if(count==3):
    print("Congrats, you answered all 3 questions correctly. Your score is: ",count)
    print()
    if kidnapper == 2:
        print("He was grading tests all morning.")
        print()
    else: 
        print("The alibi of Mr. Liu was that he was in his office all morning with his wife.")
        print()
    level2Counter -= 1
else:
    print("Sorry! You did not answer all 3 questions correct. You will not get the alibi.")
    print()
    print()
    

#Level 3 
print("******* LEVEL 3 *******")
print("-----------------------------------------------")
print("\n")
print("You walk and find Mrs.Kalen, who seems to be getting ready for class. You head over to her desk and ask if you could ask her a quick question.")
print("\n")
print("Beat Mrs.Kalen in a game of Tic Tac Toe to get the next clue.")
print("\n")

level3Counter = 1
import random as r 

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

startGame = True
winner = None
player = "X"
gameTries = 0
opponite = "O"
alibi = "Mrs. Kalen was welcoming the student in the courtyard"


def gameTitle():
    print("Defeat Mrs. Kalen!")
            
def displayBoard():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")
        
def playGame():
    
        global level3Counter
        displayBoard()
        
        while startGame:
            
            playerTurn(player)
            
            checkGame()
            
            computerTurn(opponite)    
            
            checkGame()
            
            if winner == "X" and gameTries == 0:
                print("You win!")
                print("\n")
                if kidnapper == 3:
                    print("Mrs.Kalen's was grading test" )
                else:
                    print("Mrs.Kalen's alibi - ", alibi)
                print("\n")
                print("Mrs.Kalen also reveals that she remembers seeing the victim walking with Ms. Garcia before the victim entered the classroom.")
                print("\n")
                print("Good luck in the next level!")
                level3Counter -= 1
                return False

            elif winner == "X" and gameTries == 1:
                print("You were suppose to win on the first try!")
                print("You did not get Mrs.Kalen's alibi.")
                return False
            elif winner == "X" and gameTries > 1:
                print("You were supposed to win on the first try!")
                print("It took %d tries" % gameTries)
                print("NO ALIBI FOR YOU :(")
                return False
            elif winner == "O":
                print("Mrs.Kalen wins!")
                playAgain()
                print("\n")
                return False
            
def playerTurn(player):
    
    print(player + "'s turn.")
    print("\n")
    
    try:
        playerPosition = int(input("Choose a number, 1 - 9: "))
        playerPosition = playerPosition - 1
        if board[playerPosition] == "-":
            board[playerPosition] = player
            displayBoard()
            return player
        elif board[playerPosition] == "O":
            print("This spot is taken. You lose your turn.")
            print("\n")
    except ValueError:
        print("This is not a number! You lose your turn.")
        print("\n")
    except IndexError:
        print("This is not a number between 1 - 9! You lose your turn.")
        print("\n")
#computer turn
def computerTurn(opponite): 
    #computer takes middle if open
    if board[4] == "-":
        board[4] = opponite
        displayBoard()
        return opponite
    #computer blocks win
    #blocks row win
    elif board[0] == "X" and board[1] == "X" and board[2] == "-":
        board[2] = opponite
        displayBoard()
    elif board[3] == "X" and board[4] == "X" and board[5] == "-":
        board[5] = opponite
        displayBoard()
    elif board[6] == "X" and board[7] == "X" and board[8] == "-":
        board[8] = opponite
        displayBoard()
    #blocks column win
    elif board[0] == "X" and board[3] == "X" and board[6] == "-":
        board[6] = opponite
        displayBoard()
    elif board[1] == "X" and board[4] == "X" and board[7] == "-":
        board[7] = opponite
        displayBoard()
    elif board[2] == "X" and board[5] == "X" and board[8] == "-":
        board[8] = opponite
        displayBoard()
    #blocks diagonal win
    elif board[0] == "X" and board[4] == "X" and board[8] == "-":
        board[8] = opponite
        displayBoard()
    elif board[2] == "X" and board[4] == "X" and board[6] == "-":
        board[6] = opponite
        displayBoard()
    else: #random spot
        while True:
            comPosition = r.randint(0,8)
            if board[comPosition] == "-":
                board[comPosition] = opponite
                displayBoard()
                break
#check if game over
def checkGame():
    checkWin()
    checkTie()
    
#checks for win    
def checkWin():
    global winner
    if threeInRow() or threeInColumn() or threeInDiagonal():
        return False
    
#checks for tie       
def checkTie():
    global startGame
    if "-" not in board:
        print("Tie!")
        playAgain()
        return True
    else:
        return False         
#checks row for win
def threeInRow():
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
#checks column for win
def threeInColumn():
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
#checks diagonal for win
def threeInDiagonal():
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif  board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True  
def resetGame():
    global winner
    global board
    winner = None
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    
#play again if you lose
def playAgain():
    global gameTries
    yesOrNo = input("Would you like to play again? (Y/N): ").upper()
    if yesOrNo == "Y":
        gameTries+=1
        resetGame()
        playGame()
    elif yesOrNo == "N":
        print("Thanks for playing. GG! NT! ")
        endGame()
#ends game                
def endGame():
    global startGame
    startGame = False 
playGame()
print("-----------------------------------------------")
#Level 4 
print("----------------------")
print(" Welcome to level 4 ")
print("----------------------")
print()

level4Counter = 1
import time

validAnswers = {"kidnapper", "KIDNAPPER"}
wordPuzzle = '''
T	Y	K	W	U	X	I	Y	Y	T	Q	N	Q
Q	W	B	R	B	E	N	Y	C	V	F	Z	M
A	C	N	O	O	E	P	R	F	Q	V	Y	U
R	E	P	P	A	N	D	I	K	G	W	J	K
E	U	Q	M	K	D	X	G	H	O	M	Q	X
Y	W	S	H	A	V	L	Z	A	G	H	V	I
K	W	N	D	J	P	E	Z	Y	Z	R	D	I
U	A	I	G	T	X	U	K	W	C	Y	M	J
X	W	S	B	B	F	N	M	M	I	M	E	T
Q	B	Q	W	K	V	X	Y	C	N	Z	J	B
E	R	T	X	J	H	V	Q	I	E	I	D	Q
H	F	B	D	T	Y	V	O	C	X	Y	X	Q
N	R	V	R	X	F	Q	C	N	Y	N	S	A
'''


def main():

  print("You walk into the teacher’s lounge to find Ms. Garcia reading the daily newspaper. You walk up to her and ask her what she has been doing all morning.")
  print()
  print("She ignores you as she does the daily word search puzzle in the newspaper.")
  print("She has not been able to find all the words in the grid as her eye sight is not that good.")
  print("She states that if you can finish her word search, she will give you her alibi!")
  print()
  print("You have 2 minutes to complete find the missing word")
  print()
  print("you can get a hint in the last 40 seconds!")
  print()
  print("Hint: The hidden word is part of the story line")
  print()

  userinput = input("Are you ready? yes/no: ")
  if userinput == "yes":
    print("Good luck finding the word in the puzzle!")
    print(wordPuzzle)
    start_time = time.time()
    elapsed = 0

    while elapsed < 120:
      elapsed -= 1
      time.sleep(0.1)

      elapsed = time.time() - start_time
      if elapsed > 80:
        print("Hint: Your word starts with a letter K and is in the forth line.")

      usersGuess = input("Insert your guess: ")
      print()
      elapsed = time.time() - start_time
      # print(int(elapsed))
      # usersGuess = input("Insert your guess: ")
      # elapsed = time.time() - start_time
      # print(elapsed)
      
      if usersGuess in validAnswers:
        global level4Counter
        print("Correct!")
        level4Counter -= 1
        if kidnapper == 4:
            print("He was grading tests all morning.")
            print()
        else: 
            print("she was having coffee in teachers lounge")
            print("Thank you for playing this game and good luck in the next level")
        break
      else:
        print("Sorry! This is the wrong answer, please try again")
        elapsed = time.time() - start_time
        print("Time: %d seconds past" % int(elapsed))

      elapsed = time.time() - start_time
      if elapsed > 120:
        print("Sorry your time is up, You took: %d seconds " % int(elapsed))
        break  
  elif userinput == "no":
    print("Goodbye! Hope you will come back")
  else:
    print("wrong input answer with yes or no!")
    userinput = input("Are you ready? yes/no: ")
main()
print("-----------------------------------------------")
print()
print()




#Level 5
print("******* LEVEL 5 *******")
print()
print("Time to review the last suspect on your list: Mr. Tom, the 10th grade history teacher.")
print(" ")
print("Mr. Tom’s history room is full of books about ancient civilization. As you walk around the classroom to find a clue, you see a piece of paper under the desk. You cannot understand the text as they do not make any words. You search the bookcase for a hyroglifics book to unscramble the words.")
print(" ")
import random
wordBank = ['private investigator', 'he is not the kidnapper', 'tom is innocent', 'hunt the kidnapper']
answer = random.choice(wordBank)
level5Counter = 1
#answer = "privateinvestigator"
toDecypher = ""
toCheck = ""
letterCodes = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y',
    'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's',
    'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k',
    's': 'l', 't': 'z', 'u': 'x', 'v':'c', 'w': 'v', 'x': 'b', 
    'y': 'n', 'z':'m'
    }

#length is the length of however long the answer is 
for i in range(0, len(answer)):
#if the letter is in the converison code dictionary, it will add the corresponding values
    if answer[i] in letterCodes.keys():
        toDecypher += letterCodes[answer[i]]
    #this will add the spaces from the answer to the encrypted code
    else:
    	toDecypher += answer[i]
def key():
    print("_____________________________________________")
    print("Here Are The Keys. Goodluck!")
    print("a : q", "|", "b : w",  "|", "c : e",  "|","d : r", "|", "e : t", "|", "f : y")
    print("g : u", "|", "h : i","|", "i : o","|", "j : p","|", "k : a","|", "l : s")
    print("m : d", "|","n : f","|", "o : g","|", "p : h","|", "q : j","|", "r : k")
    print( "s : l","|", "t : z","|", "u : x","|", "v : c","|", "w : v","|", "x : b" )
    print("y : n", "|", "z : m", "|")
    print("_____________________________________________")
while True:
    newAnswer=""
    toCheck = ""
    # Printing the message to decypher and its code
    key()
    print(" ")
    print("Solve this: ", toDecypher)
    for x in answer:
        x = x.replace(" ", "")
        newAnswer += x
    guess = input("Enter your guess: ")
    #this is remove any punctuation marks, spacing and change any uppercase letters to lowercase
    for i in guess:
        i = i.strip(',:;.!"?()')
        i = i.lower()
        i = i.replace(" ", "")
        i = i.strip() 
        toCheck += i
    
    if toCheck != newAnswer:
        print(" ")
        print("You did not successfully decypher the code. Please try again.")
        level5Counter -= 1
    if toCheck == newAnswer:
        print(" ")
        print("Congratulations you decoded the word!")
        print(" ")
        if level5Counter == 1:
            if kidnapper == 5:
                print("Was grading test all morning")
            else:
                print("Right after you found the clue, a student comes in the classroom. You ask them if they know what Mr. Tom was going all morning. ")
                print(" ")
                print("They replied that he was with them decorating this classroom all morning.")
                print("")
                print("With that, you have reviewed all of your suspects.")
        if level5Counter != 1:
            print("You realize you were going to be late to to your next class.")
            print(" ")
            print("You did not have enough time to find his alibi.")
        break
print("-----------------------------------------------")

#Guess the kidnapper 
print()
print("It is the end of the first day of school and you have finished checking everyone on your suspect list. You sit down by the benches to review your clues.")
print()
print("Remember the alibis youve earned at every level ")
print()
result= int(input("Guess the kidnapper based off the level you got it from (type 1-5): "))
if result == kidnapper:
    print()
    print("CONGRATULATION JR DETECTIVE %s YOU HAVE TRACKED DOWN YOUR SUSPECT AND WON THE GAME" % userName)
    print()
else:
    print()
    print("OOO NOOOO YOU'RE INCORRECT! PLEASE TRY AGAIN FROM BEGINNING")