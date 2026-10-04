class ExceptionWithErrorCode(Exception):
    def __init__(self, error_code: str, message: str = "", http_status_code: int = 500):
        self.http_status_code = http_status_code
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)