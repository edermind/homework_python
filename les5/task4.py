# Запрограммируй наставникам заполнение личной информации. Программа должна запрашивать ввод:
# 1. Фамилия преподавателя. 2. Должность. 3. Количество студентов во всех группах(например: 12,8,10).
# Эти данные должны лежать в отдельном списке внутри общего списка с информацией

surname = input()
job = input()
amount_students = input()

info_for_one = []

info_for_one.append(surname)
info_for_one.append(job)
info_for_one.append(amount_students)

global_info = []
global_info.append(info_for_one)
print(global_info)