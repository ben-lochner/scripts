import string

tbs = str(input("Type a sentence! Any sentence! "))
depunctuate = tbs.translate(str.maketrans("", "", string.punctuation))
filter = depunctuate.upper()
separate = filter.split()
uniqueify = set(separate)
print("Your sentence contains " + str(len(uniqueify)) + " unique words! \n" + str(uniqueify))
