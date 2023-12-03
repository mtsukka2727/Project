import datetime
# https://docs.google.com/spreadsheets/d/1z5EdQOmEMEFg2tdQEc-yeWUBdT8QeCvr38EeDgIFX2k/edit?usp=sharing
from dateutil.relativedelta import relativedelta

# 基準年月

# 元金

# 初期費用

### 入力
input_annual_late = 7

# 月の積立金額
pay_per_month = 30
# 積立期間
pay_term = 30
# スタート年月


###出力


# スタートの〇年〇月
input_year = 2024
input_month = 1
dt1 = datetime.datetime.now()


# 欲しい年の期間
output_period_year = 1
# 内部での計算用に変換が必要
output_period_month = output_period_year * 12

# # 年月のリスト
# # year_month_list =[]
# # for i in range(output_period_month):
# #     # 
# #     if year_month_list == []:
# #         year_month_list.append()
# #     else:
# #         year_month_list.append(year_month_list[-1])
# #     dt2 = dt1 + datetime.timedelta(year_month_list=1)
#     # 年を取得# 元金のリスト


# 出力予定の年月のリスト
year_month_list = []
for i in range(12):
    # dt1 + 〇ヵ月
    this_month = dt1 + relativedelta(months=i)
    # 2024/1 の形式で出力
    this_month_output = f"{this_month.year}/{this_month.month}"
    # print(f"{i},{this_month_output}")
    # [2023/11, 2023/12, 2024/1, ...]
    year_month_list.append(this_month_output)
print(f"年月日{year_month_list}")


# 元金
pay_list = []
for elem in range(output_period_month):
    # 今月までの元金(=前月までの元金 + 今月の掛け金)
    if pay_list == []:
        pay_list.append(pay_per_month)
    else:
        pay_list.append(pay_list[-1] + pay_per_month)
print(f"元金＝{pay_list}")

# 評価額のリスト
amount_appraised_list = []
# 毎月の増加率
increase_rate = input_annual_late/100/12
for index in range(output_period_month):
    # 前月の評価額 amount_appraised の最後の要素
    # (1 + 年率/12) = increase_rate
    # 今月の積立額 [30, 60, 90, ...]
    pay_this_month = pay_list[index] 
    # 前月の評価額 * (1 + 年率/12) + 今月の積立額
    if amount_appraised_list == []:
        amount_appraised_list.append(pay_this_month)
    else:
        amount_appraised_list.append(amount_appraised_list[index-1] * increase_rate + pay_this_month)
print(f"評価額＝{amount_appraised_list}")


# 増加額のリスト
# （increase_rate * 元の金額）ー　先月の金額
increase_amount_list = []
for num in range(output_period_month):
    if increase_amount_list == []:
        increase_amount_list.append(amount_appraised_list[num])
    else:
        increase_amount_list.append(amount_appraised_list[num] - increase_amount_list[num-1])
print(f"増加額＝{increase_amount_list}")


# pay_per_month = 30 
# increase_amount_list = []
# for num in range(pay_list):
#     if increase_amount_list == []:
#         increase_amount_list.append(pay_per_month)
#     else:
#         increase_halfway_rate = increase_amount_list[-1] - increase_amount_list[num]
#         increase_amount_list.append(increase_halfway_rate)
# print(increase_amount_list)



# # 元金のリスト
# pay_list = []
# for elem in range(output_period_month):
#     # 今月までの元金(=前月までの元金 + 今月の掛け金)
#     if pay_list == []:
#         pay_list.append(pay_per_month)
#     else:
#         pay_list.append(pay_list[-1] + pay_per_month)
#     print(pay_list)