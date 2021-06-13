from collections import Counter
import re
from typing import Text
text = """
Loki is an American television series created by Michael Waldron for the streaming service Disney+, 
featuring the Marvel Comics character of the same name.
Set in the Marvel Cinematic Universe (MCU), it shares continuity with the films of the franchise and takes place after the events of the film Avengers: Endgame (2019), in which an alternate version of Loki created a new timeline.
Loki is produced by Marvel Studios, with Waldron serving as head writer and Kate Herron directing for the first season. 
"""
words = re.findall('\w+',text)
print(Counter(words).most_common(10))