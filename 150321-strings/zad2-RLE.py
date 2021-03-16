'''
 Run-Length Encoding jest prostą metodą kompresji (zob. np. https://pl.wikipedia.
org/wiki/RLE). Polega ona na zamianie każdego znaku na parę (znak, ilość kolejnych powtórzeń). Na
przykład dla listy ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B",
"B", "A", "A", "A", "A", "A", "A", "B"] jej wersją skompresowaną jest lista [("A", 12), ("B",
4), ("A", 6), ("B", 1)].
Napisz funkcję wykonującą kompresję zgodnie z powyższym algorytmem.
Napisz również funkcję wykonującą operację odwrotną (tj. dekompresję).
'''
def RLE_compress(lst):
    result = []
    count = 0
    prev = None
    for c in lst:
        if c != prev:
            if prev is not None:
                result.append((prev, count))
            prev = c
            count = 0
        count = count + 1
    if count > 0:
        result.append((prev, count))
    return result

def RLE_decompress(lst):
    return sum([[c] * count for c, count in lst], [])

def main():
    example = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'A', 'd', 'Z', 'Z', 'Z']
    print(RLE_compress(example))
    print(RLE_decompress(RLE_compress(example)))
    print(RLE_compress(['a','a','a']))

if __name__ == '__main__':
    main()
