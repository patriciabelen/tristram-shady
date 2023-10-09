import re
import text

text = text.shandy

pattern = r'————|———|——|—'

matches = re.findall(pattern, text)

print(' '.join(matches))
