import json
import random

def __main__():
    intention = json.loads(open("intent.json").read())
    done = False
    while not done:
        message = input(">>> ")
        if message in ["exit", "stop"]: 
            print("Program is closing...byeeeeeeee")
            done = True
        else:
            [print(random.choice(value['responses']) + ' [' + value['tag'] + ']') if message in value['patterns'] else '' for value in intention['intents']]

if __name__ == "__main__":
    __main__()