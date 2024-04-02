""" Defines an asynchronous function for simulating a robot task. """
import asyncio
import logging

robot_task = None
robot_logger = logging.getLogger('Robot')


async def robot(robot_id: int, start_num: int = 0):
    """
    Asynchronous function simulating a robot task.

    Parameters:
    - robot_id (int): Unique identifier for the robot task.
    - start_num (int, optional): Starting number for counting. Defaults to 0.

    Returns:
    - int: The count value at the time of cancellation.

    Raises:
    - asyncio.CancelledError: Raised when the task is cancelled.
    """
    try:
        count = start_num
        while True:
            robot_logger.info('id: %d: %d', robot_id, count)
            count += 1
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        return count
