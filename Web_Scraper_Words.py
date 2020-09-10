import requests, timeit
#from bs4 import BeautifulSoup
# Imports requests module to access the url with the file containing all the "real" words in the english dictionary
# bs4 isn't used but i think it might be useful
'''
for i in all_words:
    print(i)
    time.sleep(0.01)
'''

class word_object:
    def __init__(self, word):
        self.word = word
        self.ordered = "" # Prepares an empty string to be used later as a comparison with the anagram
        self.anagrams = [] # Prepares an empty list for use later

    def check_if_same_letter(self, check_word, number):
        # Currently no use
        if check_word == self.word[number]:
            return True
        return False
    '''
    def get_length(word):
        counter = 1
        for letter in word:
            counter =+ 1
        return counter
    '''
    def anagram(self, all_words):
        # A method to search all words for an anagram

        self.ordered = list(self.word)  # Makes a list containing the letters of the word e.g ['a', 'n', 'i', 'm', 'a', 'l']
        self.ordered_values = list(map((lambda x: ord(x)), self.ordered)) # Turns the list of letters into ASCII values e.g [97, 110, 105, 109, 97, 108]
        self.ordered_values.sort() # Sorts the list by number value e.g [97, 97, 105, 108, 109, 110]

        for word in all_words: # For every word in the list of all words
            if not len(word) == len(self.word):
                continue # skips a word if they are not the same length to the original word

            # print(word, " not skipped") # Prints all words not skipped by above "catchall"

            word_letter_list = list(word) # Makes a list containing the letters of every word e.g ['a', 'n', 'i', 'm', 'a', 'l']
            word_letter_values = list(map((lambda x: ord(x)), word_letter_list)) # Turns the list of letters into ASCII values e.g [97, 110, 105, 109, 97, 108]
            word_letter_values.sort() # Sorts the list by number value e.g [97, 97, 105, 108, 109, 110]

            # If the two sorted lists have the same length AND have the same ASCII values that means that they are anagrams
            # (and they're not the same word)
            if word_letter_values == self.ordered_values and word != self.word and not type(word) == "NoneType":
                self.anagrams.append(word)
                
                # Appends this anagram to a list containing all anagrams of this specific word


#soup = BeautifulSoup("html.parser")
def get_words(language):
    # Determinues which language to use, if no valid language is given "en" is default

    if language.lower() == "en":
        url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'

    elif language.lower() == "se":
        url = "https://raw.githubusercontent.com/martinlindhe/wordlist_swedish/master/swe_wordlist"

    else:
        url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'


    # Gets all data from the url as a "Response" object containing all the data from the HTML
    # Then puts all the text from the website into a list called all_words
    # This list is then turned into a set to increase performance
    r = requests.get(url)
    all_words = r.text.split()
    set(all_words)

    # A fun little thingy that shows the amount of words in a language according to my sources
    #
    # counter = 0
    # for i in all_words:
    #     counter += 1
    # print(language, " has ", counter, " words")
    #

    # Returns the set
    return all_words


def is_word(word, all_words, language):
    for i in all_words:
        if word == i:
            return True
    return False


def main():
    # Sets a running variable to True making this an infinite loop, although bad practice I will implement an easier exit condition
    running = True
    selected_words = []
    # Sets the language to use in the comparisons, although technically you could use both
    language = input(r"Choose a language (en or se) ")

    # Sets it to lowercase to ensure no errors in comparison
    language = language.lower()

    # Gets all the words with that language
    all_words = get_words(language)

    # create sets containing words of specific length e.g 1 letter, 2 letters ...
    #for i in range(20):
    #    pass

    run_type = input(r"Word check + anagram (WC) OR find all words without anagrams (WA)? ")
    while running:
        if run_type.lower() == "wa":
			pass
			'''# NOTE: the total runtime of this function would be somewhere around
            # 11 DAYS so optimisation is really neeeded!
            start = timeit.default_timer()
            # anagrams_list = []
            anagram_file = open("Anagrams_sv.txt", "r+")
            for word in all_words:
				
                start1 = timeit.default_timer()
                new_word_obj = word_object(word)
                #print(new_word_obj.word)
                new_word_obj.anagram(all_words)
                #if word.anagrams:
                #    anagrams_list.append(word)

                if not new_word_obj.anagrams:
                    stop1 = timeit.default_timer()
                    #print(word, " has no anagrams. Runtime is: ", stop1 - start1)
                    try:
                        write_word = new_word_obj.word + "\n"
                        anagram_file.write(write_word)
                    except IOError as a:
                        print(str(a), "error in word ", new_word_obj.word)
                        del new_word_obj
                        continue
                    except:
                        print("general error")
                    del new_word_obj
                else:
                    del new_word_obj
            # print("Words that have atleast one anagram: ", str(anagrams_list), "\n")

            stop = timeit.default_timer()
            print("Runtime is :", stop - start)
            anagram_file.close()
            running = False
			'''
        else: #if run_type.lower() == "wc":
            word = input(r"Check if a word is real: ")
            word = word.lower()
            start = timeit.default_timer()

            if is_word(word, all_words, language):
                print(word, " is a real word")
                if any in selected_words == word:
                    for used_word in selected_words:
                        if used_word == word:
                            used_word.anagram(all_words)
                            for anagrams in word.anagrams:
                                print(anagrams, " is an anagram to ", word.word)
                        else:
                            continue
                else:
                    selected_words.append(word)
                    word = word_object(word)
                    word.anagram(all_words)
                    for anagrams in word.anagrams:
                        print(anagrams, " is an anagram to ", word.word)

            else:
                print(word, " is NOT a real word")

            stop = timeit.default_timer()
            print("Runtime is :", stop - start)
            '''
            cont = input("Do you want to continue ? y/n ")
            if cont.lower == "n":
                running = False
            '''
# Checks if this code specifically is run
if __name__ == "__main__":
    main()

