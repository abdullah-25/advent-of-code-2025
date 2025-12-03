def max_joltage(banks):
    banks[0]
    sum = 0
    for bank in banks:
        print('bank', bank)
        largest = int(bank[0])
        for i, joltage in enumerate(bank):
            if i is not len(bank) - 1:
                if int(joltage) > largest:
                    largest = int(joltage)

        index_largest = (bank.find(str(largest)))
        print(index_largest)
        second_largest = int(bank[index_largest+1])
        for j in range(index_largest+1, len(bank)):
            if int(bank[j]) >= second_largest:
                second_largest = int(bank[j])
        curr_sum = str(largest) + str(second_largest)
        sum += int(curr_sum)
        print(sum)

    return sum


if __name__ == '__main__':
    banks = []
    with open('test.txt', 'r', encoding='UTF8') as f:
        for line in f:
            banks.append(line.strip())
    print(max_joltage(banks))
