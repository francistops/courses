# my code for the project (same output as instructor)
import string


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    print()

    letters_count = {}
    for letter in string.ascii_lowercase:
        letters_count[letter] = get_num_letter(text, letter)

    for letter in sorted(letters_count, key=letters_count.get, reverse=True):
        print(f"The '{letter}' character was found {
              letters_count[letter]} times")

    print('--- End report ---')


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letter(text, letter):
    return text.lower().count(letter)


main()
