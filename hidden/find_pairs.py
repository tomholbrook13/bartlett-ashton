"""Authoring helper: find common word pairs that hide a word across the gap.

    python3 find_pairs.py heron crow wren

For each split of the word (he|ron, her|on, ...) it lists common words that
end with the first part followed by common words that start with the second.
"""
import sys
from wordfreq import top_n_list

words = [w for w in top_n_list("en", 25000) if w.isalpha() and len(w) > 1 or w in ("a", "i")]
for target in sys.argv[1:]:
    print(f"== {target}")
    for i in range(1, len(target)):
        a, b = target[:i], target[i:]
        ends = [w for w in words if w.endswith(a) and w != a][:12]
        starts = [w for w in words if w.startswith(b) and w != b][:12]
        if ends and starts:
            print(f"  {a}|{b}:  {' '.join(ends)}  //  {' '.join(starts)}")
