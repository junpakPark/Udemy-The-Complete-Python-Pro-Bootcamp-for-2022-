# # list comprehension
# numbers = [1, 2, 3]
# new_numbers = [i + 1 for i in numbers]
# print(new_numbers)

# name = "Angela"
# name_list = [i.lower() for i in name]
# print(name_list)

# even_num = [i * 2 for i in range(1, 5)]
# print(even_num)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_name = [i.upper() for i in names if len(i) >= 5]
# print(long_name)

# # dict comprehension
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {name: random.randint(68, 100) for name in names}
# print(students_score)
# passed_students = {key: value for (key, value) in students_score.items() if value > 90}
# print(passed_students)

# 섭씨를 화씨로 바꾸기
# hint: temp_f = (temp_c * 9 /5) + 32
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: value * 9 / 5 + 32 for (key, value) in weather_c.items()}

print(weather_f)
