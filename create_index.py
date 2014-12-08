#!/usr/bin/env python

import re

from pathlib import Path

TEMPLATE_START = """<!DOCTYPE html>
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


def sub_dirs(path):
    paths = []
    for subs in path.iterdir():
        if subs.is_dir():
            paths.append(subs)
            for subsub in sub_dirs(subs):
                paths.append(subsub)
    return paths


def sub_files(paths):
    html = ''
    for path in paths:
        relevant = []
        for f in path.iterdir():
            if f.is_file() and str(f)[-4:] in ('html', '.wxm'):
                relevant.append(f)
        if len(relevant) > 0:
            html += '            <li>\n'
            html += '                ' + str(path)
            html += '\n                <ul>'
            for r in relevant:
                html += """
                    <li>
                        <a href="{f}">
                            {f}
                        </a>
                    </li>
                """.format(f=str(r))
            html += '</ul>\n'
            html += '            </li>\n'
    return html


if __name__ == '__main__':
    path = Path('.')
    paths = sub_dirs(path)
    #print(paths)
    paths = sorted(paths)
    #print(paths)
    tree = sub_files(paths)
    print(TEMPLATE_START + tree + TEMPLATE_END)
