def get_book_text(filepath):
    file_contents = ""
    with open("books/" + filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")

if __name__ == "__main__":
    main()