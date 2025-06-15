#def get_num_words(text):
    #num_words=0
    #separate=text.split()
    #num_words=len(separate)
    #return num_words
def number_of_letters(text):
    char_count = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_letters(char_count):
    sorting_list=[]
    for letter in char_count.keys():
        #print(letter)
        if letter.isalpha() is True:
            #print(letter)
            sorting_list.append({"char":letter,"num":char_count[letter]})
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list

