from stats import get_book_text, count_words, count_letter, print_sorted_list
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(path)
    num_words = count_words(text)
    sorted_list = count_letter(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    report = print_sorted_list(sorted_list)
    print("============= END ===============")


main()
