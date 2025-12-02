"""
1) '11-22'
    - val1, val2 = split by - and cast int
2) for i in range (value1, val2+1)
    dump errors ones in sum
"""


def repeating_numbers_check(str_number):
    """Check if number is made of some sequence repeated at least twice.
    Examples: 12341234 (1234 twice), 123123123 (123 three times), 1212 (12 twice)
    """
    n = len(str_number)

    # Pattern must repeat at least twice, so max length is n//2
    for pattern_len in range(1, n // 2 + 1):
        # Check if the string length is divisible by pattern length
        print(pattern_len)
        if n % pattern_len == 0:
            pattern = str_number[:pattern_len]
            # Check if repeating this pattern gives us the whole string
            if pattern * (n // pattern_len) == str_number:
                return True

    return False



def add_invalid_ids(input_ids):
    # input_ids = input_ids[:3]
    sum = 0
    for id in input_ids:
        id1, id2 = id.split('-')
        for i in range(int(id1), int(id2)+1):
            if str(i) == '101':
                continue
            if repeating_numbers_check(str(i)):
                print(f'invalid id: {i}')
                sum += i
    return sum


if __name__ == "__main__":
    input_ids = []
    with open('test.txt', 'r', encoding='UTF8') as f:
        input = [line.strip().split(',') for line in f]
        for data in input:
            for item in data:
                if item != '':
                    input_ids.append(item)
    print(repeating_numbers_check('565656'))
    # print(add_invalid_ids(input_ids))

