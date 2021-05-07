from typing import Union
import re
from collections import defaultdict


def read_txt(file: str) -> dict[set]:
    rezult = defaultdict(set)
    with open(file, "r", encoding="utf-8") as f:
        data = set(re.findall(r"[а-яА-Я]{3,}", f.read().lower()))
        for i in data:
            rezult[len(i)].add(i)
    return rezult


def find_word(word: str, text: dict, errors: int) -> Union[list[str], str]:
    """Поиск слов"""
    rez = []
    # for i in text[len(word)]:
    #     if method_hamming_distance(word.lower(), i) < errors:
    #         rez.append(i)
    # for i in text[len(word) - 1]:
    #     if method_hamming_distance(word.lower(), i) < errors:
    #         rez.append(i)
    # for i in text[len(word) + 1]:
    #     if method_hamming_distance(word.lower(), i) < errors:
    #         rez.append(i)
    [rez.append(i) for i in text[len(word)] if method_hamming_distance(word.lower(), i) < errors]
    [rez.append(i) for i in text[len(word)-1] if method_hamming_distance(word.lower(), i) < errors]
    [rez.append(i) for i in text[len(word)+1] if method_hamming_distance(word.lower(), i) < errors]
    if rez:
        return rez
    else:
        return "Нет похожих слов"


def method_hamming_distance(word1: str, word2: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(word1, word2))

def test(actual:list, targets:list):
    x=[1 if actual[index]== targets[index] else 0 for index in range(len(actual))]
    print(x)


file = "Властелин колец.txt"
test_word = "академия"
test_word1=[test_word]
test(find_word(test_word,text,1),test_word1)
