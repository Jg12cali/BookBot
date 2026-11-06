def get_word_count(book_text):
    words = book_text.split()
    return f"Found {len(words)} total words"

    
def get_character_count(book_text):

   characters = {}

   sanitized_text = book_text.lower()

   for char in sanitized_text:
       if char not in characters:
           characters[char] = 1
       else:
            characters[char] += 1

   order_characters(characters)


def sort_on(character : tuple[str, int]) -> int:
    return character[1]



def order_characters(data):
    unordered_characters = []
    for character in data:
        y = (character, data[character])
        unordered_characters.append(y)
    print(sorted(unordered_characters, reverse=True, key=sort_on))
    

   
        
           
           
           
       

   

   
    
    
    