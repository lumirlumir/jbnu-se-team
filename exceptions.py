# exceptions.py

from constants import EASTER_EGG_MESSAGE_1, EASTER_EGG_MESSAGE_2, EASTER_EGG_MESSAGE_3, ERROR_MESSAGE_OUT_OF_RANGE, ERROR_MESSAGE_INPUT_ERROR, ERROR_MESSAGE_INVALID_OPERATOR

# 이스터에그 예외 정의
class EasterEggException_1(Exception):
    def __init__(self, message = EASTER_EGG_MESSAGE_1):
        super().__init__(message)
        
class EasterEggException_2(Exception):
    def __init__(self, message = EASTER_EGG_MESSAGE_2):
        super().__init__(message)
        
class EasterEggException_3(Exception):
    def __init__(self, message = EASTER_EGG_MESSAGE_3):
        super().__init__(message)

# 입력 오류 예외 정의
class InputException(Exception):
    def __init__(self, message = ERROR_MESSAGE_INPUT_ERROR):
        super().__init__(message)

# 음수 팩토리얼 예외 정의
class OutOfRangeException(Exception):
    def __init__(self, message = ERROR_MESSAGE_OUT_OF_RANGE):
        super().__init__(message)

class InvalidOperatorException(Exception):
    def __init__(self, message = ERROR_MESSAGE_INVALID_OPERATOR):
        super().__init__(message)