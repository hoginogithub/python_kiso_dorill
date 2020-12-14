import re
import urllib.request

right_part = urllib.parse.quote('第二次世界大戦')
url = 'https://ja.wikipedia.org/wiki/' + right_part
html = urllib.request.urlopen(url).read()
html = html.decode('utf-8')

year_pattern = r'(?:19|20)[0-9]{2}年'
matches = re.findall(year_pattern, html)

year_counts = dict((year, matches.count(year)) for year in set(matches))

for year in sorted(year_counts, key=year_counts.get, reverse=True):
    print(year, year_counts[year])