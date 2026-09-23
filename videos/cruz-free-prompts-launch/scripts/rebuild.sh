#!/usr/bin/env bash
# Rebuild frames, captions and index from the authored sources. Run from the project root.
set -euo pipefail
S=~/.claude/skills/product-launch-video/scripts
python3 scripts/build-frames.py
python3 scripts/estimate-word-timings.py > /dev/null   # fetch-sfx rewrites audio_meta.json without words
node $S/captions.mjs build --storyboard ./STORYBOARD.md --audio-meta ./audio_meta.json --hyperframes . --out ./caption_groups.json
python3 scripts/fix-caption-fonts.py
node $S/assemble-index.mjs --storyboard ./STORYBOARD.md --hyperframes .
# mark the caption host so Studio groups it on the caption track
sed -i 's/id="el-captions"$/id="el-captions"\n        data-track-kind="captions"/' index.html
node $S/transitions.mjs inject --storyboard ./STORYBOARD.md --hyperframes .
node $S/transitions.mjs verify --storyboard ./STORYBOARD.md --index ./index.html
# GSAP from the project (the CDN is not reachable from every render machine)
sed -i 's#https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js#assets/vendor/gsap-3.14.2.min.js#g' index.html compositions/captions.html
# base ground = brand near-black (the assembler maps frame.md's `cream` key, which is text white here)
sed -i 's/        background: #FFFFFF;/        background: #0A0909;/' index.html
