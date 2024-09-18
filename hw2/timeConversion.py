sec = int(input())


#sec -> min, sec
min = sec // 60
sec = sec % 60
print(min, "min", sec, "sec")

#min -> hour, min, sec
hour = min // 60
min = min % 60
print(hour, "h", min, "min", sec, "sec")
