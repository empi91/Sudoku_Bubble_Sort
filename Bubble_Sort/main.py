sequences = [
    [],
    [1, 2, 5, 3, 1, 7, 9, 1, 12, 83, 1, 5, 3, 2],
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [2, 2, 2, 2],
    [1, 2],
    [2, 1]
]


def bubble_sort(seq):
    seq_length = len(seq)
    if seq_length == 0:
        return 0
    else:
        is_sorted = False
        while not is_sorted:
            changed = 0
            for i in range(seq_length - 1):
                if seq[i] > seq[i + 1]:
                    temp = seq[i]
                    seq[i] = seq[i + 1]
                    seq[i + 1] = temp
                    changed = 1
            if changed == 0:
                is_sorted = True
    return 0


for sequence in sequences:
    print(f"Sequence before sorting: {sequence}")
    bubble_sort(sequence)
    print(f"Sequence after sorting: {sequence} \n")
