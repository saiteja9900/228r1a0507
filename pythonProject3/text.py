import re

Text = "ab ab cd ef gh"
b = re.sub ("\d", "#", "Text")
print(b)