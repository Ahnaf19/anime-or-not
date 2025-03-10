from fastapi import HTTPException


class InvalidImageFileException(HTTPException):
    def __init__(self, detail: str = "Invalid image file."):
        super().__init__(status_code=400, detail=detail)
