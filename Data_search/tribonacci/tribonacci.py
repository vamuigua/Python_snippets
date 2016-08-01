numbers = [0,1,1]

n = int(raw_input("Input a number..."))
c = 0
while c < n:
    next = numbers[c] + numbers[c+1] + numbers[c+2]
    numbers.append(next)
    if numbers[c] >= n:
        break
    c += 1
print numbers
