from urllib import request
from nltk import word_tokenize

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)

print(f"The length of the text is {len(tokens)}")

assert True

