# расчёт необходимой длины крепежного элемента

print("Пожалуйста, введите размеры элементов в миллиметрах")

wall_thickness = input("Введите толщину стены: ")

anker_length = input("Введите длину анкера: ")

bar_thickness = input("Введите толщину бруса: ")

# запас толщины стенки в миллиметрах
reserve = 30

# меняем входные данные на целочисленые значения
wall_thickness = int(wall_thickness)
anker_length = int(anker_length)
bar_thickness = int(bar_thickness)

print("\n Variable result:" , "good" if (wall_thickness > (anker_length - bar_thickness + reserve)) else "horribly")
