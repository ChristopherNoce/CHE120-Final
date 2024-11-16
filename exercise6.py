#!/usr/bin/env python
# coding: utf-8

# # Exercise 6

# #### Problem 1
# 
# Which operator is used to access methods and members of an object in python? Please write it in the string below. 

# In[ ]:


problem1 = '.'#write only the operator inside the string


# #### Problem 2
# 
# Choose the options that are existing methods of the `str` class. 
# 
# **a)** casefold
# 
# **b)** isnum
# 
# **c)** lower
# 
# **d)** format
# 
# **e)** translate
# 

# In[ ]:


problem2 = 'acde'#'a','b','ab',etc


# #### Problem 3
# 
# How many `str` methods start with the letter `i`? Assign the numeric value to `problem3`. 

# In[ ]:


problem3 = 13# write numeric int value, i.e. 4, 10, etc 


# #### Problem 4
# 
# (True/False) The class object `str` has a method `capitalize()` which may be called explicitly as follows,
# 
# ```python
# string = "my string"
# 
# str.capitalize(string)
# ```

# In[ ]:


problem4 = True # True or False


# #### Problem 5
# 
# We have a string stored in a variable called `p5s` which is a combination of lower and upper case letters. 
# 
# In one line :
# 
# 1. Swap the case of all the letters (make lower into upper case and vice versa).
# 2. Count the occurrences of the letter 'O' in the resulting string from 1 by chaining method calls.

# In[13]:


problem5 = p5s.swapcase().count("O")


# #### Problem 6
# 
# We have a function `problem6(first_name, last_name)` that takes the first and last name of a student. The two arguments should be strings that are provided in lower case (please verify this in your functions). We would like the function to return the initial of the two names, so `problem6('alice','smith')` should return `AS` and `problem6('alice','SMITH')` should return `None`.

# In[41]:


def problem6(first_name, last_name):
    '''
    (str, str) -> str

    This function takes the first and last name of a student, then returns the initial of the two names

    >>>problem6('alice','SMITH')
    None
    >>>problem6('alice,'smith')
    AS
    '''
    if type(first_name) != str or type(last_name) != str:
        return None
    elif first_name.islower() and last_name.islower():
        return first_name[0].upper() + last_name[0].upper()
    else:
        return None


# #### Problem 7
# 
# Given the list `p7l`, assign to `problem7` a new list containing only the first and last item of `p7l` in order.

# In[ ]:


problem7 = [p7l[0],p7l[-1]]


# #### Problem 8
# 
# Given the list `p8l` of numeric objects, assign `problem8` a new list with items (in order): the minimum value, the maximum value, and the average value in `p8l`.

# In[ ]:


problem8 = [min(p8l), max(p8l), sum(p8l)/len(p8l)]


# #### Problem 9
# Develop a function `problem9(list1, list2, index)` that :
# 
# 1. Concatenates the contents of list1 and list2 in a new list.
# 2. Returns the item stored in index in the new list.
# 
# Note: the only validity check you need to do is to see whether `index` refers to an acceptable index in the resulting list from `list1` and `list2` and return `None` otherwise.  

# In[ ]:


def problem9(list1, list2, index): 
    new_list = list1 + list2
    print(new_list)

    if type(index) != int or index >= len(new_list) or index < len(new_list)*-1:
        return None
    else:
        return new_list[index]


# #### Problem 10
# 
# Develop a function `problem10(lists)` that finds the first and last string (lexicographic order) in a list of strings `lists` and returns a new list with these items (in order).

# In[ ]:


def problem10(lists): 
    if type(lists) != list:
        return None
    else:
        lists.sort()
        return [lists[0],lists[-1]]
    


# #### Problem 11
# 
# Given lists `class_names` and `class_surnames` along with the strings `student_name` and `student_surname`, assign to `problem11` the value `True` if the student is in the class and `False` otherwise.

# In[ ]:

def in_class(student_name, class_names, student_surname, class_surnames):
    if student_name in class_names and student_surname in class_surnames:
        return True
    else:
        return False

problem11 = in_class(student_name, class_names, student_surname, class_surnames)

