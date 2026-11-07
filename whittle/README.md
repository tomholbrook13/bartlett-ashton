# Whittle

A daily word builder. Today's 8-letter word is hidden in a bag of its letters.
Make any 3-letter word from the bag, then grow it one letter at a time: keep
every letter, add one more, and rearrange into a new word. Reach eight letters
and you've found the day's word. Most puzzles take two to four minutes.

- `index.html` is the whole game (no build step).
- `puzzles.js` holds 730 days of puzzles starting 2026-11-07, then loops.
- `words.js` is the accepted word list (~23k words, 3 to 8 letters), most
  common first so hints suggest familiar words.
- `generate.py` rebuilds both (`pip install wordfreq english-words`). Every
  answer is a common word with no other 8-letter anagram, reachable from
  3 letters through common words.

A word that is real but can't grow into the day's word is turned away with a
message, so you can never paint yourself into a dead end. Hints show which
letter to add, then a word that works. The shared result has one square per
step: 🟩 first try, 🟨 after a miss, 🟪 with a hint.
