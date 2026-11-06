# Tumbler

A daily word lock. Five 5-letter words are written top to bottom in a 5x5 grid,
then every row is spun out of place. Turn the rows until each column spells a
word. Most puzzles take two to four minutes.

- `index.html` is the whole game (no build step). Open it in a browser.
- `puzzles.js` holds 730 days of puzzles starting 2026-11-06, then loops.
- `generate.py` rebuilds `puzzles.js` (`pip install wordfreq english-words`).
  Every puzzle is checked so that only one alignment of the rows makes all
  five columns valid words, against a dictionary of ~12k words.

Scoring: each one-letter turn counts. Par is the fewest turns that open the
lock. "Set a row" snaps one row into place and shows as 🟪 in the shared result.
Progress and stats are kept in the browser's localStorage.
