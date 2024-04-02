""" Defines an asynchronous function to record the start information of a robot in the database. """
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from webapp.model.main_db.robot_history import RobotHistory


async def set_start_inf(session: AsyncSession, start_num: int) -> int:
    """
    Asynchronous function to record the start information of a robot.

    This function creates a new RobotHistory object with the provided start number
    and the current timestamp as the start time. It then adds the object to the session
    and flushes it to the database to record the start information.

    Args:
    - session (AsyncSession): Asynchronous session for interacting with the database.
    - start_num (int): The start number of the robot.

    Returns:
    - int: The ID of the newly created robot history record.
    """
    new_robot_history = RobotHistory(start_num=start_num, start_time=datetime.now())
    async with session.begin():
        session.add(new_robot_history)
        await session.flush()
    return new_robot_history.id
