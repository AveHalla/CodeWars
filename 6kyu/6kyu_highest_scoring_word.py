def high(sentence: str) -> str:
    num_arr: list[any] = []
    for word in sentence.split(' '):
        int_num: int = 0
        for letter in list(word):
            int_num += ord(letter) - 96
        num_arr.append(int_num)
    return sentence.split()[num_arr.index(max(num_arr))]
