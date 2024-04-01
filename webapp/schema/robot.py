from datetime import datetime
from typing import List, Annotated

from pydantic import BaseModel, ConfigDict, AfterValidator


class StartInfo(BaseModel):
    start_num: int = 0


class StopInfo(BaseModel):
    task_id: int


class ResponseDefault(BaseModel):
    message: dict


def check_page(page: int) -> int:
    assert page > 0, 'the page number cannot be less than one'
    return page


class HistoryInfo(BaseModel):
    page: Annotated[int, AfterValidator(check_page)]


class RobotHistoryInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    duration: int
    start_time: datetime
    stop_time: datetime
    start_num: int


class RobotHistoryInfoList(BaseModel):
    robot_history: List[RobotHistoryInfo]
