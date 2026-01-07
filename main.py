import sys
from stats import count_characters, count_words, sorted_list

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    wordcount = count_words(book_text)
    amount = count_characters(book_text)

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {wordcount} total words
--------- Character Count -------""")
    for char in sorted_list(amount):
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()