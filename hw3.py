def prime_first(number):
    if number >= 2:
        is_prime = "prime"
        num1 = number

        #print(num1)
        if num1 > 0:
            for i in range(2,num1,1):
                if num1 % i == 0: # num1 is not prime
                    is_prime = "not prime"
                    break
            #print(is_prime)
            if is_prime == "prime":
                print(num1)

def prime_second(number):
    if number >= 2:
        is_prime = "prime"
        num1 = number

        # print(num1)
        if num1 > 0:
            for i in range(2, num1, 1):
                if num1 % i == 0:  # num1 is not prime
                    is_prime = "not prime"
                    break
            # print(is_prime)
            if is_prime == "prime":
                print(num1)

for i in range(0,1000,1):
    if i<500:
        prime_first(i)
    else:
        prime_second(i)

