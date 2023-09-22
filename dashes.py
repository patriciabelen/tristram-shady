import re
import text

text = text.text

pattern = r'————|———|——|—'

matches = re.findall(pattern, text)

print(' '.join(matches))
