frank_path = "frankenstein.txt"

def get_book_text(file_path):
    with open(f"./books/{file_path}")as f:
        return f.read()

def get_word_count(book_text):
    words = book_text.split()
    return f"Found {len(words)} total words"

text = get_book_text(frank_path)
print(get_word_count(text))



    