# circular shape 0-99
# start at 50
# if < 0, then - ans + 99
# if > 99 then ans - 99

# for eg, L34 should give 0 (curr) - 34 = -34 -> -34 +99 = 65
# R50, should give 65(curr) + 50 = 115 -> 115 - 99 = 16

# 1. determine if L or R
# 2. apply operartion
# 3. if ans = 0, append 1 to password
# 4. return password

def secret_password(safe_input):
    password = 0
    curr = 50

    if not safe_input:
        return 
    
    for line in safe_input:
        first_letter = line[0]
        number = int(line[1:])
        if first_letter == 'L':
            curr = curr - number
            print(f"curr in L {curr}")
            while curr < 0:
                curr = curr + 100
                print(f"curr in L while block {curr}")
        elif first_letter == 'R':
            curr = curr + number
            print(f"curr in R {curr}")
            while curr > 99:
                curr = curr - 100
                print(f"curr in R while block {curr}")
        if curr == 0:
            password += 1
            print(f"password getting added {password}")
    return password


if __name__ == '__main__':
    with open('test.txt', 'r', encoding='UTF8') as f:
        ans = []
        for line in f:
            ans.append(str(line).strip())
        safe_input = ans

    ans = secret_password(safe_input)
    print(ans)