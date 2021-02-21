import random as rnd

class HangmanGame():
    def __init__(self,word):
        self.original_word = word
        self.word = ''.join(word) # repeated letters removed. source : https://stackoverflow.com/a/4481731/12579069
        self.correct_guesses = []
        self.life = len(word) # Ben boyle sectim

    def start(self):
        while self.life > 0:
            unique_letters_of_word = list(set(self.original_word))
            if(len(self.correct_guesses) == len(unique_letters_of_word)):
                print("YOU WIN THE GAME!")
                break
            else:
                guessed_letter = input("Enter a letter as your guess: ")
                guessed_letter = guessed_letter.upper()
                if(len(guessed_letter) > 1):
                    print("Please enter a letter")
                    continue
                if(guessed_letter in self.word and guessed_letter not in self.correct_guesses): # correct
                    self.correct_guesses.append(guessed_letter)
                    print("You guessed correctly.", len(unique_letters_of_word) - len(self.correct_guesses)," letters left.")
                    print("You have",self.life,"wrong guessing right.\n")
                elif(guessed_letter in self.correct_guesses):
                    print("You entered that letter before. \n")
                elif(guessed_letter not in self.word):
                    self.life -= 1
                    print("You guessed wrong!", len(unique_letters_of_word) - len(self.correct_guesses)," letters left.")
                    if(self.life == 0):
                        print("YOU LOST THE GAME! GAME IS OVER!")
                        break
                    print("You have",self.life,"wrong guessing right.\n")
        print("Answer is ", self.word)

def getRandomCategory():
    categories = ["animals", "countries", "football_teams"]
    return categories[rnd.randrange(0,len(categories),1)]
def getRandomWordList():
    category = getRandomCategory()
    if(category == "animals"):
        return category, ["SNAKE", "ELEPHANT", "LION", "CROCODILE", "TIGER", "CANARY", "FISH" ]
    elif(category == "countries"):
        return category, ["TURKEY", "AZERBAIJAN", "ENGLAND", "ITALY", "FENERBAHÇE", "KYRGYZSTAN","KAZAKHSTAN","UZBEKISTAN"]
    elif(category == "football_teams"):
        return category, ["FENERBAHÇE","GALATASARAY","BEŞİKTAŞ","GÖZTEPE","KOCAELİSPOR","KARS36 SPOR"]
def getRandomWord():
    category, word_list = getRandomWordList()
    random_index = rnd.randrange(0,len(word_list),1)
    return category, word_list[random_index]


category, word = getRandomWord()

print("The word you will guess is in category", category)

hangman_game = HangmanGame(word)
hangman_game.start()

