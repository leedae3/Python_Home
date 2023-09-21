#salary_input

def myinput(employee):
    num = int(input("사원번호 :"))
    geup = int(input("급 : "))     #int - 숫자로 인식
    ho = int(input("호 : "))
    sudang = int(input("수당 : "))
    # math = int(input("입력/출력(I/O)? : "))
    employee["사원번호"] = num
    employee["급"] = geup
    employee["호"] = ho
    employee["수당"] = sudang
    #employee[""]