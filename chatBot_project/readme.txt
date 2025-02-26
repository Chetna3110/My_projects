🛠️ Technologies Used
Programming Language: Python
Framework/Libraries: TensorFlow, NLTK, NumPy, Flask (if applicable)
Platform: Command Line Interface (CLI)
Development Environment: VS Code

📂 Project Structure
bash
chatbot/
│── Include/                     # Additional dependencies
│── Lib/                         # External libraries
│── Scripts/                      # Main scripts
│── chatbot_model.h5              # Trained model
│── chatbot.py                    # Main chatbot script
│── classes.pkl                   # Encoded class labels
│── intents.json                   # Intents dataset
│── pyvenv.cfg                     # Virtual environment config
│── train.py                       # Training script
│── words.pkl                      # Tokenized words
│── README.md                      # Documentation


🚀 How It Works
User Input Processing:

The chatbot takes user input from the CLI.
Tokenizes and converts input into a numerical format using bag_of_words().
Intent Prediction:

The processed input is passed to a trained deep learning model (chatbot_model.h5).
The model predicts the intent category using probability scores.
Response Generation:

The chatbot selects the best response based on the predicted intent using intents.json.
The response is displayed in the CLI.
