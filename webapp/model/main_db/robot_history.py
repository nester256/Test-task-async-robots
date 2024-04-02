""" Defines the SQLAlchemy model for robot history records. """
from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from conf.config import settings
from webapp.model.meta import Base


class RobotHistory(Base):
    """
    SQLAlchemy model for robot history records.
    """

    __tablename__ = 'robot_history'
    __table_args__ = ({'schema': settings.DEFAULT_SCHEMA},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    duration: Mapped[int] = mapped_column(Integer, nullable=True)

    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    stop_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    start_num: Mapped[int] = mapped_column(Integer, nullable=False)
