punctuations= '''!()-{}[]:;"'\,<>./?@#$%^&*'''
mystring = str(input('Enter a string to remove punctuations: '))
no_punct=""
for char in mystring:
    if char not in punctuations:
        no_punct=no_punct+char
print(no_punct)