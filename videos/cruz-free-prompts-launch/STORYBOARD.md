---
format: 1080x1920
duration: 30s
message: "Cruz Creative's 15 client-tested AI prompts are free — stop making content that looks AI-generated"
arc: PAS with negative contrast — hook → contrast (value) → product intro → features → proof → CTA
audience: small-business owners, marketers and creators on Reels / TikTok / Shorts who already use AI for content
mode: autonomous
music: punchy confident modern electronic, social-promo energy, clean driving beat
---

## Video direction

- **Canvas:** 1080×1920 vertical. All content planned into the top ~83% — the bottom ~17% is the caption band (captions on). Side margins follow frame.md `pad-x`.
- **Palette system (frame.md, dark register throughout):** ground `ink-black` #0A0909; text `cream` #FFFFFF, secondary `cream-muted` #CCCCCC; the ONLY accent is brand mint `fire-orange` #A5F0B1 (one mint clause/word per frame, kickers, the CTA button, the 50+ numeral). Card surfaces #141212 with 1px `border-dark` hairlines. The brand danger tone #F0A5A5 appears ONLY on the one negative label (Frame 2 "looks like everyone else") uses the site's danger tone only there. No gradients as grounds, no shadows, 0 radius except pills/CTA (the site's own rounded button is allowed on the CTA only).
- **Type:** display Montserrat 900/800 lowercase, negative-tracked (frame.md display/h1/h2); mono chrome IBM Plex Mono uppercase tracked (kickers, labels, the URL tag line); body Montserrat 400–600. Local @font-face from `assets/fonts/`.
- **Motion grammar:** smooth long-tail settles (`power3` default, `expo.out` on fast arrivals); overshoot only for the Frame 2 badges and the Frame 6 press. Kinetic swaps are hard cuts (`discrete-text-sequence`). Every piece reveals on its spoken cue (word timings in audio_meta.json are phrase-accurate) — nothing enters before the VO names it; the back half of every frame carries a reveal. Holds are still; the only sanctioned aliveness is subtle jitter (`sine-wave-loop`, low amplitude) on one held hero.
- **Rhythm / held frames:** F1 and F2 are fast (punchy hook + proof); F3 is the breather/title card (near-still, one move per card); F4 accumulates; F5 is a single-number climax; F6 resolves and holds the URL to the last frame.
- **Negative list:** no purple/blue AI gradients, no bokeh, no floating decorative blobs, no browser chrome/nav, no fake logos (use the captured CRUZ CREATIVE wordmark SVG as-is), no uppercase display, no second accent hue. Forbid both motion failure modes — slideshow (front-load then freeze) and screensaver (many elements drifting independently); no lazy breathing, no back-half slow pan/push; no `repeat:-1`, no randomness.

## Frame 1 — Looks like AI

- scene: The viewer's own complaint slams in as giant lowercase type — "your AI content" → "looks like AI content", generic AI posters flicker behind the swap
- voiceover: "Your AI content… looks like AI content."
- duration: 3.349s
- transition_in: cut
- status: animated
- src: compositions/frames/01-looks-like-ai.html
- type: hook
- persuasion: Pain validation
- beat: frustration + recognition
- blueprint: kinetic-type-beats
- asset_candidates: assets/generic-ai-poster-for-a-gym-stock-templa.webp — generic AI gym poster, loud stock-template look; assets/generic-ai-poster-for-a-burger-restauran.webp — generic AI burger poster, cartoon mascot; assets/generic-ai-poster-for-a-bike-rental-stoc.webp — generic AI bike-rental poster

narrativeRole: stops the scroll by naming the exact embarrassment the viewer already feels (lifted from the site's own meta line).
keyMessage: everyone can tell your content was made by AI.

- focal: assets/generic-ai-poster-for-a-gym-stock-templa.webp
- roles: generic gym poster = background (full-bleed, dim ~35%, final flicker state) · generic burger poster = background (flicker) · generic bike poster = background (flicker)
- sfx: glitch-1, impact-bass-1

Adapt (kinetic-type-beats, flash sub-shape): keep the in-place token swap as the signature; add a background poster flicker that hard-cuts on each word so the "AI look" is literally behind the words.
Scene 1 (0.0–1.6s): black field; "your" / "ai" / "content…" FLASH in one word per cue (0.05 / 0.40 / 0.62s) as giant lowercase display stacked left-aligned in the upper-middle (~65% frame width), white. On each word a different generic AI poster hard-cuts in full-bleed behind it at ~35% opacity (bike → burger → gym) — hard-cut / flash word-swap → `discrete-text-sequence`.
Scene 2 (1.6–2.6s): the in-place swap (signature): "your" hard-cuts to "looks like" at 1.66s while "ai content" holds its position; at 2.34s "ai content." re-inks to mint as the VO repeats it — the line now reads "looks like / ai content." Poster flicker stops on the gym poster. `discrete-text-sequence` + one hard color cut.
Scene 3 (2.6–3.35s): held read; subtle jitter on the mint "ai content." only (`sine-wave-loop`, low amplitude). Exit = harness zoom-through.

## Frame 2 — Same AI, better prompt

- scene: Split screen — generic AI gym poster (labelled "generic prompt · looks like everyone else") vs the on-brand gym poster ("our prompt · looks like your brand"); the payoff half wins
- voiceover: "Same AI. Better prompt. Now it looks like your brand."
- duration: 3.563s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/02-same-ai-better-prompt.html
- type: feature_showcase
- persuasion: Negative contrast / show-don't-tell proof
- beat: curiosity → clarity
- blueprint: comparison-split
- asset_candidates: assets/generic-ai-poster-for-a-gym-stock-templa.webp — generic AI gym poster ("any AI tool — generic prompt"); assets/on-brand-ai-poster-for-a-gym-matches-the.webp — same gym poster made with the Cruz prompt, on-brand

narrativeRole: lands the value claim in beat 2 — the difference is the prompt, and the proof is on screen (the site's own before/after).
keyMessage: the prompt, not the tool, makes it look like your brand.

- focal: assets/on-brand-ai-poster-for-a-gym-matches-the.webp
- roles: generic gym poster = supporting (left card) · on-brand gym poster = cutout (right card, the payoff)
- sfx: whoosh-short, pop

Adapt (comparison-split): keep the mirrored split-tilt book-open entry and inner-edge pill badges; vertical canvas → two portrait poster cards side-by-side in the middle band, title above as a stacked two-line headline built per VO phrase.
Scene 1 (0.0–1.1s): headline line 1 "same ai." slides down into the upper third (h1, white, left-aligned); simultaneously the LEFT card (generic gym poster, mono label above "ANY AI TOOL — GENERIC PROMPT") enters from the left wing with a rightward-facing rotateY tilt → `split-tilt-cards`. Right half empty.
Scene 2 (1.1–2.0s): as the VO says "better prompt", line 2 "better prompt." appends under line 1 in mint and the RIGHT card (on-brand gym poster, label "CRUZ CREATIVE — OUR PROMPT", 1px mint border) enters from the right wing with the mirrored tilt; both settle facing each other like an opened book. Split-screen, two equal cards ~44% width each, 3 layers (ground / cards / labels).
Scene 3 (2.0–3.56s): badges punctuate on the VO: at ~2.1s a muted-danger pill "looks like everyone else" pops at the left card's inner-bottom edge and the left card dims to ~55%; at ~2.9s ("your brand") a mint pill "looks like your brand" spring-pops at the right card's inner edge (the lone overshoot) → `spring-pop-entrance`. Hold still.

## Frame 3 — 15 prompts, free

- scene: The CRUZ CREATIVE wordmark pops over the moody hero footage, then "15 client-tested prompts" and a mint "free" land beneath it
- voiceover: "Cruz Creative just made its fifteen client-tested prompts… free."
- duration: 4.523s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/03-fifteen-free.html
- type: product_intro
- persuasion: Risk reversal (free) + authority by association (client-tested)
- beat: surprise → desire
- blueprint: titlecard-reveal
- asset_candidates: assets/logo-8fccc9a2.svg — CRUZ CREATIVE boxed wordmark, mint outline on near-black; assets/hero-bg-poster.jpg — still of the site hero video: moody silhouette walking a dark wet street (used as a still so it travels with the frame transitions)

narrativeRole: names the offer — who made it, how many, and the price (nothing).
keyMessage: 15 client-tested prompts, free.

- focal: assets/logo-8fccc9a2.svg
- roles: CRUZ CREATIVE wordmark = cutout (hero mark) · hero-bg-poster.jpg = background (full-bleed, center-cropped to 9:16, dim ~35%)
- sfx: whoosh-cinematic, impact-bass-2

Adapt (titlecard-reveal, card-chain variant): keep one restrained move per card and the still hold; the chain is wordmark → "15 client-tested prompts" → "free." stacked in one column rather than replacing each other, over the site's own hero footage.
Scene 1 (0.0–0.9s): the hero still (silhouette on the dark street) sits full-bleed, dimmed, with one slow push-in across the frame (the single camera move); the CRUZ CREATIVE wordmark reveals centered in the upper third with ONE slide-up crossfade as the VO says the name (~70% frame width). Centered template.
Scene 2 (0.9–3.8s): held while "just made its" is spoken; at 1.84s ("fifteen") a giant mint "15" (display numeral) slides up under the wordmark, and at 2.03s the h2 "client-tested prompts" slides up beside/under it in white — per-phrase reveal (`dynamic-content-sequencing`), smooth settle, then still.
Scene 3 (3.8–4.52s): on the VO's "free." (3.95s) a mint block with ink text "free." hard-cuts in below the stack (orange-register chip, the frame's one declaration) → `discrete-text-sequence`; holds still to the cut.

## Frame 4 — Built for what you make

- scene: Three cards stack in, one per prompt family — on-brand graphics, a brand voice that sounds like you, product shots — each with its on-brand poster/line from the site
- voiceover: "On-brand graphics. A voice that sounds like you. Product shots that save you thousands."
- duration: 5.867s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/04-built-for-you.html
- type: benefit_highlight
- persuasion: Rule of three / feature-to-benefit translation
- beat: aspiration + ease
- blueprint: grid-card-assemble
- asset_candidates: assets/on-brand-3.webp — on-brand burger restaurant poster (graphics); assets/same-ai-better-prompt-completely-differe.webp — on-brand bike rental poster with realistic product photo (product shots); assets/on-brand-ai-poster-for-a-gym-matches-the.webp — on-brand gym poster

narrativeRole: the evidence — what's inside, translated into what each prompt family gets the viewer.
keyMessage: graphics, voice and product shots — the content you actually create.

- focal: assets/on-brand-3.webp
- roles: on-brand burger poster = supporting (card 1 thumbnail) · on-brand gym poster = supporting (card 1 thumbnail, fanned behind the burger) · on-brand bike poster = supporting (card 3 thumbnail, the realistic product shot)
- sfx: click-soft, click-soft, click-soft

Adapt (grid-card-assemble, stacked-list variant): keep the self-assembling list; items arrive one per spoken cue (not a quick cascade), three full-width cards stacked in the middle band.
Scene 1 (0.0–1.6s): mono kicker "WHAT'S INSIDE · 15 PROMPTS" and a 36×2 mint rule stub sit top-left; card 01 rises into slot 1 at 0.05s — #141212 surface with 1px hairline, left: fanned on-brand burger + gym poster thumbnails; right: mono "01" + h3 "on-brand graphics" → `waterfall-entry`.
Scene 2 (1.6–3.5s): card 02 rises into slot 2 at 1.63s ("a voice that sounds like you") — no image; instead a mono code snippet from Prompt #7: "short, confident sentences, zero corporate jargon" in a quiet code block, plus mono "02" + h3 "a voice that sounds like you".
Scene 3 (3.5–5.87s): card 03 rises into slot 3 at 3.59s — left: on-brand bike product-shot poster thumbnail; right: mono "03" + h3 "product shots that save you thousands"; at 5.22s the word "thousands" glows mint on its cue → `asr-keyword-glow`. List holds still to the cut (no float).

## Frame 5 — Proof, not promises

- scene: "50+" counts up in giant mint type — "businesses already using these prompts" — with the Halcyon client logo and a short slice of Dolores Phillips' quote
- voiceover: "Built from real client work — already used by fifty-plus businesses."
- duration: 4.629s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-proof.html
- type: social_proof
- persuasion: Social proof / statistical proof
- beat: skepticism → trust
- blueprint: dataviz-countup
- asset_candidates: assets/halcyon-group.webp — Halcyon Group client logo (quoted client); assets/lake-company.webp — Lake Company client logo

narrativeRole: removes the "free = junk" doubt with the site's own proof (50+ businesses, the Halcyon testimonial).
keyMessage: real brands already use these.

- focal: assets/halcyon-group.webp
- roles: Halcyon Group logo = supporting (attribution on the quote card, shown as-is on a white tile) · Lake Company logo = supporting (second client tile in the logo row)
- sfx: riser, impact-bass-1

Adapt (dataviz-countup, single-instrument cold-open): one hero metric instead of 2–3 instruments; keep the count-up signature and a single short push-in that locks as the number lands (no push-through to a second instrument).
Scene 1 (0.0–2.1s): mono kicker "PROOF, NOT PROMISES" top-left; a quote card rises in the upper third as the VO says "built from real client work": mint ★★★★★, quote slice "our open rate actually went up. feels like us, not like a chatbot." (body, white), attribution "DOLORES PHILLIPS · PROJECT DIRECTOR, HALCYON" in mono with the Halcyon logo tile → `waterfall-entry`.
Scene 2 (2.1–3.5s): on "already used by" the giant mint numeral appears in the center band and counts 0 → 50 with its scale growing with the value, landing "50+" exactly at 3.42s → `counting-dynamic-scale`; one short camera push-in on the numeral runs during the count and locks at the land → `multi-phase-camera`.
Scene 3 (3.5–4.63s): on "businesses" (3.72s) the h3 "businesses already using these prompts" slides up under the numeral and a small logo row (Halcyon, Lake Company tiles) settles beneath it; hold still.

## Frame 6 — Grab them free

- scene: The wordmark condenses into the mint "Send me the 15 prompts →" button, a cursor clicks it, and the URL freeprompts.cruzcreative.net holds to the end
- voiceover: "Grab all fifteen, free — at freeprompts dot cruzcreative dot net."
- duration: 4.715s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/06-cta.html
- type: cta
- persuasion: Friction reduction (free, instant, no spam)
- beat: urgency-to-act
- blueprint: cta-morph-press
- asset_candidates: assets/logo-8fccc9a2.svg — CRUZ CREATIVE boxed wordmark

narrativeRole: converts — one action, one URL, the site's own CTA button.
keyMessage: freeprompts.cruzcreative.net — free, instant.

- focal: assets/logo-8fccc9a2.svg
- roles: CRUZ CREATIVE wordmark = cutout (hero mark that condenses into the CTA)
- sfx: whoosh-short, click

Reproduce (cta-morph-press): hero mark and CTA share one center; the morph is the signature.
Scene 1 (0.0–1.1s): the CRUZ CREATIVE wordmark holds dead-center in the upper-middle; h1 "grab all 15." reveals above it per word on the VO (0.05s) → `dynamic-content-sequencing`. Centered template.
Scene 2 (1.1–2.0s): on "free" (1.17s) the headline appends a mint "free." and the wordmark CONDENSES at the same center into the site's mint CTA button "Send me the 15 prompts →" (ink text) — the mark shrink-fades exactly as the button scales up in place → `scale-swap-transition` (smooth, no overshoot on the morph).
Scene 3 (2.0–3.0s): on "at freeprompts…" the URL "freeprompts.cruzcreative.net" rises under the button in bold white (h3 scale), and a cursor arrives from lower-right on a decelerating path, landing slightly off the button's center.
Scene 4 (3.0–4.72s): the cursor clicks at ~3.1s — cursor + button compress together and release with a mint ripple → `cursor-click-ripple` + `press-release-spring`; mono line "FREE FOREVER · INSTANT DOWNLOAD · NO SPAM" settles under the URL; holds still to the end (final frame — no exit move).
