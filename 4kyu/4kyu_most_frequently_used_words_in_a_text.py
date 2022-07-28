from collections import Counter
import re


def top_3_words(text: str) -> list[str]:
    c: Counter = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [i for i, _ in c.most_common(3)]
