import random

questions = [
    "Do I need this item?",
    "Is this item within my budget?",
    "Have I researched alternative options?",
    "Will this item improve my daily life?",
    "Can I afford this item without financial strain?",
    "Is this the best time to buy this item?",
    "Do I have space for this item at home?",
    "Have I read reviews or ratings about this item?",
    "Is this item a priority over other planned purchases?",
    "Will I use this item frequently?",
    "Does this item match my current style or preferences?",
    "Is this item available at a discount or on sale?",
    "Have I checked the return policy for this item?",
    "Is this item environmentally friendly or sustainable?",
    "Have I consulted with someone else about this purchase?",
    "Is this item durable and of good quality?",
    "Does this item have a good warranty or guarantee?",
    "Will this item enhance my productivity or efficiency?",
    "Is this item compatible with what I already own?",
    "Do I have any unresolved doubts about purchasing this item?"
] # List of normal question, needs to update with meaningful one which are actually practical to make decision.

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
        #print("You should buy ")
        status = 'approved'
    elif score < 4:
        #print("Do you really need it. My calculation says you don't!")
        status = 'denied'
    return status
