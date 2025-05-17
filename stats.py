
def get_words(book: str) -> int:
    words = book.split()
    return len(words)

def count_characters(book: str):
    character_count = {}

    for char in book:
        if char.lower() in character_count:
            character_count[char.lower()] += 1
        else:
            character_count[char.lower()] = 1

    return character_count

def sort_character_count(characters):
    listified = [{"char": char, "num": num} for char, num in list(characters.items()) if char.isalpha()]

    listified.sort(key=lambda x: x["num"], reverse=True)

    return listified
