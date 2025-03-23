import re
import pandas as pd

# Определяем шаблон для лог строки:
pattern = re.compile(
    r'(\S+)\s+'            # IP
    r'(\S+)\s+'            # User_ID
    r'(\S+)\s+'            # Auth_User
    r'\[([^\]]+)\]\s+'      # Timestamp
    r'"([^"]+)"\s+'         # Request
    r'(\S+)\s+'             # Size
    r'(\S+)\s+'             # Status
    r'(\S+)\s+'             # Response_Time
    r'(\S+)\s+'             # Session_ID
    r'"([^"]+)"\s+'         # Referer
    r'"([^"]+)"\s+'         # User_Agent
    r'"([^"]+)"'            # Client_IP
)

data = []
with open(r"C:\Users\rsadriev\Downloads\Telegram Desktop\nglog.txt", "r", encoding="utf-8") as f:
    for line in f:
        m = pattern.match(line)
        if m:
            data.append(m.groups())

# Задаем названия колонок
columns = ["IP", "User_ID", "Auth_User", "Timestamp", "Request", "Size", 
           "Status", "Response_Time", "Session_ID", "Referer", "User_Agent", "Client_IP"]

df = pd.DataFrame(data, columns=columns)

# Сохраняем результат в Excel
df.to_excel(r"C:\Users\rsadriev\Downloads\Telegram Desktop\nglog_output.xlsx", index=False)
