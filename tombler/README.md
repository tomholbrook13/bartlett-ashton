# Tombler

A daily word lock. Five 5-letter words are hidden in five rings of letters.
Turn the rows to spell any one of them down a column, taking one letter from
each row. That column locks and the leftover letters re-spin onto smaller
rings (5, then 4, 3 and 2 letters), so every word has to be found on its own.
The last word drops in by itself. Most puzzles take two to four minutes.

- `index.html` is the whole game (no build step). Open it in a browser.
- `words.js` is the dictionary used to tell players when they've spelled a real
  word that isn't one of the day's answers.
- `puzzles.js` holds 730 days of puzzles starting 2026-11-06, then loops.
- `generate.py` rebuilds `puzzles.js` (`pip install wordfreq english-words`).
  Every puzzle is checked so that only one alignment of the rows makes all
  five columns valid words, against a dictionary of ~12k words.

Scoring: each one-letter turn counts. Par is the sum, over each stage, of the
fewest turns needed to spell any remaining word from where the rings landed.
Re-spins are seeded, so the same moves give every player the same rings.
"Set a row" turns one row to where the nearest word needs it; a stage where it
was used shows as 🟪 in the shared result.
Progress and stats are kept in the browser's localStorage.

## Hosting

`.github/workflows/pages.yml` publishes this folder to GitHub Pages on every
push to `main` that touches `tombler/`. One-time setup: in the repository's
Settings → Pages, set **Source** to **GitHub Actions**.
