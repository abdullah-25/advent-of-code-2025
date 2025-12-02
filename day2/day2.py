def add_invalid_ids(ids):
    pass


if __name__ == "__main__":
    input_ids = []
    with open('sample_test.txt', 'r', encoding='UTF8') as f:
        input = [line.strip().split(',') for line in f]
        for data in input:
            for item in data:
                if item != '':
                    input_ids.append(item)

    print(input_ids)

        