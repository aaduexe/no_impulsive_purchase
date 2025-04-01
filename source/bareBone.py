import random

# List of decision making question
questions = [
    {
        "question": "Did not having this item cause any inconvenience in the past month?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If your daily life was unaffected, this might not be essential.",
        "category": ["Necessity", "Utility", "Health & Well-being"]
    },
    {
        "question": "Would my daily routine improve significantly if I had this item?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If it wouldn’t make a real difference, reconsider the purchase.",
        "category": ["Necessity", "Utility", "Health & Well-being"]
    },
    {
        "question": "Would I still want this if I had to wait another 30 days?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If the urgency fades, it might have been an impulse desire.",
        "category": ["All"]
    },
    {
        "question": "Does this wish align with my long-term needs or goals?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If it's just a short-term craving, reconsider.",
        "category": ["Necessity", "Utility", "Health & Well-being", "Investment"]
    },
    {
        "question": "Have I thought about this item multiple times in the past 30 days without reminders?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If you only remembered because of this app, it may not be truly needed.",
        "category": ["All"]
    },
    {
        "question": "Would I still buy this if it were slightly more expensive?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If a small price increase would stop you, it might not be that important.",
        "category": ["Necessity", "Utility", "Health & Well-being", "Investment"]
    },
    {
        "question": "Would I regret not buying this if it became unavailable?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If you wouldn’t care, it’s likely not a priority.",
        "category": ["All"]
    },
    {
        "question": "Is this item the best way to achieve what I want?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If there’s a more efficient or cost-effective way, consider it.",
        "category": ["Utility", "Investment"]
    },
    {
        "question": "Would I still want this if I had to remove something I already own to make space for it?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If you wouldn’t sacrifice anything, it may not be essential.",
        "category": ["Necessity", "Utility", "Luxury"]
    },
    {
        "question": "Does this purchase align with my current financial priorities?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If other priorities need your money first, this can wait.",
        "category": ["All"]
    },
    {
        "question": "Will this item add long-term value?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If it’s only for short-term excitement, reconsider.",
        "category": ["Investment", "Utility", "Health & Well-being"]
    },
    {
        "question": "Am I buying this for practical reasons, not just emotional impulse?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If emotions are the main driver, wait before purchasing.",
        "category": ["Luxury", "Entertainment"]
    },
    {
        "question": "Would I still want this if no one else could see or know I bought it?",
        "score": 1,
        "expected_answer": "Yes",
        "note": "If social influence is the main factor, reconsider.",
        "category": ["Luxury", "Entertainment"]
    }
]

def AskSession() -> int:
    """
    Runs the questionnaire by asking a random selection of 5 questions.
    Returns the total score based on the user's answers.
    """

    score = 0
    fv_questions: list[dict] = random.sample(questions, 5)

    for question in fv_questions:
        print(question['question'])
        print('Note:', question['note'])
        print()
        answer = input("Yes or No: ")
        acceptedInput = ['yes', 'no']
        proceed = False

        # Ensure the user provides valid input
        for ans in acceptedInput:
            if answer.lower() == ans:
                proceed = True

        # Check if the answer matches the expected response
        if proceed:
            if answer.lower() == question['expected_answer'].lower():
                score += int(question['score'])
        else:
            print('Unrecognized Input. Quit the terminal. It\'s not handled yet.')
    return score

def Conclusion(score: int) -> str:
    """
    Evaluates the user's purchase decision based on the questionnaire score.
    Returns 'approved' if the score is 4 or above, otherwise 'denied'.
    """
    if score >= 4:
        #print("You should buy ")
        status = 'approved'
    elif score < 4:
        #print("Do you really need it. My calculation says you don't!")
        status = 'denied'
    return status
