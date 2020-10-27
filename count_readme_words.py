#----------------------------------------------------------------
# File:     count_readme_words.py
#----------------------------------------------------------------
#
# Author:   Marek Rychlik (rychlik@email.arizona.edu)
# Date:     Tue Oct 27 10:06:31 2020
# Copying:  (C) Marek Rychlik, 2020. All rights reserved.
# 
#----------------------------------------------------------------

def count_the_words():
    file = open("README.md", "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))
