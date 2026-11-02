from stats import get_word_count, get_character_count


def main():
    frank_path = "frankenstein.txt"
    book_text = get_book_text(frank_path)
    print(get_word_count(book_text))
    print(get_character_count(book_text))
    

def get_book_text(file_path):
    with open(f"./books/{file_path}")as f:
        return f.read()

main()





    