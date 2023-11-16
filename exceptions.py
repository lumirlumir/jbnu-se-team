# exceptions.py

# 이스터에그 예외 정의
class EasterEggException(Exception):
    def __init__(self, message=EASTER_EGG_MESSAGE):
        super().__init__(message)