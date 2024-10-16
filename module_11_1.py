import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Библиотека  requests
URL = ('https://mail.ru')
response = requests.get( URL )
# Проверяем статус-код
if response.status_code == 200:
    print ('Succses')
    print(f'Кодировка сайта -  {response.encoding}')
    print(f'Время ответа - {response.elapsed}')
else:
    print('Error')


# Библиотека  pandas
fl = pd.read_excel('test.xlsx')
print (fl)
print (f'Вывод двух первых строк  \n {fl.head(2)}')
print(f'Машина с минимальным пробегом  \n {fl.min()}')



# Библиотека   numpy
array = np.array([1, -2, 3, -4, 5])

# Выполнение математических операций
sum = np.sum(array)
mean = np.mean(array)
abs = np.abs(array)

# Вывод результатов
print('Массив:', array)
print('Сумма:', sum)
print('Среднее:', mean)
print('Абсолютное значение:', abs)



# Библиотека  matplotlib

year = ['2020', '2021', '2022', '2023', '2024']
values = [205000, 320000, 310000, 340000, 350000]

plt.plot(year , values)
plt.grid()
plt.title('Продажи автомобилей')
plt.xlabel('Год')
plt.ylabel('Количество проданых автомобилей')
plt.show()


