
import re



def user_input():

    """
    @ function to prompt user to enter the length of the word and the number of terms to return 
    @ function takes no arguments, function returns the word length and number of terms
    @ if the user doesn't enter integers they will get an error message and be prompted to enter again
    """

    user_input=input("Enter length of word and # terms to return: ")
    user_input_split=re.findall("\S*[0-9]", user_input)
    word_length_str=user_input_split[0]
    no_terms_str =user_input_split[1]

    while word_length_str.isdigit()==False or no_terms_str.isdigit()==False: 
        print("Word length and number of terms must be integers")
        user_input=input("Enter length of word and # terms to return: ")
        user_input_split=re.findall("\S*[0-9]", user_input)
        word_length_str=user_input_split[0]
        no_terms_str = user_input_split[1]

    word_length = int(word_length_str)
    no_terms =int(no_terms_str)
    
    return word_length, no_terms



def read_file(filename): 
    """
    opens file with input file name, reads the data and stores it in a list
    """

    with open (filename,"r") as f:
        lines = f.readlines()
        return lines


def convert_file_contents(file_contents):
    """
    @ function to iterate through file contents and extract words 
    @ the data is converted to lowercase, so we don't get duplicated word counts for upper and lowercase
    @ stores the words extracted from the file contents in a list 
    
    """

    file_contents_split=[]
    for item in file_contents:
        x = re.findall("\S*[a-z]", item)
        for word in x:
            converted_word = word.lower()
            file_contents_split.append(converted_word)
    return file_contents_split



def select_words(word_length): 
    """
    @ function to get a list of all the words of a specified length 
    @ argument is word_length which is an integer
    """
    result=[]
    for item in file_contents_split:
        item_length=len(item)
        if item_length==word_length:
            result.append(item)
    return result




def word_counter(input_list): 
    """
    @ function to go through list and create a counter of items in the list.
    
    """
    from collections import Counter
    word_count=Counter(input_list)
    return word_count




def filter_counter(number_words,word_count): 
    """
    @ function to filter word count to the top nth words.
    """
    from collections import Counter
    results_filtered=word_count.most_common(number_words)
    return results_filtered 




def print_word_count_results(results_filtered,no_words,word_length): 
    """
    @ function to print the results of the word count for the specified number of words and length of word
    @ Words with punctuation in them such as "to-day" are kept intact as a single word. 
    @ function argument is the data filtered to the specified word length 
    """
    print(f'Top {no_words}, length of word: {word_length}')
    for item in results_filtered: 
        print(item[0],item[1])




# Getting the user input 
user_input_values = user_input()
word_length = user_input_values[0]
no_words = user_input_values[1]




# Reading the data from the sonnet file
filename = "sonnet.txt"
file_contents = read_file(filename)




# Using the convert_file_contents function to get the contents of the file split by word in a single list
file_contents_split = convert_file_contents(file_contents)




# Selecting words of length specified by user
selected_words = select_words(word_length)




# Creating a word counter for the words of the specified length
word_counter_selected_length = word_counter(selected_words)




# Filter the word counter to the number of words we want
filtered_counter = filter_counter(no_words,word_counter_selected_length)



# Print the filtered word count results
print_word_count_results(filtered_counter,no_words,word_length)






