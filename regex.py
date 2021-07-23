import re

# text = "you can call me at 123-234-4567"
# pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# result = re.search(pattern, text)
# print(result)
# print(result.span())
# print(result.start())
# print(result.group())

# text = "you can call me at 123-234-4567 or 333-333-3333"
# pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# # result = re.findall(pattern, text)
# # print(result)
#
# for item in re.finditer(pattern, text):
#     print(item)
#     print(item.start())

# Character identifier
# \d -> digit, \w -> alphanumeric D_og-1 \w\w\w\w-\w
# \s -> space
# \D -> non-digit XYZ \D\D\D
# \W -> non-alphanumeric *+-)=


# Quantifier
# + (Occurs one or more time)
# * (Occurs zero or more time)
# ? (once or more)
# {3} exactly 3 times

# text = "you can call me at 123-234-4567"
# pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# result = re.search(pattern, text)
# print(result)
# print(result.span())
# print(result.group(1))

# or (|) operator
# text = "I have Tesla car"
# pattern = re.compile(r'Tesla | Honda')
# result = re.search(pattern, text)
# print(result)

# . (dot) operator
# text = "It is best to take rest during fest"
# pattern = re.compile(r'.est')
# result = re.findall(pattern, text)
# print(result)

# ^ starts with
# text = 'date 1/1/2021'
# result = re.findall("^\d", text)
# print(result)

# $ ends with
# text = '1/1/2021 date'
# result = re.findall("\d$", text)
# print(result)


# [] to exclude data
text = "This is sanjeev! the founder of interviewbox.tech?"
pattern = re.compile(r'[^!?]+')
result = re.findall(pattern, text)
print(result)
print("".join(result))

