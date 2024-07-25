# REGULAR EXPRESSION
# 1. INTRODUCTION TO REGEX
# 2. SIMPLE CHARACTERS MATCHES
# 3. CHARACTER CLASSES
# 4. SPECIAL CHARACTERS
# 5. QUANTIFIERS
# 6. SUBSTITUTING



import re
# 2 SIMPLE CHARACTERS MATCHING

text = 'cat bat mat rat'
pattern = 'cat'

# re.findall(pattern, text)
output =re.findall (pattern, text)
print(output)

text_1 = 'cat bat mat rat'
output_1=re.findall(pattern, text_1)
print(output_1)

my_text = 'The dog barks loudly'
pattern = 'dog'
print(re.findall(pattern, my_text))

# 3. CHARACTER CLASSES
text = 'abc 123'
pattern = '\d'
print(re.findall(pattern, my_text))



text ='333af3b4c'
pattern= '\d'
print(re.findall(pattern, text))


text = 'abc def ghi jkl'
pattern= r'[def]' # for extracting the string put outputting it individually
print(re.findall(pattern, text))

text='Hello World! abc DEF 123'
pattern=r'[a-z]' # for extracting the lowercase letters
print(re.findall(pattern, text))

text='Hello World! abc DEF 123'
pattern=r'[a-z]' # for extracting the uppercase letters
print(re.findall(pattern, text))

text = 'abc def ghi jkl'
pattern=r'[^def]'
print(re.findall(pattern, text))

text = 'abc \t def \t'
pattern=r'[^def]'
print(re.findall(pattern, text))

#RECAP THISS!!!
text = 'abc \t def \t'
pattern=r'[^def]' #Extract all excluding the one in \\ using \t
print(re.findall(pattern, text))

text= 'Hello World 1234'
pattern= r'[a-zA-Z0-9]' #Extracting just the symbols alone
print(re.findall(pattern, text))

text ='Hello World 1234 ^&**%$'
pattern= r'\s' #extracting the spaces
print(re.findall(pattern, text))

text = 'Hello World 1234 ^&**%$'
pattern= r'[^]'

#4. SPECIAL CHARACTERS
text = 'hello world hallo'
pattern = r'h.llo'
print(re.findall(pattern, text))

text = 'hello world hallo'
pattern = r'h.llo' #starting with h and end with llo
print(re.findall(pattern, text))

text = 'hello world hallo heeelo'
pattern = r'h*llo' 
print(re.findall(pattern, text))

text = 'dello world hallo heello'
pattern = r'h.*llo'
print(re.findall(pattern, text))

text = 'dello world falld heello'
pattern = r'h.llo'
print(re.findall(pattern, text))





























text = 'dello world falld heello'
pattern = r'.*ld'
print(re.findall(pattern, text))



# 5- QUANTIFIERS
text= 'a aa aaa aaaa aaaaa'
pattern= r'a*' #extract for matches of 0 a's or more
print(re.findall(pattern, text))

text= 'a aa aaa aaaa aaaaa'
pattern= r'a+' #extract for matches of 0 a's or more
print(re.findall(pattern, text))

text= 'a aa aaa aaaa aaaaa'
pattern=r'a{3}' # extract for three occurances
print(re.findall(pattern, text))

text= 'a aa aaa aaaa aaaaa'
pattern=r'a{6}' # extract for three occurances
print(re.findall(pattern, text))

text= 'a aa aaa aaaa aaaaa'
pattern=r'a{3}' # pulling out for three occurances of a's
print(re.findall(pattern, text))


#6- SUBSTITUTING

text= 'Daniel and Marvelous are friends'
pattern= 'friends' #word we are trying to substitute
output = re.sub(pattern, 'opps', text)
print(output)

#7 -COMPILING REGULAR EXPRESSION

text = 'There are 10 apples and 20 oranges'
pattern = '[0-9]'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = '\d'
print(re.findall(pattern, text))

daniel_text = 'There are 10 apples, 30 mangoes and 20 oranges'


pattern= re.compile('\d+')
daniel_text = 'There are 10 apples, 30 mangoes and 20 oranges'
output=pattern.findall(daniel_text)
print(output)

text = 'There are 10 apples, 30 mangoes and 20 oranges'
pattern = '[\w]+'#  to extract letters and numbers
print(re.findall(pattern, text))

#8- Split function

text = 'Split this text for me right away'
pattern=r'\s+' # split with respect to white spaces found
output = re.split(pattern, text)
print(output)

