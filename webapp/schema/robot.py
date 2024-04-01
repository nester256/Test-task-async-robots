from pydantic import BaseModel


class StartInfo(BaseModel):
    start_num: int = 0


class StopInfo(BaseModel):
    task_id: int


class ResponseDefault(BaseModel):
    message: dict
