#SIMPLE GUESSING GAME WHERE USER NEEDS TO SELECT THE RIGHT ANSWER
#USING CLASSES / IMPORT / FUNCTIONS
from Question import Question
questions_prompts = [
    "Qual a capital de Santa Catarina?\n (a)Florianópolis\n (b)Joinville\n (c)Blumenau\n",
    "Qual a capital de Santa Catarina?\n (a)Florianópolis\n (b)Joinville\n (c)Blumenau\n",
    "Qual a capital de Santa Catarina?\n (a)Florianópolis\n (b)Joinville\n (c)Blumenau\n",
    "Qual a capital de Santa Catarina?\n (a)Florianópolis\n (b)Joinville\n (c)Blumenau\n",
    "Qual a capital de Santa Catarina?\n (a)Florianópolis\n (b)Joinville\n (c)Blumenau\n"
]

questions = [
        Question(questions_prompts[0], "a"),
        Question(questions_prompts[1], "a"),
        Question(questions_prompts[2], "a"),
        Question(questions_prompts[3], "a"),
        Question(questions_prompts[4], "a"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " corret")

run_test(questions)