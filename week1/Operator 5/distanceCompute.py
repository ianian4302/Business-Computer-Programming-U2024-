# meters between earth and moon
distance = 384400000
# meter per minute
rocket_speed = 250000

min = distance // rocket_speed

hour = min // 60
min = min % 60

day = hour // 24
hour = hour % 24

print(day, "days", hour, "hours", min, "minutes")