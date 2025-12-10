def math_homework(input):
    res = int()
    ops = input[-1]

    for j in range(len(input[0])):
        add, mul = int(), int()

        for i in range(len(input)-1):
            print(input[i][j])
            print(ops[j])
            if ops[j] == "+":
                add += int(input[i][j])
            else:
                if int(input[i][j]) == 0:
                    mul = 0
                    break
                if mul == 0:
                    mul = 1
                mul *= int(input[i][j])
        
        res += add + mul

    return res






if __name__ == '__main__':
    input = []
    with open('sample_test.txt', 'r', encoding='UTF8') as f:
        for line in f:
            input.append(line.strip().split())
    print(input)
    print(math_homework(input))