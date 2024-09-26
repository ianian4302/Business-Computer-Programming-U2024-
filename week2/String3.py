letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1. 請取出自A到J的這些字母
# Start = 0 (A), End = 10 (J's next index)
print(letters[0:10])  # 結果: ABCDEFGHIJ

# 2. 請取出自A到倒數第3個的這些字母
# Start = 0 (A), End = -3 (倒數第三個的下一個是W)
print(letters[0:-2])  # 結果: ABCDEFGHIJKLMNOPQRSTUVWX

# 3. 請取出自字母E到最後一個的這些字母
# Start = 4 (E), End = len(letters) (包含最後一個字母)
print(letters[4:])  # 結果: EFGHIJKLMNOPQRSTUVWXYZ

# 4. 請取出自字母E到倒數第3個的這些字母
# Start = 4 (E), End = -2 (倒數第三個的下一個是W)
print(letters[4:-2])  # 結果: EFGHIJKLMNOPQRSTUVWX

# 5. 請取出自字母K到倒數第3個的這些字母
# Start = 10 (K), End = -2 (倒數第三個的下一個是W)
print(letters[10:-2])  # 結果: KLMNOPQRSTUVWX
