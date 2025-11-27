from datetime import datetime
import re
import time

def log(title: str, other: str, additional: str | None = None):
    print(f'({additional or 'log'})[{title}] {other}')

def is_convertible_to_number(s: str) -> bool:
    return bool(re.fullmatch(r'^-?\d*\.?\d+$', s))

def get_until_date(seconds: int) -> datetime:
    return datetime.fromtimestamp(seconds + time.time())

def split_text(text: str) -> list[str]:
    pattern = r'"[^"]*"|\S+'
    return [item.strip('"') for item in re.findall(pattern, text)]