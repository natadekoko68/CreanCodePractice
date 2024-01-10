# try:
#     x = int(input("整数値を入力してください: "))
#     result = 10/x
#     print("結果:", result)
# except Exception:
#     pass

try:
    x = int(input("整数値を入力してください: "))
    result = 10/x
    print("結果:", result)
except ValueError:
    pass
except ZeroDivisionError:
    pass
