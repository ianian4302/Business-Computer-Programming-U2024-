# 本期頭獎末三位數號碼
jackpot_last_three = "386"

# 使用者輸入統一發票號碼
invoice_number = input("請輸入統一發票號碼：")  # 輸入範例: "AA60366386"

# 取出統一發票號碼的末三位數
invoice_last_three = invoice_number[-3:]

# 檢查是否中獎
is_winner = invoice_last_three == jackpot_last_three
print(is_winner)  # 結果: True 或 False


# 員工資料範例
employee_data_1 = "A002Michale Jordon19661021"
employee_data_2 = "B004Charlene Doe19961201"

# 定義函式來分割員工資料
def parse_employee_data(data):
    number = data[:4]  # 前四位為編號
    name = data[4:-8]  # 中間部分為人名
    birth_date = data[-8:]  # 後八位為出生年月日
    print(f"number: {number}")
    print(f"name: {name}")
    print(f"date of birth: {birth_date}")

# 呼叫函式並顯示結果
parse_employee_data(employee_data_1)
parse_employee_data(employee_data_2)
