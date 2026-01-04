from stats import get_book_text, count_words, count_letter


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print(count_letter(text))


main()
