'''Переменные'''

# Присваиваем значение 2 переменным
variable1 = 5
variable2 = 10

# С помощью 3 переменной в качестве буфера сохраняем одну из двух переменных в нее

# Стандартный подход
variable3 = variable2

variable2 = variable1

variable1 = variable3

# Средствами Питона

variable1, variable2 = variable2, variable1

# Также один ищ вариантов

variable1 = variable1 + variable2

variable2 = variable1 - variable2

variable1 = variable1 - variable2
