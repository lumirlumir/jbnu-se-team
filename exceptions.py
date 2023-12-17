# exceptions.py

from constants import EASTER_EGG_MESSAGE_1, EASTER_EGG_MESSAGE_2, EASTER_EGG_MESSAGE_3

# 이스터에그 예외 정의
class EasterEggException_1(Exception):
    def __init__(self, message=EASTER_EGG_MESSAGE_1):
        super().__init__(message)
        
class EasterEggException_2(Exception):
    def __init__(self, message=EASTER_EGG_MESSAGE_2):
        super().__init__(message)
        
class EasterEggException_3(Exception):
    def __init__(self, message=EASTER_EGG_MESSAGE_3):
        super().__init__(message)