import re
# module used for regular expression

print(r"\t")
# when r is placed the content inside the " " are considered as raw string and no escape sequence in used

pattern = re.compile(r"abc")
# creating a regular expression

text_to_search = """hello everyone abc this is nice abc"""

matches = pattern.finditer(text_to_search)
# finding matches in the text with pattern
# returns the position of the match

for m in matches:
    print(m.span())