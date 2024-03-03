class DiaryIsLockedException(BaseException):
    def __init__(self,message):
        super().__init__("diary is locked, you have to unlock it")