from Question import Question
import random

randomList = []
for i in range(0,10):
    n = random.randint(2,9)
    randomList.append(n)

question_prompts = [
    f'{randomList[0]} x {randomList[1]}? ',
    f'{randomList[2]} x {randomList[3]}? ',
    f'{randomList[4]} x {randomList[5]}? ',
    f'{randomList[6]} x {randomList[7]}? ',
    f'{randomList[8]} x {randomList[9]}? ',
]

result1 = randomList[0] * randomList[1]
result2 = randomList[2] * randomList[3]
result3 = randomList[4] * randomList[5]
result4 = randomList[6] * randomList[7]
result5 = randomList[8] * randomList[9]

questions = [
    Question(question_prompts[0], f'{result1}'),
    Question(question_prompts[1], f'{result2}'),
    Question(question_prompts[2], f'{result3}'),
    Question(question_prompts[3], f'{result4}'),
    Question(question_prompts[4], f'{result5}'),
]

def run_test(questions):
    score = 0
    scoreStep = 10
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += scoreStep
            print('Відповідь вірна!')
        else:
            print('Відповідь не вірна!')
    print(f'Вітаю. В тебе {str(score)} очок з {str(len(questions*scoreStep))} можливих.')

run_test(questions)
