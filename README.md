# Usage

Find which fonts on your system support a glyph.
For the glyph `0xFF03` run:

```
./find_glyph.py ff03
```

Or specify your own files!

```
./find_glyph.py ff03 <ttf path 1> <ttf path 2> ...
```

You should see this (meaning `unifont` supports this glyph):

```
$ ./find_glyph.py ff03 
FULLWIDTH NUMBER SIGN
/nix/store/adznf6h69af320wpmlhx525l6hfizaqw-unifont-11.0.02/share/fonts/truetype/unifont.ttf
```

# Install

To install python & needed packages just use a [nix](https://nixos.org/nix/) shell:

```
nix-shell --command './find_glyph.py ff03'
```

You can also use `pip` which is less cool: `pip install FontTools`

