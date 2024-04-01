import asyncio
import logging

robot_task = None
robot_logger = logging.getLogger('Robot')


async def robot(robot_id: int, start_num: int = 0):
    try:
        count = start_num
        while True:
            robot_logger.info('id: %d: %d', robot_id, count)
            count += 1
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        return count
