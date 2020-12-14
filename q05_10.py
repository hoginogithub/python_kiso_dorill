import re

class MarkdownParseError(Exception):
    pass

def parse_markdown_link(link):
    link_pattern = r'\[(?P<text>.+)\]' \
        r'\((?P<url>[^ ]+)' \
        r'( \"(?P<title>.+)\")?\)'
    
    m = re.match(link_pattern, link)

    if m is not None:
        return [m.group('text'), m.group('url'), m.group('title')]
    else:
        raise MarkdownParseError("Invalid markdown link")

link_str = '[表示されるテキスト。[リンク]の情報](http://www.myurl.com "私の"任意"タイトル")'

print(parse_markdown_link(link_str))

