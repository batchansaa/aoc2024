def check_safe(arr):
    def check_inc_or_dec(sub_arr):
        return (
            all(1 <= int(sub_arr[i+1]) - int(sub_arr[i]) <= 3 for i in range(len(sub_arr) - 1)) or
            all(-3 <= int(sub_arr[i+1]) - int(sub_arr[i]) <= -1 for i in range(len(sub_arr) - 1))
        )
    if check_inc_or_dec(arr):
        return True
    
    for i in range(len(arr)):
        temp_arr = arr[:i] + arr[i+1:]
        if check_inc_or_dec(temp_arr):
            return True
    return False


with open('Day2/puzzle.txt') as f:
    data = [line.split() for line in f]

total = 0
total += sum(1 for line in data if check_safe(line))

print(total)
