import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language.",
    "Practice makes perfect.",
    "Coding is fun and rewarding.",
    # Add more sentences as needed
]

def get_random_sentence():
    return random.choice(sentences)
import time

def test_typing_speed(sentence):
    print("Type the following sentence:")
    print(sentence)
    input("Press Enter when you are ready to start typing.")
    
    start_time = time.time()
    user_input = input("Type the sentence: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_per_minute = len(sentence.split()) / (elapsed_time / 60)
    
    return elapsed_time, words_per_minute

sentence = get_random_sentence()
elapsed_time, words_per_minute = test_typing_speed(sentence)

print(f"\nElapsed time: {elapsed_time:.2f} seconds")
print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    