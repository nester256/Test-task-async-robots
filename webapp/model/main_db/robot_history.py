from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from webapp.model.meta import DEFAULT_SCHEMA, Base


class RobotHistory(Base):
    __tablename__ = 'robot_history'
    __table_args__ = ({'schema': DEFAULT_SCHEMA},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    duration: Mapped[int] = mapped_column(Integer, nullable=True)

    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    stop_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    start_num: Mapped[int] = mapped_column(Integer, nullable=False)
