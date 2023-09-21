#st_input

def st_input(student):
    name = input("name : ")
    kor = int(input("korean : "))     #int - 숫자로 인식
    eng = int(input("english : "))
    math = int(input("math : "))
    student["name"] = name
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math