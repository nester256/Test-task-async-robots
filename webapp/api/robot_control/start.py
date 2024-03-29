from webapp.api.robot_control.router import robot_router


@robot_router.post(
    '/start'
)
async def start() -> None:
    pass
