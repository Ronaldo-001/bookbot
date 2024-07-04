def main():
    path_to_file = "books/Frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count_word(file_contents)
        char=count_char(file_contents)
        sort_on(char)
        
        

def count_word(book):
    words=book.split()
    print(f"{len(words)} words found in the book")
    

def count_char(book):
    book=book.lower()
    char_count = {}
    for char in book:
        if char.isalpha():  # Check if the character is alphabetic
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
    
def sort_on(char_count):
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    main()
    
