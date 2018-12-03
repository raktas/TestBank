from time import sleep
import os
import json

#-------------------------------------------------------------------------------------------------
# Credits: I would like to give credit to Mike Dane as I build this app from one of his videos. 
# Original Author: Mike Dane - Youtube Channel for training videos 
# Link: https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=190s
#-------------------------------------------------------------------------------------------------


def intro():
    print("\n\n")
    print("Welcome to Computer Networking Quiz!\n\n")
    sleep(2)
    print("Let's Start! \n")

def test_select():
    chapter = input('Enter Chapter: ')
    filename_bank = 'Chapter_'+str(chapter)+'_questions.json'
    with open(filename_bank) as f:
        question_key = json.load(f)
    return question_key

def clear():
        if os.name == 'nt':
            os.system("cls") # clears the screen must use import os
        else:
            os.system('clear')
        sleep(1)
    

def run_MC_test(question_key):
    score = 0
    question_count = 0
    for question in question_key['t/f']:
        question_count += 1
        clear()
        print(question['question'])
        for option in question:
            if str(option[:3]) == 'opt':
                print(question[option])
        user_answer = input('\n :: ')
        clear()
        if user_answer == question['answer'] or user_answer == question['answer'].lower():
            score += 1
            print("\nThe Answer: " + question['answer'] + " Correct\n\n-----------------------------------------------------\n\n")
            sleep(3)
        else:
            print("\nThe Answer: " + question['answer'] + " Incorrect\n\n-----------------------------------------------------\n\n")
            sleep(3)
    for question in question_key['mc']:
        question_count += 1
        clear()
        print(question['question'])
        for option in question:
            if str(option[:3]) == 'opt':
                print(question[option])
        user_answer = input('\n :: ')
        clear()
        if user_answer == question['answer'] or user_answer == question['answer'].lower():
            score += 1
            print("\nThe Answer: " + question['answer'] + " Correct\n\n-----------------------------------------------------\n\n")
            sleep(3)
        else:
            print("\nThe Answer: " + question['answer'] + " Incorrect\n\n-----------------------------------------------------\n\n")
            sleep(3)
    
    print("\n\n\n\n")
    clear()
    print("You got " + str(score) + "/" + str(question_count) + "correct")

def run_vocab_test():
    print('Welcom to the Vocab Section')

intro()
question_key = test_select()
run_MC_test(question_key)
