import re

def clean_titles(html_input):
    title_pattern = r'<p .*class=".*title-section.*"[^>]*>(.*)</p>'
    return re.sub(title_pattern, '<h1>\\1</h1>', html_input)

html_text = '<p class="title title-section">Hello World</p>'

print(clean_titles(html_text))