import time
import random

operators = ["+", "-", "*", "/"]
random.seed()
gameDuration = None
gameDifficulty = None
needsHeading = False

fileFirstStr = "Duration:\tDifficulty:\tScore:\n"

with open("math_practice_scores.txt", "a") as f:
    True

with open("math_practice_scores.txt", "r") as f:
    if not f.readline() == fileFirstStr:
        needsHeading = True

if needsHeading:
    with open("math_practice_scores.txt", "a") as f:
        f.write(fileFirstStr)

def newGame():
    global gameDuration
    global gameDifficulty
    if(gameDuration == None or gameDifficulty == None):
        print("Welcome!")
        gameDurationStr = input("Enter game duration in seconds: ")
        gameDifficultyStr = input("Enter game difficulty: ")
        try:
            gameDuration = int(gameDurationStr)
            gameDifficulty = int(gameDifficultyStr)
            print("Game duration: ", gameDuration, " seconds.")
            print("Game difficulty: ", gameDifficulty)
        except:
            print("Wrong game mode selected.")
            return
    print("Ready...")
    time.sleep(1.5)
    score = 0
    startTime = time.time()
    while(time.time()-startTime < gameDuration):
        operator = operators[random.randint(0, len(operators))-1]
        firstNumLen = random.randint(1, gameDifficulty)
        secondNumLen = random.randint(1, gameDifficulty)
        firstNum = random.randint(pow(10, firstNumLen-1), pow(10, firstNumLen) - 1)
        secondNum = random.randint(pow(10, secondNumLen-1), pow(10, secondNumLen) - 1)

        answer = None
        if operator == "+":
            answer = firstNum + secondNum
        elif operator == "-":
            answer = firstNum - secondNum
        elif operator == "*":
            answer = firstNum*secondNum
        else: answer = firstNum/secondNum

        print(firstNum, operator, secondNum, "=")
        roundStartTime = time.time()
        playerAnswerStr = input()
        roundTime = time.time()-roundStartTime
        answer = abs(answer)
        try:
            playerAnswer = abs(float(playerAnswerStr))
            correctness = 100*pow(2.718281828459, -4*playerAnswer/answer)*pow(2.718281828459*playerAnswer/answer, 4)
            score += pow(correctness, 1.2) / pow(roundTime, 0.8)
            print("Correct answer: ", int(answer*10000)/10000.0, " Correctness: ", int(correctness*100)/100.0, "% Time: ", int(roundTime*100)/100.0, " Score: ", int(score*100)/100.0)
            print()
        except:
            print("Answer not a number.")

    print("Game ended")
    print("Score: ", score)
    filePrintStr = str(gameDuration) + "\t" + str(gameDifficulty) + "\t" + str(score) + "\n"
    with open("math_practice_scores.txt", "a") as f:
        f.write(filePrintStr)

    choice = input("Press [Enter] to play again with same settings, press any key to end session")
    if choice == "":
        firstGame = False
        return gameDuration
    else: return None

while not newGame() == None:
    True

print("Thanks for playing!")