import datetime
import sys

def run_calendar(year, month, day):
    month_name = day.strftime("%B")
    print(f"{month_name} {year}".center(20))

    day_of_week = 'Mo Tu We Th Fr Sa Su'
    print(f"{day_of_week}")

    first_day = datetime.date(year, month, 1)
    end_of_month = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1) if month == 12 else datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    days_of_month = (end_of_month).day
    first_day_of_week = first_day.weekday()

    for _ in range(first_day_of_week):
        print("   ", end="")

    for day in range(1, days_of_month + 1):
        print(f"{day:2d} ", end="")
        current_day = datetime.date(year, month, day)
        if (current_day.weekday() + 1) % 7 == 0:
            print()

args = sys.argv

# len(args) == 1 or len(args) == 3のときrun_calendarを実行したい
if len(args) == 1 or len(args) == 3:
# len(args) == 1 のときはtodayからyearとmonth代入
    if len(args) == 1:
        day = datetime.date.today()
        year = day.year
        month = day.month
        run_calendar(year, month, day)
# len(args) == 3 かつ'1' <= args(2) <= '12'のときはtodayからyear,args[2]からmonthに代入
    if len(args) == 3:
        today = datetime.date.today()
        year = today.year
        try:
            month = int(args[2])
        except ValueError:
            print(f"{args[2]} is neither a month number (1..12) nor a name")
            sys.exit(1)
        try:
            day = datetime.date(year, month, 1)
        except ValueError:
            print(f"{month} is neither a month number (1..12) nor a name")
            sys.exit(1)
        if args[1] == '-m' and 1 <= month <= 12:
            run_calendar(year, month, day)
        else:
            print(f"{month} is neither a month number (1..12) nor a name")
            sys.exit(1)
# それ以外は print(f"{month} is neither a month number (1..12) nor a name")してsys.exit(1)
else:
    print(f"{month} is neither a month number (1..12) nor a name")
    sys.exit(1)

# 学習記録-----------------------------------------------------------------------------------------------
# 必須条件
# mac に入っている cal コマンドと同じ見た目になっていること
# ※ cal コマンドは日曜始まりになっていますが、今回は月曜始まりで実装すること
# calendar モジュール は使わないこと
# Python の標準ライブラリは使用可能
# -mオプションで月を指定できるようにすること。今年が 2022 年なら cal -m 6で 2022 年 6 月のカレンダーになる。
# 引数を指定しない場合は、今月・今年のカレンダーが表示される
# -mの引数が不正な月の場合は次のエラーを出すこと
# --------------------------------------------------------------------------------------------------
# import datetime
# import sys
# "args: ["/Users/apple/hc_projects/hc_practice/python/calendar.py", "-m", "4"]
# sysで行いたいこと
# -m の引数1~12の入力があった際todayに該当する年の入力があったカレンダーを出力
# args = sys.argv
# month = int(args[2])
# print(month)
# print(args) # ['/Users/apple/hc_projects/hc_practice/python/calendar.py'] が出力 listかつstr型で格納される
# -m (引数) が1~12だったらyearに代入
# print(f"{1 <= month <= 2}")  # -m 12 == True, -m 20 == False
# if args[1] == '-m' and 1 <= month <= 12:
#     d = datetime.date(2025, month, 1)
#     year = d.year
# -m (引数)が1~12以外だったら(引数) is neither a month number (1..12) nor a name を出力
# else:
#     print(f"{month} is neither a month number (1..12) nor a name")
#     sys.exit


# month_name = d.strftime("%B")
# print(f"{month_name} {year}".center(20))

# day_of_week = 'Mo Tu We Th Fr Sa Su'
# print(f"{day_of_week}")

# first_day = datetime.date(year, month, 1)
# end_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
# days_of_month = (end_of_month).day
# first_day_of_week = first_day.weekday()

# for _ in range(first_day_of_week):
#     print("   ", end="")

# for day in range(1, days_of_month + 1):
#     print(f"{day:2d} ", end="")
#     current_day = datetime.date(year, month, day)
#     if (current_day.weekday() + 1) % 7 == 0:
#         print()

# ---------------------------------------------------------------------------------------------------------
# sysなし 対象月の日付出力と対象月1日の曜日出力
# d = datetime.date(2025, 2, 4)
# year = d.year
# month = d.month
# month_name = d.strftime("%B")
# print(f"{month_name} {year}".center(20))

# day_of_week = 'Mo Tu We Th Fr Sa Su'
# print(f"{day_of_week}")

# first_day = datetime.date(year, month, 1)
# end_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
# days_of_month = (end_of_month).day

# first_day_of_week = first_day.weekday()


# for _ in range(first_day_of_week):
#     print("   ", end="")


# for day in range(1, days_of_month + 1):
#     print(f"{day:2d} ", end="")
#     current_day = datetime.date(year, month, day)
#     # もしcurrent_day % 6 == 0 のとき文字列を改行したい
#     if (current_day.weekday() + 1) % 7 == 0: # %6 にしてしまうと月曜時にも適用されるのでweekday()に+1と%7で対応
#         print()

#--------------------------------------------------------------------------------------------------------------
# ヒントからコード作成

# 4月 2025 の部分を出力
# d = datetime.date(2025, 4, 4)
# year = d.year
# month = d.month
# print(f"{month}月 {year}")
# 月 火 水 木 金 土 日 の曜日の部分を出力
# day_of_week = ['月', '火', '水','木', '金', '土', '日']
# .weekday()で月曜を0,日曜6として整数で返すことができる
# weekday = d.weekday()
# print(day_of_week[weekday])
# 日付部分は該当月の初日と最終日を求めて、最初の日から最後の日まで出力する
# first_day = datetime.date(year, month, 1)
# end_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
# current_day = first_day
# while current_day <= end_day:
    # print(first_day)
    # current_day += datetime.timedelta(days=1)
# カレンダーのどの曜日から表示するかを求めるには初日の曜日をdate.weekday()で判定する
# first_day_of_week = first_day.weekday()
# print(day_of_week[first_day_of_week])