# Hidden

A daily hidden-word hunt. A short paragraph hides six to eight words on a
theme, each running across a gap between words ("slo**w l**earners" hides
OWL). Drag across the letters, or tap the first and last letter, to mark one.

- `index.html` is the whole game (no build step).
- `puzzles.json` is where puzzles are written: a theme, a paragraph, and the
  hidden words. Puzzle n is played on 2026-11-07 + n days, looping when the
  list runs out.
- `build.py` checks every puzzle and writes `puzzles.js`. Each word must run
  across a gap and must not appear as a plain word. It also warns if another
  word from the theme happens to hide across a gap, so players never find a
  "right" answer that doesn't count.
- `find_pairs.py` helps write new ones: `python3 find_pairs.py heron` lists
  common word pairs that hide HERON across the gap.

To add puzzles: append to `puzzles.json`, run `python3 build.py`, and update
`length` for Hidden in the root `index.html` so the menu shows the right number.
