#아스키코드로 알파벳 출력
#5개 마다 줄바꿈
#한줄마다 대, 소문자 전환


count, line = 0, 1
for i in range(65, 91) :               #알파벳 대문자 65-91
    if line % 2 == 1 : 
        print(chr(i), end = '\t')           #알파벳 소문자 97-123
    else : print(chr(i + 32), end = "\t")
    count += 1
    if count % 5 == 0 :
        print()
        line += 1
print()