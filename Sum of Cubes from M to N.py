def sum_of_cubes_m_to_n(m, n):
    result = 0
    for num in range(m, n + 1):
        result = result + num ** 3
    return result

m = int(input())
n = int(input())
result = sum_of_cubes_m_to_n(m, n)
print(result)