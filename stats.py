def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def count_words(content):
    return len(content.split())


def count_letter(content):
    count_letter = 0
    letters = {}
    for character in content:
        if character.isalpha():
            lower = character.lower()
            if lower in letters:
                letters[lower] += 1
            else:
                letters[lower] = 1
    sorted_dict = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


def print_sorted_list(sorted_dict):
    for letter, count in sorted_dict:
        print(f"{letter}: {count}")
