from stats import get_words, count_characters, sort_character_count
import sys

def get_book_text(filepath: str) -> str:
    contents = ''
    with open(filepath) as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    book = get_book_text(file_path)
    num_words = get_words(book)

    character_count = count_characters(book)

    char_high_to_low = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in char_high_to_low:
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")
main()
