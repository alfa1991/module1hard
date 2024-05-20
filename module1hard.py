# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Упорядочиваем имена учеников в алфавитном порядке
sorted_students = sorted(students)

# Создаем словарь для хранения средних баллов
average_grades = {}

# Заполняем словарь средними баллами учеников
for i, student in enumerate(sorted_students):
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[student] = average_grade

# Выводим результат
print(average_grades)