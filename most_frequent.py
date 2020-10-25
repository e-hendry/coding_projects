

def read_file(filename): 
    """
    opens file with input file name, reads the data, removes the new line characters ("\n") and stores it in a list
    one element of the list is a single line of the text file
    """

    with open (filename,"r") as f:
        lines = f.readlines()
        data_clean_line = []
        for l in lines: 
            new_line = l.replace("\n","")
            data_clean_line.append(new_line)
        return data_clean_line




def remove_special(file_contents):
    
    """
    input is the file contents as a list. 
    Function iterates through the list and removes the following special characters: 
    
    question mark (?)
    exclamation mark (!)
    period (.)
    comma (,) 
    semi-colon (;)
    colon (:)
     
    """
    
    cleaned_line = []
    for f in file_contents:
        replacement_line = f.replace("?","").replace("!","").replace(".","").replace(",","").replace(";","").replace(":","")
        cleaned_line.append(replacement_line)
    return cleaned_line




def remove_page_numbers(file_contents):
    """
    remove page numbers from file contents. 
    input is file contents as a list. 
    """
    pages_removed = []
    for t in file_contents: 
        stripped = t.strip()
        if stripped.isdigit()!=True:
            pages_removed.append(stripped)
    return pages_removed




def remove_empty(file_contents): 
    """
    remove any empty elements from the list. 
    input is file contents as list
    """
    non_empty = []
    for l in file_contents:
        if l!="":
            non_empty.append(l)
    return non_empty




def split_data(file_contents):
    """
    split the data by space to make it easier to iterate over. 
    input is file contents as list. 
    """
    
    lines_split_space = []
    for line in file_contents:     
        split_lines = line.split(" ")
        lines_split_space.extend(split_lines)
    return  lines_split_space





def lower_case(file_contents):
    """
    iterate through the list, convert all values to lowercase and save to a new list. 
    input is the file contents as list.
    """
    
    lowercase_text = []
    for i in file_contents: 
        new_values = i.replace(i,i.lower())
        lowercase_text.append(new_values)
    return lowercase_text





# reading the data from the file
filename = "sonnet.txt"
file_contents = read_file(filename)

# removing special characters 
special_removed = remove_special(file_contents)

# removing page numbers 
pages_removed = remove_page_numbers(special_removed)

# removing any empty elements from the list
empty_removed = remove_empty(pages_removed)

# split data by spaces to make it easier to iterate over
lines_split = split_data(empty_removed)

# convert all the values to lowercase so we don't have duplicates in the wordcount
cleaned_text = lower_case(lines_split)




# creating a dictionary of words and their total counts in the text

def create_dictionary(file_contents):
    """
    create a dictionary of keys (words in text) and values (count of words in text)
    input is the file contents as a list
    """

    dictionary = {}
    for i in file_contents: 
        if dictionary.get(i)!=None: 
            dictionary[i]=dictionary.get(i)+1
        else: 
            dictionary[i]=1
    return dictionary




dictionary_counts = create_dictionary(cleaned_text)
dictionary_counts_sorted = sorted(dictionary_counts, key=dictionary_counts.get,reverse=True)





# creating filters for length defined
def select_len(input_list,len_arg):
    """
    filter the dictionary based on the length of the words
    input is a list and the length of words we want
    """
    len_list=[]
    for i in input_list: 
        if len(i)==len_arg: 
            len_list.append(i)
    return len_list





for len_argument in range(2,11):
    sorted_keys_len2 = select_len(dictionary_counts_sorted,len_argument) 
    print('')
    print(f'Top 15, length of word: {len_argument}')
    for i in range(0,15):
        counts_sorted_len2 = dictionary_counts.get(sorted_keys_len2[i])
        print(f'{sorted_keys_len2[i]} {counts_sorted_len2}')






