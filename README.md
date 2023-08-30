This bot is highly inspired of nicolaspiet's github repo, **[jklm-word-bot]([url](https://github.com/nicolaspiet/jklm-word-bot.git)https://github.com/nicolaspiet/jklm-word-bot.git)**, but slightly optimized. I found out that their code is slight buggy in terms of getting the mouse position, and word output is apparently typing random words. I optimized that using my own OOP programming.

# Requirements
 - pynput
 - keyboard
 - pyperclip

# Installation
 - Step 1: Download the zip of this file and then extract.
 - Step 2: Once extracted, copy the file location of the file **(e.g. C:/Users/admin/Downloads/jklm-word-bot)**
 - Step 3: Open up the terminal, and then change your directory to that file location. For example, type **"cd C:/Users/admin/Downloads/jklm-word-bot"**
 - Step 4: Run **"pip install -r requirements.txt"**
 - Step 5: Once installed, you're good to go!

# Usage
 - Step 1: Run **word-bot.py** using a code editor or simply the same terminal earlier and run 'python word-bot.py'.
 - Step 2: Go to the JKLM game as soon as it starts. Place your cursor over the two letter text inside the bomb, and press **'Ctrl + F8'**. 
 - Step 3: When it is now your turn, press **'Ctrl + F9'**. 

# Functionality
 - 'Ctrl + F8': This will copy your current mouse cursor position, so make sure it is accurate.
 - 'Ctrl + F9': This will immediately hover your mouse cursor to your previously recorded mouse position, and prompts the code to output the text automatically in the typing box by using **pyperclip** and **keyboard.write** with **different delays** in typing speed. Hence, it is coded to act like a human.

# Walkthrough
![automated-jklm-word-bot](https://github.com/meezlung/automated-jklm-word-bot/assets/65329581/7219aa11-6540-4bec-9cb7-11f492d09df3)



