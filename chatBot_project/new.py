# Random implemented as a pseudo-random number generator
import random 

# JSON file to work with JSON data
import json 
import pickle
import numpy as np

# TensorFlow is a multi-dimensional array of elements
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))  # Fixed: Should be 'words', not 'classes'

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    
    for word in words:
        bag.append(1 if word in wordPatterns else 0)  # Fixed: Proper if-else structure
    
    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training, dtype=np.float32)
# Fixed: Ensure compatibility with NumPy array

trainX = training[:, :len(words)]  # Fixed: Correct slicing
trainY = training[:, len(words):]

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))  # Fixed: Typo in 'tf.keras.layers'
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation="softmax"))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)  # Fixed: Typo in 'optimizers'

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)  # Fixed: Typo in 'batch_size'

model.save('CHATBOT_simplilearmodel.h5', hist)
print("Executed")

