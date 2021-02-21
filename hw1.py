import  random as rnd

limit = 10 #this is for the maximum value
list1 = []
list2 = []
list3 = []

result_list = [list1,list2,list3]

temp_list = list1

while len(list3) != 3:
    if len(list1) == 3:
        temp_list = list2
    if len(list2) == 3:
        temp_list = list3

    is_prime = "prime"
    num1 = rnd.randrange(0,limit,1)

    #print(num1)
    if num1 > 0:
        for i in range(2,num1,1):
            if num1 % i == 0: # num1 is not prime
                is_prime = "not prime"
                break
        #print(is_prime)

        if is_prime == "prime":
            temp_list.append(num1)

"""
print(list1)
print(list2)
print(list3)
print(result_list) 
"""
print("\t","Generated matrix:")
print("\t",result_list[0],"\n\t",result_list[1],"\n\t",result_list[2] )

