import numpy as np

jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]

base_salary = np.array([jeff_salary, nick_salary, tom_salary])
print(f' Базовый оклад \n {base_salary}')

jeff_bonus = [500, 400, 400]
nick_bonus = [600, 300, 400]
tom_bonus = [200, 500, 400]

bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])

print(f' Бонусы  \n {bonus}')

bonus_and_salary = base_salary + bonus

print(f' Оклад плюс бонусы \n {bonus_and_salary}')

print(f' Максимальная зарплата {bonus_and_salary.max()}')

print(f' Максимальная зарплата по горизонтали {np.amax(bonus_and_salary, axis=1)}')

print(f' Максимальная зарплата по вертикали {np.amax(bonus_and_salary, axis=0)}')

print(f' Среднее значение {np.average(bonus_and_salary)}')

print(f' Медианное значение {np.median(bonus_and_salary)}')