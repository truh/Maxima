#!/usr/bin/env python

import re

from pathlib import Path

TEMPLATE_START = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <ul>
"""

TEMPLATE_END = """
        </ul>
    </body>
</html>
"""


def sub_files(path):
    if '.git' in str(path): return ''
    if path.is_dir():
        html_dir = ''
        for new_file in path.iterdir():
            html_dir += sub_files(new_file) or ''
        if len(html_dir) > 0:
            return """
            <li>
            {name}
            <ul>
            {tree}
            </ul>
            </li>""".format(path=str(path), name=str(path.parts[-1:]), tree=html_dir)
        return ''
    else:
        if str(path)[-4:] in ('html', '.wxm'):
            return """
            <li>
            <a href="{path}">
            {name}
            </a>
            </li>""".format(path=str(path), name=str(path.parts[-1]))


if __name__ == '__main__':
    path = Path('.')
    print(TEMPLATE_START + sub_files(path) + TEMPLATE_END)
