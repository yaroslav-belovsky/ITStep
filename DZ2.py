from turtle import *

shape("turtle")
pensize(7)
speed(5)

# 1. Синє кільце
pencolor("blue")
circle(50)

# Перехід до місця для чорного кільця
penup()
forward(110)
pendown()

# 2. Чорне кільце
pencolor("black")
circle(50)

# Перехід до місця для червоного кільця
penup()
forward(110)
pendown()

# 3. Червоне кільце
pencolor("red")
circle(50)

# Перехід вниз до зеленого кільця
penup()
right(90)      # Повертаємо вниз
forward(50)    # Спускаємось на 50 пікселів
right(90)      # Повертаємо ліворуч (відносно екрана)
forward(55)    # Зміщуємось, щоб бути між червоним та чорним
left(180)      # Повертаємось у вихідний напрямок (праворуч)
pendown()

# 4. Зелене кільце
pencolor("green")
circle(50)

# Перехід до жовтого кільця
penup()
backward(110)  # Відходимо назад ліворуч
pendown()

# 5. Жовте кільце
pencolor("yellow")
circle(50)
