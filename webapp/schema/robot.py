from datetime import datetime
from typing import Annotated, List

from pydantic import AfterValidator, BaseModel, ConfigDict


def check_positive_nums(page: int) -> int:
    assert page > 0, 'the page number cannot be less than one'
    return page


class StartInfo(BaseModel):
    start_num: int = 0
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'start_num': -3,
                }
            ]
        }
    }


class StopInfo(BaseModel):
    task_id: Annotated[int, AfterValidator(check_positive_nums)]
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'task_id': 1,
                }
            ]
        }
    }


class ResponseDefault(BaseModel):
    message: dict


class HistoryInfo(BaseModel):
    page: Annotated[int, AfterValidator(check_positive_nums)]
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'page': 1,
                }
            ]
        }
    }


class RobotHistoryInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    duration: int
    start_time: datetime
    stop_time: datetime
    start_num: int


class RobotHistoryInfoList(BaseModel):
    robot_history: List[RobotHistoryInfo]
