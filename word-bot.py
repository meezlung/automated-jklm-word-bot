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
        self.delays = [0.03, 0.04, 0.05, 0.06, 0.04, 0.07, 0.045, 0.036, 0.051, 0.067, 0.023, 0.20]
        self.mouse = Controller()
        self.used_words = set()

    def record_mouse_position(self, key): # Function that listen for your key ('ctrl + f8') until it is pressed
        keyboard.wait(key)
        print('Bomb text position recorded.')
        current_position = self.mouse.position
        return current_position
    
    def record_text_box_position(self, key): # Function that listens for your key ('ctrl + f9) until it is pressed
        keyboard.wait(key)
        print('Text box position recorded.')
        text_box_position = self.mouse.position
        return text_box_position

    def listen_for_ctrl_f11(self, key, text_position): # Function that listens for your key ('ctrl + f11') until it is pressed
        keyboard.wait(key)
        self.move_mouse_to(text_position)

    def move_mouse_to(self, text_position): # Function that moves your mouse to your recorded mouse position using 'ctrl + f8'
        self.mouse.position = text_position
        sleep(0.01)
        self.double_click_copy_paste_to_text_box()

    def double_click_copy_paste_to_text_box(self): # Copy paste
        self.mouse.click(Button.left, 1)
        sleep(0.1)
        self.mouse.click(Button.left, 1)

        keyboard.press_and_release('ctrl+c')
        sleep(0.1)
        pasted = pyperclip.paste()
        caps = pasted.upper()
        sleep(0.1)

        return caps
    
    def find_matching_words(self, file_name, prefix): # Search that specific two letter string in the wordlist.txt
        matching_word = []

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
    
    def write_the_word(self, final_word, text_box_position):
        self.mouse.position = text_box_position
        self.mouse.click(Button.left, 1)
        sleep(0.2)

        for letter in final_word:
            keyboard.write(letter)
            delay = random.choice(self.delays)

            sleep(delay)
        
        keyboard.press_and_release('enter')
        
       
if __name__ == "__main__":
    wordfinder = Wordfinder()

    # Listens for your keyboard input
    recorded_text_position = wordfinder.record_mouse_position('ctrl+f8')
    recorded_text_box_position = wordfinder.record_text_box_position('ctrl+f9')

while True:
    wordfinder.listen_for_ctrl_f11("ctrl+f11", recorded_text_position)
    
    # Signals the copypaste function   
    prefix = wordfinder.double_click_copy_paste_to_text_box()

    # Put the file location of wordlists.txt here 
    file_name = r"wordlist.txt"

    matching_word = wordfinder.find_matching_words(file_name, prefix)
    
    wordfinder.write_the_word(matching_word, recorded_text_box_position)