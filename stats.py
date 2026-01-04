def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def count_words(content):
    words = content.split()
    count = 0
    for word in words:
        count += 1
    return count


# {'p': 6121, 'r': 20818, 'o': 25225, ...


def count_letter(content):
    count_letter = 0
    letters = {}
    for character in content:
        for letter in character:
            lower = letter.lower()
            if lower in letters:
                letters[lower] += 1
            else:
                letters[lower] = 1
    return letters


