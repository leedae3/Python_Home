student = {}         #1  
                           #딕셔너리는 키:값 쌍의 모음
def myinput(man) :           #3
    name = input("Enter your name : ")          #4
    age = input("Enter your age : ")
    man["name"] = name
    man["age"] = age      #5

myinput(student)       #2
print(student)      #6