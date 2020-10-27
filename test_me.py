import datetime
from count_readme_words import count_the_words

def test_word_count():
    run_name = datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
    print(run_name)
    count_the_words()

if __name__ == '__main__':
    test_word_count()
