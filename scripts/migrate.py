""" Defines an asynchronous function for database migration and table creation. """
import asyncio
import logging

from sqlalchemy.exc import IntegrityError

from webapp.db.postgres import engine
from webapp.model import meta


async def main() -> None:
    """
    Asynchronous function for database migration and table creation.

    This function performs database migration by creating tables defined in the
    metadata of the web application's model. It utilizes the SQLAlchemy engine
    to execute SQL commands asynchronously.

    Raises:
    - IntegrityError: If the database objects already exist.

    Note:
    - Ensure that the database connection engine is properly configured before
      running this function.
    """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(meta.metadata.create_all)
    except IntegrityError:
        logging.exception('Already exists')


if __name__ == '__main__':
    asyncio.run(main())
