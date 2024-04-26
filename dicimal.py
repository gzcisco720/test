import re

# 定义正则表达式
pattern = r'\bdecimal\b\s*\(\s*\d+\s*,\s*\d+\s*\)' # 匹配 'decimal' 后跟括号内的数字，考虑了空格
pattern = fr"(?i){pattern}"  # (?i) 使正则表达式不区分大小写

# 示例 SQL 语句
sql_text = "CREATE TABLE example (id INT, price DECIMAL(10, 2), length decimal (5, 0));"

# 使用 re.findall 检查 SQL 文本中所有匹配的 'DECIMAL' 声明
matches = re.findall(pattern, sql_text)

if matches:
    print("Found DECIMAL declarations:", matches)
else:
    print("No DECIMAL declarations found.")