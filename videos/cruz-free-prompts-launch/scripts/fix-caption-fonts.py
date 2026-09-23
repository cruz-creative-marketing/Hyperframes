#!/usr/bin/env python3
"""Inject local Montserrat @font-face rules into compositions/captions.html.

Works around the product-launch skill's captured-fonts helper: the capture's CSS names
Montserrat without a downloadable source, so captions.mjs treats the family as "captured"
and skips the staged assets/fonts files, leaving the caption track with no @font-face.
Idempotent. Run after every `captions.mjs build`: python3 scripts/fix-caption-fonts.py"""
p = "compositions/captions.html"
s = open(p).read()
marker = "/* local-font-faces */"
if marker not in s:
    faces = "".join(
        f'\n      @font-face {{ font-family: "Montserrat"; font-weight: {w}; font-style: normal; font-display: block;'
        f' src: url("assets/fonts/montserrat-latin-{w}-normal.woff2") format("woff2"); }}'
        for w in (400, 600, 700, 800, 900)
    )
    s = s.replace("<style data-brand-tokens>", "<style data-brand-tokens>\n      " + marker + faces, 1)
    open(p, "w").write(s)
    print("injected Montserrat @font-face into", p)
else:
    print("already present")
