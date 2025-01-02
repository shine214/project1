s = "12.34"
try:
    num = int(s)  # 尝试将字符串 "12.34" 转换为整数
except ValueError as e:
    print("ValueError:", e)
