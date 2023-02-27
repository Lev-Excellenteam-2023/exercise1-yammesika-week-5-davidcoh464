def is_complete_division(num):
    if num < 2:
        return False
    count = 1
    for i in range(2, num//2+1):
        if num % i == 0:
            count+=i
    return count == num

def all_complete_division():
    num = 2
    while True:
        if is_complete_division(num):
            yield num
        num+=1
        
out_complete_division = all_complete_division()
for i in range(4):# More than 4 it will get stuck in an infinite loop
    print(next(out_complete_division))