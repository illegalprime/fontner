# Usage

Find which fonts on your system support a glyph.
For the glyph `0xFF03` run:

```
./find_glyph.py ff03
```

# Install

To install python & needed packages just use a [nix](https://nixos.org/nix/) shell:

```
nix-shell --command './find_glyph.py ff03'
```

You can also use `pip` which is less cool: `pip install FontTools`

