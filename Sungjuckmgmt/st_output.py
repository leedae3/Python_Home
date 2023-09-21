#st_output

def output(student) :
    print(f"{student['name']}\t{student['kor']}\t{student['eng']}", end='\t')
    print(f"{student['math']}\t{student['total']}\t{student['avg']:.2f}", end='\t')      #.2f- 소수점 2자리 까지만 출력
    print(f"{student['grade']}")