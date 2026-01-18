#Hangman
import random
art = {0:(" ",
          " ",
          " "),
       1: (" O ",
          " ",
          " "),
       2: (" O ",
          " | ",
          "   "),
       3: (" O ",
          "/| ",
          "   "),
       4: (" O ",
          "/|\\",
          " "),
       5: (" O ",
          "/|\\ ",
          "/  "),
       6: (" O ",
          "/|\\ ",
          "/ \\ ")}

def display_man(wrong_attempts):
    for i in art[wrong_attempts]:
        print(i)


word_bank = ['Rizz','Keys','Rocket','Thrust','Flight','electricity', 'donkey',
 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language',
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus',
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower',
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'wind',
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 'absolute',
 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 'cinema',
 'hardware', 'xerox', 'transistor', 'computer']

word = random.choice(word_bank).lower()
guessed_word = len(word) * ['_']
wrong_attempts = 0
attempts = 6
while wrong_attempts < attempts:
    display_man(wrong_attempts)
    print("".join(guessed_word))
    guess = input("Enter a letter: ")
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                guessed_word[i] = guess
        print("Great guess!")
    else:
       wrong_attempts += 1
       print("Wrong guess")
    if '_' not in guessed_word:
        print("Congrats you got the word!")
        break

if wrong_attempts == attempts and '_' in guessed_word:
    display_man(wrong_attempts=6)
    print("Wrong guesses! the word was " + word)