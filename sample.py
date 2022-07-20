for i in range(3,10):
    print(i,"Hello "+str(i))

val = lambda x : x + 10
arr = [10,20,30,40,51,78,99,21]

check_even = list(filter(lambda x : x%2==0,arr))

check_odd = list(map(lambda x : x%2!=0,arr))

print("The answer is",val(15))

print(check_even)
print(check_odd)