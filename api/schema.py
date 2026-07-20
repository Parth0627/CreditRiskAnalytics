from pydantic import BaseModel

class LoanApplication(BaseModel):
    data: dict