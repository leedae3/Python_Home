#main
import st_input
import st_calc
import st_output

print("Program is Start...")
student = {}
st_input.st_input(student) #call by ref
st_calc.st_calc(student)
st_output.output(student)
print("Program is over...")