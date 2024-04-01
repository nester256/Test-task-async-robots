from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from webapp.model.main_db.robot_history import RobotHistory


async def set_stop_inf(session: AsyncSession, task_id: int) -> None:
    async with session.begin():
        robot_history = await session.get(RobotHistory, task_id)
        if robot_history:
            robot_history.stop_time = datetime.now()
            robot_history.duration = (robot_history.stop_time - robot_history.start_time).total_seconds()
