import sys

from stats import get_word_count, get_character_count

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    character_list = get_character_count(book_text)
    get_final_report(sys.argv[1], word_count, character_list)
   

def get_book_text(file_path):
    with open(file_path)as f:
        return f.read()

def get_final_report(path, word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_list:
        if character[0].isalpha():
            print(f"{character[0]}:{character[1]}")
        continue
    print("============= END ===============")
        
    
main()





    