from stats import get_word_count, get_character_count

def main():
    frank_path = "frankenstein.txt"
    book_text, book_path = get_book_text(frank_path)
    print(book_path)
    print(get_word_count(book_text))
    get_character_count(book_text)
   

def get_book_text(file_path):
    path = f"./books/{file_path}"
    with open(path)as f:
        return f.read(), path


main()





    