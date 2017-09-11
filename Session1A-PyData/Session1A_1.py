
# coding: utf-8

# # Introduction to Python

# ## Data types

# Python has four basic data types that we will use:
# 
# + float (which is for numerical or _floating point_ data)
# + int (which is for integer data)
# + str (which is for strings or character data)
# + boolean (i.e. True/False, which is used for testing)
# 
# Python can do basic calculations 

# In[1]:

1+1


# In[2]:

4 * 5


# In[3]:

6/4


# > This is a good new feature for Python 3. In Python 2 the above would give you 1, since it did something called integer division. That can still be done in Python 3, but it's not the default behavior

# In Python, we can assign quantities to __variables__, that is, named objects. Internally this serves as a container for the quantity, which has a particular address in your computer. 

# In[25]:

a = 123
b = 123.0
c = '123'


# In Excel, these three quantities might look the same, but in Python (or any other computer language) you have to be careful

# In[26]:

type(a)


# In[27]:

type(b)


# In[28]:

type(c)


# In[9]:

a == b


# In[10]:

a == c


# In[11]:

d = 123.000000000001
a == d


# In[12]:

b == d


# Once again, a and d might look the same in a spreadsheet, but if the actual recorded numbers are different, Python will make a distinction

# ## Lists, Tuples and Dictionaries

# There are three kinds of bracketed entities in Python:
# 
# 1. Lists (`[]`)
# 2. Tuples (`()`)
# 3. Dictionaries (`{}`)
# 
# Lists are baskets that can contain different kinds of things. They are ordered, so that there is a first element, and a second element, and a last element, in order. 
# 
# Tuples are basically like lists, except that they are _immutable_, i.e., once they are created, individual values can't be changed. They are also ordered.
# 
# Dictionaries are __unordered__ key-value pairs, which are very fast for looking up things. They work almost like hash tables. Dictionaries will be very useful to us as we progress towards the PyData stack. Elements need to be referred to by _key_, not by position.

# In[6]:

test_list = ['apple', 3, True, 'Harvey', 48205]


# In[8]:

test_list


# In[9]:

len(test_list)


# In[10]:

test_list[0]


# In[11]:

test_list[:3]


# In[12]:

test_list[2:]


# The important thing here is if you provide an index `a:b`, then `a` is included but `b` __is not__

# In[13]:

test_list[-1]


# In[18]:

test_list


# In[14]:

test_list[:-1]


# In[15]:

test_list[-3:]


# In[17]:

test_list[-3:-1]


# You can also make a list of lists, or nested lists

# In[23]:

test_nested_list = [[1,'a',2,'b'],[3,'c',4,'d']]
test_nested_list


# This will come in useful when we talk about arrays and data frames.

# ### Tuples

# Tuples are like lists, except that once you create them, you can't change them.

# In[17]:

test_tuple = ('apple', 3, True, 'Harvey', 48205)


# In[20]:

test_tuple[:3]


# In[21]:

test_list[0] = 'pear'
test_list


# In[22]:

test_tuple[0] = 'pear'
test_tuple


# ## Dictionaries

# In[3]:

test_dict = {1: 'value', 'a': 3245}


# In[37]:

test_dict[1]


# In[38]:

test_dict['a']


# In[39]:

type(test_dict)


# In[41]:

test_dict['a'] = 4524
test_dict


# In a dictionary, the keys can be strings, numbers or tuples, but the values can be any Python object. You can see the keys and values using extractor functions

# In[4]:

test_dict.keys()


# In[5]:

test_dict.values()


# ### Loops and list comprehensions

# Python has loops to iterate through a group of things. Usually these are lists, but you can loop through tuples and dictionaries too.

# In[7]:

for i in range(len(test_list)):
    print(test_list[i])


# In[9]:

for u in test_list:
    print(u)


# In[14]:

test_list2 = [1,2,3,4,5,6,7,8,9,10]
mysum = 0
for u in test_list2:
    mysum +=  u
print(mysum)


# ### List comprehensions

# In[15]:

squares = [u**2 for u in test_list2]


# In[16]:

squares


# In[20]:

[type(u) for u in test_tuple]


# In[31]:

even_numbers = [u for u in squares if u % 2 == 0]
even_numbers


# ### String operations

# Strings operations are actually quite commonly used for data cleaning and data munging. Specially when doing text analytics, or even when we are dealing with categorical data.

# In[13]:

'a' + 'b'


# In[14]:

5 * 'a'


# In[31]:

fname = 'Larry.txt'
newname = fname.replace('Larry','Henry')
newname


# > Notice that we attach a function after an object: `fname.replace()`. This is called piping, and allows us to write expressive code

# Here's one we use quite often when reading or verifying files:

# In[17]:

test_string = 'A quick brown fox leaps over the lazy rabbit'
test_string.split(' ')


# In[18]:

test_string2 = 'Jack, Ryder, 301-357-2436, Ashburn, Virginia,56'
test_string2.split(',')


# Strings can be sliced just like lists. 

# In[34]:

fname[2:5]


# In[35]:

len(fname)


# ## Loops

# We're doing loops here both to demonstrate loops (for loops in particular), but also to demonstrate a syntactical issue with Python that often bites users.

# In[1]:

for i in range(10):
    print(i)


# The general structure for a `for` loop is:
# 
# ```python
# for (element) in (list):
#     do some stuff
#     do more stuff
# ```

# One can also do what are known as _list comprehensions_, which are useful shortcuts.

# In[42]:

names = ['Abby','Benjy','Carmen','David','Eli']
length_names = [len(x) for x in names]


# In[43]:

length_names


# So list comprehensions take a list, apply some function to each of the elements of the list, and then returns the results into a list.
# 
# The last part of the statement is basically querying if an element is in the list `names`. You can ask this question generally:

# In[44]:

'Abby' in names


# In[45]:

'Gavin' in names


# These require exact matches:

# In[46]:

'Abb' in names


# Fuzzy matching requires a package. Typically the package `fuzzywuzzy` is suggested. 
