from collections import Counter
import re
from typing import Text
text = """
Counter is a sub-class available inside the dictionary class.
Using the Python Counter tool, you can count the key-value pairs 
in an object. The Counter holds the data in an unordered collection, 
just like hashtable objects. The elements here represent the keys and 
the count as values.
"""
words = re.findall('\w+',text)
print(Counter(words).most_common(10))