# 1. 請分別取出字母並且組合成一個字 (BMW)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bmw = letters[1] + letters[12] + letters[22]
print(bmw)  # 結果: BMW

# 2. 請分別取出字母並且組合成一個字 (OOOOOOOOOOPS)
oops = letters[14]*9 + letters[15] + letters[18]
print(oops)  # 結果: OOOOOOOOOOPS

# 3. 請將字串的元素取出後重新組合成另一個字串 (USA -> AUS)
word = "USA"
aus = word[2] + word[0] + word[1]
print(aus)  # 結果: AUS

# 4. 請分別取出元素並且組合成一個字串 (186)
digits = "1234567890"
result_186 = digits[0] + digits[7] + digits[5]
print(result_186)  # 結果: 186

# 5. 請分別取出元素並且組合成一個數值186，開根號取整數部分的值
import math
number_str = "1234567890"
num_186 = int(number_str[0] + number_str[7] + number_str[5])
sqrt_value = math.isqrt(num_186)
print(sqrt_value)  # 結果: 13
