text = "This is a sample string with various separators:sep1, sep2; sep3 - sep4"
separators = [', ', '; ', ' - ',' ']

result = filter(None, [text] + [part.strip() for sep in separators for part in text.split(sep)])
print(list(result))
