user = raw_input("Input a text to search for...")
def reader():
    count = 0
    fo = open('words.txt', 'rw+')
    line = fo.readlines()
    for data in line:
        if user in data:
            count += 1
    return count
    fo.close()


print reader()