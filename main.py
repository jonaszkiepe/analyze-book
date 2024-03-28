def main():
    document = "./books/frankenstein.txt"
    book = get_text(document)
    word_count = count_words(book)
    character_count = count_characters(book)
    report(word_count, character_count, document)


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(book):
        words = book.split()
        return len(words)


def sort_on(dict):
    return dict["number"]


def count_characters(book):
    char_infos = []
    unique_chars = set()
    for char in book:
        lower_char = char.lower()
        if lower_char.isalpha():
            new_info = { "name": lower_char, "number": 1,}
            if char_infos == [] or lower_char not in unique_chars:
                char_infos.append(new_info)
                unique_chars.add(lower_char)
            else:
                for info in char_infos:
                    if lower_char == info["name"]:
                        info["number"] += 1
    char_infos.sort(reverse=True, key=sort_on)
    return char_infos


def report(words, characters, document):
    print(f"--- Begin report of {document} ---")
    print(f"There is {words} words in the document.\n\n")
    for info in characters:
        print(f"{info["name"]} was found {info["number"]} times.")
    print("--- End of report ---")


main()
