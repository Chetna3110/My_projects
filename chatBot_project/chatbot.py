import random
import json
import pickle  # Used for reading the words.pkl file which are pickled Python objects
import numpy as np
import nltk  # Used for natural language processing
import speech_recognition as sr
import pyttsx3
from nltk.stem import WordNetLemmatizer  # Used to lemmatize the words
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

# Load intents and trained model data
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))  # Fixed incorrect filename & open method
classes = pickle.load(open('classes.pkl', 'rb'))  # Fixed incorrect filename & open method

model = load_model("CHATBOT_simplilearmodel.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence,words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
               # print("Bag of words length : ",len(bag))
    return np.array(bag)

# def predict_class(sentence):
#     bow = bag_of_words(sentence)
#     res = model.predict(np.array([bow]))[0]

#     ERROR_THRESHOLD = 0.25
#     results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
#     results.sort(key=lambda x: x[1], reverse=True)
    
#     return_list = []
#     for r in results:
#         return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})  # Fixed dictionary syntax
#     return return_list

def predict_class(sentence, model):
    ints = model.predict(np.array([bag_of_words(sentence, words)]))[0]
    #print("Raw model output:", ints)  

    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(ints) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
   # print("Predicted intent:", return_list) 
    #xprint(f"Intent: {intents[0]['intent']}")

    return return_list


def get_response(intents_list, intents_json):
    list_of_intents = intents_json['intents']  
    tag = intents_list[0]['intent']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('Great! Bot is running!!!!')

while True:
    message = input("You: ")
    ints = predict_class(message,model)
    res = get_response(ints, intents)
    print("Bot:", res)

import random

def get_self_care_tips():
    tips = [
        "Try deep breathing exercises.",
        "Go for a short walk to clear your mind.",
        "Write down your thoughts in a journal.",
        "Listen to your favorite music.",
        "Talk to a friend or loved one.",
        "Drink some water and take a break."
    ]
    return random.choice(tips)

# Modify the response function
def get_response(intents_list, intents_json):
    list_of_intents = intents_json["intents"]
    tag = intents_list[0]["intent"]
    for i in list_of_intents:
        if i["tag"] == tag:
            response = random.choice(i["responses"])
            if tag in ["anxiety", "depression"]:
                response += " Here's something that might help: " + get_self_care_tips()
            return response
response = "I'm sorry you're feeling this way. What would help you right now?\n"
response += "1️⃣ Talking about it\n2️⃣ A relaxing exercise\n3️⃣ A motivational quote"
print(response)
choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print("Tell me what's on your mind. I'm here to listen. 🧡")
elif choice == "2":
    print("Try this: Close your eyes and take 3 deep breaths. 🌬️")
elif choice == "3":
    print("“You have power over your mind – not outside events. Realize this, and you will find strength.” – Marcus Aurelius 💪")



recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return "Sorry, I didn't catch that."

user_input = get_audio()
speak(f"You said: {user_input}")


