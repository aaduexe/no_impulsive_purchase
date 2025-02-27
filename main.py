from oldScript import questions
import random

item = input("What you want to buy?: ")
socreVisible = False

print("Answer these 5 question before you buy " + item)

def AskSession():
    score = 0
    selectedQuestions = random.sample(questions,5)
    for question in selectedQuestions:
        print(question)
        answer = input("Yes or No: ")
        if answer.lower() == "yes":
            score += 1
        elif answer.lower() == "no":
            score -= 1
        else:
            print("Incorrect input, no affect on score. This isn't handled yet.")
    return score

def Conclusion(score):
    if score >= 4:
        print("You should buy " + item)
    elif score < 4:
        print("Do you really need " + item + ". My calculation says you don't!")

sc_ore = AskSession()
Conclusion(sc_ore)