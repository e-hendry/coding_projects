
from collections import deque
from queue import LifoQueue
import re


class HTMLVerifier:
    
    """
    the class HTMLVerifier has 3 methods: 
    __init__: initializes an instance of the class with a filename
    check_balance(): checks which tags are unbalanced in the input file 
    print_unbalanced(): prints out pairs of unbalanced tags in the html document   
    
    """
    
    def __init__(self,filename):
        self.filename = filename
        self.unbalanced_tags=[]
    
    def check_balance(self):
        with open(self.filename, 'r') as f:
            s = LifoQueue()
            #unbalanced_tags = []
            for line in f.readlines():
                tag = re.findall(r'[<][/]{0,1}[a-z0-9]+[>]',line)
                if tag!=[]:
                    for i in tag:
                        if re.findall(r'[<][a-z0-9]+[>]',i)!=[]: #if the tag is an opening tag
                            stripped_tag_opening=re.findall(r'[<][/]{0,1}([a-z0-9]+)[>]',i)
                            s.put(stripped_tag_opening) # adding the stripped opening tag to the stack 
                        else: 
                            stripped_tag_closing=re.findall(r'[<][/]{0,1}([a-z0-9]+)[>]',i)
                            if s.empty()==False: #if the stack is not empty
                                last_val = s.get() #get the last value from the stack 
                                if last_val!=stripped_tag_closing: #if they don't match 
                                    opening_tag=f'<{last_val[0]}>'
                                    self.unbalanced_tags.append(opening_tag)
                                    self.unbalanced_tags.append(i)
                            else: #if the stack is empty 
                                self.unbalanced_tags.append(i)
                
        while s.empty()==False: #checking for any extra opening tags 
            unmatched_val = s.get()
            unmatched_opening = f'<{unmatched_val[0]}>'
            self.unbalanced_tags.append(unmatched_opening)
                
    
    def print_unbalanced(self):
        if self.unbalanced_tags==[]:
            print('all tags are balanced')
        else:
            print(*self.unbalanced_tags,sep=', ')



