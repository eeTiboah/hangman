#Hangman Project
import random
import hangman_art
import requests

response = requests.get("https://api.noopschallenge.com/wordbot?count=100")
word_list = response.json()['words']
chosen_word=random.choice(word_list)
end_game=False
lives=6
word_length = len(chosen_word)
word_replace=chosen_word.replace(chosen_word, "_"*word_length)
word_replace_list=list(word_replace)
print(hangman_art.logo)


while not end_game:
	guess_letter = input("Guess a letter: ").lower()
	if guess_letter in word_replace_list:
		print(f"You\'ve already guessed {guess_letter}")
	for position in range(word_length):
		letter=chosen_word[position]
		if letter==guess_letter:
			word_replace_list[position]=letter
	if guess_letter not in chosen_word:
		print(f"You guessed {guess_letter} which is not in the word. You lose a life")
		lives-=1
		if lives==0:
			print("You lose!.")
			print(f"The word is {chosen_word}")
			end_game=True
	print("  ".join(word_replace_list))
	if "_" not in word_replace_list:
		end_game=True
		print("You win!.")
	print(hangman_art.stages[lives])

