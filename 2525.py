hour, min = input().split()
hour = int(hour)
min = int(min)
time = int(input())

cook_hour = int(time / 60)
cook_min = time % 60
result_hour = hour + cook_hour
result_min = min + cook_min

if (min + cook_min >= 60):
    result_hour +=1
    result_min -= 60

if (result_hour >= 24):
    result_hour -= 24

print(f'{result_hour} {result_min}')

