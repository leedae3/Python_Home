def calc_sum(start, end) :             
    sum = 0                   
    for i in range(start, end + 1):
        sum += i
    
    return sum
#    print('%d부터 %d까지의 합은 %d입니다.' % (start, end, sum))
    
start = 50  
end = 80      
result = calc_sum(start, end)
print("%d부터 %d까지의 합은 %d입니다." % (start, end, result))      #인자, 인수

