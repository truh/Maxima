#!/usr/bin/env python

import re

from jinja2 import Template
from pathlib import Path

TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <ol>
        {% for mx in mxs %}
            <li>
                <a href="{{ mx }}">
                    {{ mx }}
                </a>
            </li>
        {% endfor %}
    </ol>
    </body>
</html>
"""


def sub_files(path):
    if path.is_dir():
        for new_file in path.iterdir():
            for result in sub_files(new_file):
                yield result
    else:
        yield path


if __name__ == '__main__':
    template = Template(TEMPLATE)
    path = Path('.')
    files = sub_files(path)
    mxs = (p for p in files if str(p)[-5:] == '.html')
    template_stream = template.stream(mxs=mxs)
    template_stream.dump('index.html')
