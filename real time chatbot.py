#program to create simple chatbot 

import datetime
import time

name=input("welcome  ....  enter your name ")
now = datetime.datetime.now().hour

if 5<= now <= 11:
    print("GOOD MORNING ",name)
elif 11<= now <= 17 :
    print("GOOD AFTERNOON ",name)
elif 17<= now <= 20:
    print("GOOD EVENING ",name)
else :
    print("GOOD NIGHT ",name)





print("hello ! welcome to the study buddy chatbot  ")
print("you can ask basic question to me , type 'bye' to exit the bot  " )

# chatbot memory creation ! dictionary of responses ! 

responses= {
    "hello" : "hi, welcome . how can i help you ",
    "how are you": "i am very fine . thank you for asking ",
    "who are you": "i am smart AI chatbot ",
    "motivate me": "keep going . every bug of your project makes you better ",
    "happy": "great to hear that ",
    "what are functions ": "functions are group of statements which are used to perform specific task "

}

#creating method or functrion for reply of chatbot


def responseOfBot(userQuestions):
    userQuestions= userQuestions.lower()
    for eachkey in responses:
        if eachkey in userInput:
            return responses[eachkey]
    return "I am AI chatbot, I still need to learn, I will learn it soon "


# take user input 

while True:
    userInput= input("pls ask your questions : ")
    reply= responseOfBot(userInput)
    print("bot responses : ", reply)

    if "bye" in userInput.lower():
        print("thanks for using chatbot ")
        break