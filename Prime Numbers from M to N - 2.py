def check_is_prime(n):
    if n <= 1:
        return False
        
    for i in range(2, int((n**0.5)) +1):
        if(n % i == 0):
            return False
    return True
                    
m = int(input())
n = int(input())
prime_numbers_list = []

for i in range(m, n + 1):
    if check_is_prime(i):
        prime_numbers_list.append(str(i))

prime_numbers_seperated_by_spaces = " ".join(prime_numbers_list)
print(prime_numbers_seperated_by_spaces)
