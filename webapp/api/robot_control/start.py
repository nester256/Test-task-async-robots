import asyncio

from fastapi import Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from robot.robot import robot

from webapp.api.robot_control.robot_tasks import active_robot_tasks
from webapp.api.robot_control.router import robot_router
from webapp.db.operations.start import set_start_inf
from webapp.db.postgres import get_session
from webapp.integrations.logger import api_logger
from webapp.schema.robot import ResponseDefault, StartInfo


@robot_router.post(
    '/start',
    response_model=ResponseDefault,
    status_code=status.HTTP_200_OK,
    description='Endpoint for start robots',
)
async def start(
    body: StartInfo,
    session: AsyncSession = Depends(get_session),
) -> ORJSONResponse:
    task_id = await set_start_inf(session, body.start_num)
    task = asyncio.create_task(robot(task_id, body.start_num))
    active_robot_tasks[task_id] = task
    api_logger.info('Robot with task_id: %d started', task_id)
    return ORJSONResponse(
        {'message': f'Robot with task_id {task_id} started successfully'}, status_code=status.HTTP_200_OK
    )
