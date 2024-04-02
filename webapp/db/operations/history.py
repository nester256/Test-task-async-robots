""" Defines an asynchronous function to retrieve a page of robot history records from the database. """
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from conf.config import settings
from webapp.model.main_db.robot_history import RobotHistory


async def get_history_page(session: AsyncSession, page: int):
    """
    Asynchronous function to fetch a page of robot history records.

    This function constructs a SELECT query to retrieve a page of robot history records
    based on the specified page number and the page size defined in the application settings.

    Args:
    - session (AsyncSession): Asynchronous session for interacting with the database.
    - page (int): The page number to retrieve.

    Returns:
    - List[RobotHistory]: A list of robot history records representing the requested page.

    Note:
    - The page number starts from 1.
    """
    offset = (page - 1) * settings.PAGE_SIZE
    query = select(RobotHistory).order_by(RobotHistory.id).offset(offset).limit(settings.PAGE_SIZE)
    result = await session.execute(query)
    history_page = result.scalars().all()

    return history_page
