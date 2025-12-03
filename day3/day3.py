def max_joltage(banks):
    pass


if __name__ == '__main__':
    banks = []
    with open('sample_test.txt', 'r', encoding='UTF8') as f:
        for line in f:
            banks.append(line.strip())
    print(banks)
