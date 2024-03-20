# magic_8_ball
import random


def main():
    m8file = open('m8_answers.txt', 'r')
    question = input("Ask me and yes/no answer: ")
    answer = get_m8_answer(m8file)
    print(f"Here is your answer: {answer}")
    m8file.close()


def get_m8_answer(m8file):
    answer_num = random.randint(1, 20)
    linenum = 1
    for answer in m8file:
        if linenum == answer_num:
            return answer
        linenum += 1


main()
