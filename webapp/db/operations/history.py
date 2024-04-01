from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from conf.config import settings
from webapp.model.main_db.robot_history import RobotHistory


async def get_history_page(session: AsyncSession, page: int):
    offset = (page - 1) * settings.PAGE_SIZE
    query = select(RobotHistory).order_by(RobotHistory.id).offset(offset).limit(settings.PAGE_SIZE)
    result = await session.execute(query)
    history_page = result.scalars().all()

    return history_page
