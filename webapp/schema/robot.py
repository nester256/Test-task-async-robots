""" Defines Pydantic models for handling data validation. """
from datetime import datetime
from typing import Annotated, List

from pydantic import AfterValidator, BaseModel, ConfigDict


def check_positive_nums(number: int) -> int:
    """
    Validator function to ensure the page number is positive.

    Args:
    - page (int): The page number to validate.

    Returns:
    - int: The validated page number.

    Raises:
    - AssertionError: If the page number is less than or equal to zero.
    """
    assert number > 0, 'the number cannot be less than one'
    return number


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
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'message': {'information': 'example info'},
                }
            ]
        }
    }


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
