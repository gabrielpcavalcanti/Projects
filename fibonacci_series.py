import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):

    lista_num = [1,1]

    for i in range(2, n+1):

        num = lista_num[i-2] + lista_num[i-1]
        lista_num.append(num)
    
    return lista_num


y_axis = fibonacci(10)
print(y_axis)

range_num = np.arange(0,11,1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fibonacci sequence")

plt.bar(range_num, y_axis)
plt.plot(range_num, y_axis)

plt.show()


