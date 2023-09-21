def calc_sum() :             #함수의 head
    sum = 0                   #함수의 body
    for i in range(1, 101):
        sum += i
    
    print(f'sum = {sum}')
    
    
calc_sum()     #함수의 호출

# def calc_sum(start, end) :             
#     sum = 0                   
#     for i in range(start, end + 1):
#         sum += i
    
#     print('%d부터 %d까지의 합은 %d입니다.' % (start, end, sum))
    
# start = 50  
# end = 80        
# calc_sum(start, end)      #인자, 인수