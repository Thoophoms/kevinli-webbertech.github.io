import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

## 2: Prepare Your Textual Playground

data = [
    "Warren Edward Buffett (/ˈbʌfɪt/ BUF-it; born August 30, 1930)[2] is an American businessman, investor, and philanthropist who currently serves as the chairman and CEO of Berkshire Hathaway."
]

## 3: Tokenize and Sequence
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in data:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_length = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

## 4: Building the LLM Architecture

model = Sequential()
model.add(Embedding(total_words, 100,input_length=max_sequence_length-1))
model.add(LSTM(150, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))

## 5: Training the LLM

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

X, y = input_sequences[:, :-1], input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

model.fit(X, y, epochs=200, verbose=1)

# 6: Unleashing the Creativity
seed_text = " Your starting data goes here: "
next_words = 15

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
    predicted_probabilities = model.predict(token_list, verbose=0)[0]
    predicted_index = np.argmax(predicted_probabilities)
    output_word = tokenizer.index_word[predicted_index]
    seed_text += " " + output_word

print(seed_text)