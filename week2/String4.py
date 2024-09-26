# 1. 將以下句子全部輸出成小寫
sentence = "PLEASE CONVERT THIS SENTENCE TO LOWER CASE."
print(sentence.lower())  # 結果: please convert this sentence to lower case.

# 2. 從字串裡取出 .html 左邊的部分
string = "python修煉第一期.html"
result = string.split(".html")[0]
print(result)  # 結果: python修煉第一期

# 3. 將輸入的卡號補0至16位
card_number = "314159265359"
formatted_card_number = card_number.zfill(16)
print(formatted_card_number)  # 結果: 0000314159265359

# 4. 使用者輸入年份、月份、日期，調整格式輸出
year = input("請輸入年份：")  # 輸入: "2010"
month = input("請輸入月份：")  # 輸入: "12"
day = input("請輸入日期：")  # 輸入: "31"
formatted_date = f"{year}.{int(month):02}.{int(day):02}"
print(formatted_date)  # 結果: 2010.12.31

# 5. 比對使用者輸入的帳號，無視大小寫及空白
correct_account = "TaipeiUniversity123"
user_input = input("請輸入帳號：")  # 例如輸入: "  TAIPEIUNIVersity123   "
is_correct = correct_account.lower().strip() == user_input.lower().strip()
print(is_correct)  # 結果: true 或 false
