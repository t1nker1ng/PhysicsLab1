import math

f = open(r"C:\\Users\\egorn\\Downloads\\Telegram Desktop\\chisla.txt")
number = f.read().split()
numbers = []
for i in range(50):
    numbers.append(float(number[i]))  # Создание всех чисел
min = 1000
max = 0
sr = 0


for i in range(50):
    if numbers[i] < min:
        min = numbers[i]  # min
    if numbers[i] > max:
        max = numbers[i]  # max


for i in range(50):
    sr += numbers[i]/50  # Среднее значение


print("------------------------------")
kv = 0
s = 0
for i in range(50):
    kv += (numbers[i]-sr)**2  # Сумма квадратов разностей
    s += (numbers[i]-sr)
sigma = math.sqrt(kv/49)  # sigma
print("LaTeX or no?(y/n)")
otv = input()
if otv == "y":
    print("table 1:")
    print("\\begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}")
    print("\\hline № & $t_i$, с & $t_i -\\langle t \\rangle_N$,с & $(t_i-\\langle t \\rangle_N)^2$, c$^2$ \\\\")
    for i in range(50):
        print("\\hline")
        print(i+1, '&', round(numbers[i], 4), '&', round(numbers[i]-sr, 4),
              '&', round((numbers[i]-sr)**2, 4), "\\\\")  # Создание таблицв
    rho = 1/(sigma*math.sqrt(2*math.pi))  # Ро
    print("\\hline")
    print("$\\langle t \\rangle_N =$", sr, '&', "$\\Sigma = $", s, '&', "$\\sigma = $",
          sigma, '&', "$\\rho = $", rho, "\\\\")  # Нижняя строчка таблицы
    print("\\hline")
    print("\\end{tabular}")
else:
    for i in range(50):
        print("table 1:")
        print(i+1, '|', round(numbers[i], 4), '|',
              round(numbers[i]-sr, 4), '|', round((numbers[i]-sr)**2, 4), "\\\\")  # Создание таблицв
    rho = 1/(sigma*math.sqrt(2*math.pi))  # Ро
    print("<t>N = ", sr, ' ', "Sigma = ", s, ' ', "sigma = ",
          sigma, ' ', "rho = ", rho)  # Нижняя строчка таблицы
print("------------------------------")
a = (max-min)/math.sqrt(50)  # Дельта Т
intervals = []
rho_max_arr = []
inter = int(a)
chislo = min
counter = 0
while chislo < max:
    chislo += a
    counter += 1  # Подсчет максимального числа интервалов
counter -= 1
counter1 = counter
intervals.append(min)
for i in range(counter1):
    intervals.append(min+a*(i+1))  # Интервалы
intervals.append(max)
counter += 2
int_length = intervals[1]-intervals[0]

for i in range(counter1+1):
    rho_max = (1/(sigma*math.sqrt(2*math.pi))) * \
        math.e**(-(intervals[i]-sr)**2/(2*(sigma)**2))  # rho 2nd table "p"
    rho_max_arr.append(rho_max)

znach = []
for i in range(len(intervals)-1):
    counter = 0
    for j in range(50):
        if numbers[j] >= intervals[i] and numbers[j] <= intervals[i+1]:
            counter += 1
    znach.append(counter)


middle_value = []
for i in range(len(intervals)-1):
    middle_value.append(((intervals[i+1]-intervals[i])/2) + intervals[i])
print("LaTeX or no?(y/n)")
otv = input()
if otv == "y":
    print("table 2:")
    print("\\begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}")
    print("\\hline Границы интервалов, с & $\\Delta N$ & $\\frac{\\Delta N}{N \\Delta t},$с$^{-1}$ & $t$, c & $\\rho$, c$^{-1}$ \\\\")
    for i in range(len(intervals)-1):
        print("\\hline")
        print("$[", round(intervals[i], 4), ';', round(intervals[i+1], 4), "]$", '&',
              round(znach[i], 4), '&', round(znach[i]/(50*int_length), 4), '&', round(middle_value[i], 4), '&', rho_max_arr[i], "\\\\")
    print("\\hline")
    print("\\end{tabular}")
else:
    print("table 2:")
    for i in range(len(intervals)-1):
        print("[", round(intervals[i], 4), ';', round(intervals[i+1], 4), "]", '|',
              round(znach[i], 4), '|', round(znach[i]/(50*int_length), 4), '|', round(middle_value[i], 4), '|', rho_max_arr[i])
sigma_arr_p = []
sigma_arr_m = []
for i in range(3):
    sigma_arr_p.append(sr+(i+1)*sigma)
    sigma_arr_m.append(sr-(i+1)*sigma)
print("------------------------------")
DeltaN = []
for i in range(3):
    counter = 0
    for j in range(50):
        if numbers[j] <= sigma_arr_p[i] and numbers[j] >= sigma_arr_m[i]:
            counter += 1
    DeltaN.append(counter)
print("LaTeX or no?(y/n)")
otv = input()
if otv == "y":
    print("table 3:")
    print("\\begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}")
    print("\\hline & Интервал, с &  & & \\\\ & От и До &$\\Delta N$ & $\\frac{\Delta N}{N}$ & $P$ \\\\")
    P = [0.683, 0.954, 0.997]
    for i in range(3):
        print("\\hline")
        print("$\\langle t \\rangle_N \\pm \\sigma_N$","&","$[", round(sigma_arr_m[i], 4), ';', round(sigma_arr_p[i], 4),
              ']$', '&', DeltaN[i], '&', DeltaN[i]/50, '&', P[i], "\\\\")
    print("\\hline")
    print("\\end{tabular}")
else:
    print("table 3:")
    P = [0.683, 0.954, 0.997]
    for i in range(3):
        print("[", round(sigma_arr_m[i], 4), ';', round(sigma_arr_p[i],
              4), ']', '|', DeltaN[i], '|', DeltaN[i]/50, '|', P[i])