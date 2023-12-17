import re

# 정규표현식을 이용한 정수 확인 함수
def is_integer(s):
    """Returns True if the string is an integer."""
    return re.match("[-]?\d+$", str(s)) != None