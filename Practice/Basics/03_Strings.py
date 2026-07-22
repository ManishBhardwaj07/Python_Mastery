# String  


# name = "Manish"
# city = "Patna"
# course = "AIML"

# """
# Character:   M   a   n   i   s   h
# Index:       0   1   2   3   4   5

# """

# # Indexing

# name = "Manish"

# print(name[0])  
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# #  print(name[8])  # This will give an error because index 8 does not exist in the string "Manish"

# ## Negative Indexing]
# """
# Character:   M   a   n   i   s   h
# Positive:    0   1   2   3   4   5
# Negative:   -6  -5  -4  -3  -2  -1

# """

# name = "Manish" 

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[-6])

# word = "Developer"

# print(word[-1])
# print(word[-4])
# print(word[-9])

# ## Slicing
# # #  string[start : end]

# # Remember this rule:
# # Start is included, End is excluded.

# name = "Manish"
# print(name[0:3])
# print(name[1:4])  
# print(name[2:6])

# print(name[:4]) # it will take from 0 to 3 index , as it is not mentioned in the start index , so automatically it will take 0 index as start index

# print(name[2:]) # it will take from 2 to last index , as it is not mentioned in the end index , so automatically it will take last index as end index

# word = "Programming"
# print(word[0:6])
# print(word[3:9])
# print(word[3:9])
# print(word[:4])
# print(word[5:])

# country = "India"
# print(country[0:3])
# print(country[2:])
# print(country[0:])
# print(country[1:3])
# print(country[-1])

# # Slicing with Steps
# # string[start : end : step]

# name = "Manish"
# print(name[0:6:2])  # M n s
# print(name[0:6:3])  # M i
# print(name[1:6:2])  # a i h

# name = "Manish"
# print(name[::2])
# print(name[::3])

# print(name[::-1])  # Reverse the string 
# print(name[::2])  # Reverse every second character of the string


# text = 'artificial intelligence'
# print(text[::2])
# print(text[::3])
# print(text[::-1])  # Reverse the string
# print(text[::-2])

# name = "Python"

# print(name[::-1])

# word = "MachineLearning"
# print(word[:7])
# print(word[7:])
# print(word[:4])
# print(word[8:])
# print(word[::-1])
# print(word[::2])
# print(word[::3])

## Strings Methods

# name = "manish"
# print(name.upper())  # Convert to uppercase

# name = "MANISH"
# print(name.lower()) 

# name = "manish"
# print(name.capitalize()) # make first letter capital

# sentence = "i love python"
# print(sentence.title()) ## makes the first letter of every word capital

# text = "Manish Kumar"
# print(text.swapcase()) # Changes uppercase to lowercase and lowercase to uppercase


# text = "welcome to python programming"
# print(text.upper())
# print(text.capitalize())
# print(text.capitalize())
# print(text.title())
# print(text[:17].upper() + text[17:])

## Strip ()
# removes extra spaces from the beginning and end of a string 

# text = "   Hello Python   "
# print(text)
# print(text.strip()) # Removes the spaces from beginning and end 

# ## Replace()

# # Replaces one word or character with another 
# # String.replace(old, new)
# text = "I love java"
# print(text.replace("java", "Python"))

# mobile = "Apple"
# print(mobile.replace("Apple", "Samsung"))

# Find()
# Finds the index of the first occurrence of a character or word.

# text = "Machine Learning"
# print(text.find("L"))

# print (text.find("Z")) # if not found it will print -1 as output 



# ## Count ()
# #counts how many times something appears.

# text = "banana"
# print(text.count("a"))


# sentence = "Python Python Java Python"
# print(sentence.count("Python")) 


# text = "     Artificial Intelligence.   "
# print(text.strip())
# print(text.replace("Artificial", "Macine"))
# print(text.find("I"))
# print(text.find("z"))
# print(text.count("i"))

sentence = "Python is easy. python is powerful" # only change first one because it's case sensitive , replace() only replaces text that exactly matched the case
print(sentence.replace("Python", "Java"))
print(sentence.count("Python"))
print(sentence.find("easy"))
text = "   Hello World.     "
print(text.strip())

text = "banana"
print(text.count("a"))
print(text.find("n"))
print(text.replace("na", "NA"))
print(text.upper())

## Split()
### string.split(separtor)

text = "I love python"
print(text.split()) # converts to lists

fruits = "Apple,Mango,Banana" 
print(fruits.split(","))

## Join
## join() does opposite of split().

fruits = ["Apple", "Mango", "Banana"]
print(" ".join(fruits))
print("-".join(fruits))

## Startswith()
## checks wheather a string starts with a specific value.
# Return True or False

text = "Python Programming"
print(text.startswith("Python"))
print(text.startswith("Java"))


## Endswith ()

file = "resume.pdf"
print(file.endswith(".pdf"))





text = "Python,Java,C++"
print(text.split(","))
names = ["Rahul", "Aman", "Riya"]
print("-".join(names))
print("Machine Learning".startswith("Machine"))
print("photo.png".endswith(".png"))