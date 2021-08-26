import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label='linear')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label='quadratic')
plt.plot([1, 2, 3, 4], [1, 8, 27, 64], label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()