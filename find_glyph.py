#!/usr/bin/env python
from itertools import chain
import sys
import subprocess

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

glyph = int(sys.argv[1], 16)
print(Unicode[glyph])

fc_list = subprocess.check_output(["fc-list"]).decode()

for line in fc_list.split():
    if line[-4:] != "ttf:":
        continue
    path = line[:-1]

    ttf = TTFont(path, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)

    chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)

    exists = glyph in (x[0] for x in chars)

    ttf.close()

    if exists:
        print(path)

