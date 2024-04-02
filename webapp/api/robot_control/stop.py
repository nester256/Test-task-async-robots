from fastapi import Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.robot_control.robot_tasks import active_robot_tasks
from webapp.api.robot_control.router import robot_router
from webapp.db.operations.stop import set_stop_inf
from webapp.db.postgres import get_session
from webapp.integrations.logger import api_logger
from webapp.schema.robot import ResponseDefault, StopInfo


@robot_router.post(
    '/stop',
    description='Endpoint for stop robots',
    responses={
        200: {'model': ResponseDefault, 'description': 'Robot stopped successfully'},
        404: {'model': ResponseDefault, 'description': 'Robot not found'},
    },
)
async def stop(
    body: StopInfo,
    session: AsyncSession = Depends(get_session),
) -> ORJSONResponse:
    if body.task_id in active_robot_tasks:
        task = active_robot_tasks.pop(body.task_id)
        task.cancel()
        await set_stop_inf(session, body.task_id)
        api_logger.info('Robot with task_id: %d stopped', body.task_id)
        return ORJSONResponse(
            {'message': f'Robot with task_id {body.task_id} stopped successfully'}, status_code=status.HTTP_200_OK
        )
    else:
        return ORJSONResponse(
            {'message': f'No robot found with task_id {body.task_id}'}, status_code=status.HTTP_404_NOT_FOUND
        )
