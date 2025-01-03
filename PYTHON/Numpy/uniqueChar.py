# Given a Python function that takes in a list of strings, write a code to return a new list containing only those strings in which all characters are distinct (non-repeating). These strings should be present in the same order in which they are present in the input list.

# NOTE: You can assume that the input list contains only lowercase alphabetic characters (a-z).

# Input Format

# List[str]
# Output Format

# List[str]
# Sample Input 1

# ['hello', 'world', 'python', 'programming']
# Sample Output 1

# ['world', 'python']
# Sample Explanation 1

# In this case, the input list contains four strings. The function returns a new list containing only the strings that have all distinct characters. The strings 'hello' and 'programming' have repeated characters, so they are not included in the output list. The strings 'world' and 'python' have all the distinct (non-repeating) characters, so they are included in the output list. They appear in the same order as in the given input list.
# Sample Input 2

# ['abc', 'def', 'ghi', 'jkl']
# Sample Output 2

# ['abc', 'def', 'ghi', 'jkl']
# Sample Explanation 2

# In this case, all the input strings have only unique (non-repeating) characters, so all of them are part of the output list. In the output list, these strings appear in the same order as in the given input list.

####Shortest code##################
def unique_chars(list_of_words):
    ans=[]
    for i in list_of_words:
        if(len(i)==len(set(i))):
            ans.append(i)
    
    print(ans)
    
unique_chars(['hello', 'world', 'python', 'programming'])
unique_chars(['abc', 'def', 'ghi', 'jkl'])

##########Traditional method#######################
def unique_chars1(list_of_words):
    ans=[]
    for i in list_of_words:
        flag=True
        for j in range(len(i)):
            word=i[j]
            count=0
            for k in range(len(i)):
                if(word==i[k]):
                    count+=1
            
            if(count>1):
                flag=False
                break
        if(flag):
            ans.append(i)
    
    print(ans)
    
unique_chars1(['hello', 'world', 'python', 'programming'])
unique_chars1(['abc', 'def', 'ghi', 'jkl'])
