#from stats import get_num_words
from stats import number_of_letters
from stats import sorted_letters
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        text=f.read()
    return text
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        arguments=sys.argv
        filepath=arguments[1]
    text=get_book_text(filepath)
	#num_words=get_num_words(text)
	#print(f"{num_words} words found in the document")
    letter_count=number_of_letters(text)
    #print(number_of_letters(text))
    #print(text)
    #print(letter_count)
    x=sorted_letters(letter_count)
    #print(len(x))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arguments[1]}...")
    print("----------- Word Count ----------")
    #printing total words
    a=text.split()
    b=0
    for word in a:
       b+=1 
    print(f"Found {b} total words")
	#printing sorted numbers
    print("--------- Character Count -------")
    for i in range(0,len(x)):
        y=x[i]
        print(f"{y["char"]}: {y["num"]}")
    print("============= END ===============")
main()
