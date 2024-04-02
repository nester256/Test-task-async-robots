""" Defines an asynchronous function to set stop information for a robot in the database. """
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from webapp.model.main_db.robot_history import RobotHistory


async def set_stop_inf(session: AsyncSession, task_id: int) -> None:
    """
    Asynchronous function to set stop information for a robot.

    This function retrieves the robot history record with the provided task ID
    from the database using the provided session. If the record exists, it updates
    the stop time to the current timestamp and calculates the duration of the robot's
    operation. It then commits the changes to the database.

    Args:
    - session (AsyncSession): Asynchronous session for interacting with the database.
    - task_id (int): The task ID of the robot history record to update.
    """
    async with session.begin():
        robot_history = await session.get(RobotHistory, task_id)
        if robot_history:
            robot_history.stop_time = datetime.now()
            robot_history.duration = (robot_history.stop_time - robot_history.start_time).total_seconds()
