import re

# MetaCharacters (Need to be escaped): . ^ $ * + ? { } [ ] \ | ( )
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
coreyms.com
321--555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

King
ping
ding 
'''

urls='''

https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern=re.compile(r'https?://(www\.)?\w+\.\w+') # normal way of writing 

# making them in to groups(r'https?://(www\.)?(\w+))(\.\w+)')


matches= pattern.finditer(urls)  # passing the content to find the specific pattern

for match in matches:
    print(match)