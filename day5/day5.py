def count_fresh_ids(id_range, id_list):
    fresh_count = 0
    normalized_ranges = []

    for start, end in id_range:
        normalized_ranges.append((int(start) , int(end)))
    
    
    for id in id_list:
        for start, end in normalized_ranges:
            if start <= id <= end:
                fresh_count += 1
                break
    
    return fresh_count





if __name__ == '__main__':
    with open ('test.txt', 'r', encoding='UTF8') as f:
        id_range = []
        id_to_check = False
        id_list = []
        for line in f:
            
            if line.strip() == '':
                id_to_check = True
                continue
            if id_to_check:
                id_list.append(int(line.strip()))
            
            if not id_to_check:
                id_range.append(line.strip().split('-'))
    print(count_fresh_ids(id_range, id_list))