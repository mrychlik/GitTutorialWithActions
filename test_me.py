#----------------------------------------------------------------
# File:     test_me.py
#----------------------------------------------------------------
#
# Author:   Marek Rychlik (rychlik@email.arizona.edu)
# Date:     Tue Oct 27 10:19:34 2020
# Copying:  (C) Marek Rychlik, 2020. All rights reserved.
# 
#----------------------------------------------------------------
# Run some tests

import datetime
from count_readme_words import count_the_words

if __name__ == '__main__':
    run_name = datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
    print(run_name)
    count_the_words()
