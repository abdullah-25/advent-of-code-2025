"""
1) '11-22'
    - val1, val2 = split by - and cast int
2) for i in range (value1, val2+1)
    dump errors ones in sum
"""


def repeating_numbers_check(str_number):
    n = len(str_number)
    return str_number[:n//2] == str_number[n//2:]


def add_invalid_ids(input_ids):
    # input_ids = input_ids[:3]
    sum = 0
    for id in input_ids:
        id1, id2 = id.split('-')
        for i in range(int(id1), int(id2)+1):
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

    print(add_invalid_ids(input_ids))

        