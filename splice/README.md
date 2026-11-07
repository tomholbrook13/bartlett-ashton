# Splice

A daily untangling puzzle. Each strip is two words woven together, with each
word's letters kept in order (FULL + FARM becomes FFUARLML). Tap letters to
lift them into the pink lane above or drop them into the blue lane below until
both lanes spell words. Three
strips a day: 4 + 4, 5 + 5 and 6 + 6 letters.

- `index.html` is the whole game (no build step).
- `puzzles.js` holds 730 days starting 2026-11-07, then loops.
- `generate.py` rebuilds it (`pip install wordfreq english-words`). A strip is
  only kept if exactly one way of pulling its letters apart gives two words in
  a broad dictionary, so a solution can't be "right but rejected".

Hints place one correct letter at a time in the first unsolved strip, matching
whichever colour you've already given each word. The shared result has a 🟩
for each strip solved alone and a 🟪 for each one where a hint was used.
