from cProfile import label
import matplotlib.pyplot as plt

x = []
y = [1, 10, 48, 106, 122, 84, 36, 9, 1]
y2 = []


def Comb(n, m):
    m = min(m, n-m)
    ans = 1
    for i in range(m):
        ans *= (n-i)
    for i in range(m):
        ans /= (i+1)
    return ans


for i in range(1, 10):
    x.append(i)
    y2.append(float(y[i-1]) / Comb(9, i))

width = 0.3

A = plt.plot(x, y2, 'o-', color='red', label='Possibility of Quarantine')

plt.legend(loc='upper left')
plt.grid(True)

plt.xlabel('Number of Diagnoses')
plt.ylabel('P')

figure = plt.gcf()
figure.set_size_inches(10, 5)
#plt.savefig("Bar chart2.png", dpi=100)
plt.savefig("9people-2.png", dpi=1000)
plt.show()
