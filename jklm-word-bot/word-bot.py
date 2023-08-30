import re
import keyboard
import random
from time import sleep
import pyperclip
from pynput.mouse import Controller, Button
from typing import Self

class Wordfinder():
    def __init__(self, instant_typing = False, long_words = True): # Initializes the variables
        self.instant_typing = instant_typing
        self.long_words = long_words
        self.delays = [0.03, 0.04, 0.05, 0.06, 0.40, 0.07, 0.45, 0.36, 0.51, 0.67, 0.23, 0.20]
        self.mouse = Controller()
        self.used_words = set()

    def record_mouse_position(self, key): # Function that listen for your key ('ctrl+f8') until it is pressed
        keyboard.wait(key)
        current_position = self.mouse.position
        return current_position

    def listen_for_ctrl_f9(self, key, position): # Function that listens for your key ('ctrl+f9') until it is pressed
        keyboard.wait(key)
        self.move_mouse_to(position)

    def move_mouse_to(self, position): # Function that moves your mouse to your recorded mouse position using Ctrl + F8
        self.mouse.position = position
        sleep(0.01)
        self.double_click_copy_paste()

    def double_click_copy_paste(self): # Copy paste
        self.mouse.click(Button.left, 1)
        sleep(0.01)
        self.mouse.click(Button.left, 1)

        keyboard.press_and_release('ctrl+c')
        sleep(0.01)
        return pyperclip.paste()
    
    def find_matching_words(self, file_name, prefix): # Search that specific two letter string in the wordlist.txt
        matching_word = []
        used_words = []

        with open(file_name, 'r') as file: # Opening the text file
            for text in file:
                word = text.strip() # Removes /n in the lists, because as default it will output with newlines without strip()
                match = re.search(prefix, word) # Uses re.search to match that two letter string to your word
                
                if match:
                    matching_word.append(word)

        remaining_words = [word for word in matching_word if word not in self.used_words]

        if not remaining_words:
            return "No more matching words available"
        
        chosen_word = random.choice(remaining_words)
        self.used_words.add(chosen_word)
        return chosen_word
    
    def write_the_word(self, final_word):
        for letter in final_word:
            keyboard.write(letter)
            delay = random.choice(self.delays)
            sleep(delay)
        
       
if __name__ == "__main__":
    wordfinder = Wordfinder()

    # Listens for your keyboard input
    recorded_position = wordfinder.record_mouse_position('ctrl+f8')

while True:
    wordfinder.listen_for_ctrl_f9("ctrl+f9", recorded_position)
    
    # Signals the copypaste function   
    prefix = wordfinder.double_click_copy_paste()

    # Put the file location of wordlists.txt here 
    file_name = r"C:\Users\admin\OneDrive\Documents\Development\Random\jklm-word-bot\wordlist.txt"

    matching_word = wordfinder.find_matching_words(file_name, prefix)
    
    wordfinder.write_the_word(matching_word)

