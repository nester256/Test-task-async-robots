from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from webapp.model.main_db.robot_history import RobotHistory


async def set_start_inf(session: AsyncSession, start_num: int) -> int:
    new_robot_history = RobotHistory(start_num=start_num, start_time=datetime.now())
    async with session.begin():
        session.add(new_robot_history)
        await session.flush()
    return new_robot_history.id
