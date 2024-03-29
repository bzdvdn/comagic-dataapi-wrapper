
class ComagicException(Exception):
    def __init__(self, error_data, *args, **kwargs):
        self.error_data = error_data
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"Code: {self.error_data['code']}, message: {self.error_data['message']}"