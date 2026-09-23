#!/usr/bin/env python3
"""Wrap each hand-authored frame body (scripts/frames/<id>.html: <style>, markup, <script>)
in the shared sub-composition shell: GSAP load, local @font-face, #root + ground clip.
Run from the project root: python3 scripts/build-frames.py"""
import glob, os, re

FONTS = "".join(
    f"""
      @font-face {{ font-family: "Montserrat"; font-weight: {w}; font-style: normal;
        src: url("assets/fonts/montserrat-latin-{w}-normal.woff2") format("woff2"); }}"""
    for w in (400, 600, 700, 800, 900)
) + "".join(
    f"""
      @font-face {{ font-family: "IBM Plex Mono"; font-weight: {w}; font-style: normal;
        src: url("assets/fonts/ibm-plex-mono-latin-{w}-normal.woff2") format("woff2"); }}"""
    for w in (500, 700)
)

SHELL = """<template>
  <script src="assets/vendor/gsap-3.14.2.min.js"></script>
  <style>{fonts}
      #root {{
        position: absolute;
        inset: 0;
        overflow: hidden;
        color: #ffffff;
        font-family: "Montserrat", sans-serif;
      }}
      #root .clip {{ position: absolute; inset: 0; }}
      #{gid} {{ background: #0a0909; }}
      #root .mono {{ font-family: "IBM Plex Mono", monospace; font-weight: 500; text-transform: uppercase; letter-spacing: 0.14em; }}
{style}
  </style>
  <div id="root" data-composition-id="{id}" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
    <div id="{gid}" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></div>
{markup}
  </div>
  <script>
    (function () {{
      const ID = "{id}";
      const DUR = {dur};
      const tl = gsap.timeline({{ paused: true }});
{script}
      tl.set({{}}, {{}}, DUR);
      window.__timelines[ID] = tl;
    }})();
  </script>
</template>
"""

for src in sorted(glob.glob("scripts/frames/*.html")):
    fid = os.path.basename(src)[:-5]
    body = open(src).read()
    dur = re.search(r"<!--\s*duration:\s*([\d.]+)\s*-->", body).group(1)
    style = re.search(r"<style>([\s\S]*?)</style>", body).group(1).rstrip()
    script = re.search(r"<script>([\s\S]*?)</script>", body).group(1).rstrip()
    markup = re.sub(r"<!--\s*duration:[^>]*-->|<style>[\s\S]*?</style>|<script>[\s\S]*?</script>", "", body).strip("\n")
    out = SHELL.format(fonts=FONTS, id=fid, gid="f" + fid[:2] + "-ground", dur=dur, style=style, markup=markup, script=script)
    open(f"compositions/frames/{fid}.html", "w").write(out)
    print("wrote", fid, dur)
