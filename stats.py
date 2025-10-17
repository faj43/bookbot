import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text(sys.argv[1])

def word_count():
    book_text = get_book_text(sys.argv[1])
    char_count = book_text.split()
    count = len(char_count)
    print("Found",count,"total words")

word_count()

def letter_count():

    book_text = get_book_text(sys.argv[1])
    
    count = {}
    for letter in book_text:
         letter = letter.lower()  #make it small
         if letter.isalpha():
            if letter in count:    #is my letter already in the count?
                count[letter] += 1
            else:      #if not, add it
                count[letter] = 1
    return count
    

def sort_on(item):
    return item["num"]

def sort_list(counts):
    items = []
    for ch, n in counts.items():
        items.append({"char": ch, "num": n})
    items.sort(reverse=True, key=sort_on)
    return items





    


