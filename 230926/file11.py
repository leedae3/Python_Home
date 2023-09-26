def myfunc():
    a = num
    count = 0
    for num in range(1, 250):              #range(초기값, 끝값, 증감값)
        if num % num == 0 :
            print(num, end = '\t')
            a += 1
            if count % 1 == 0 :
                print()
