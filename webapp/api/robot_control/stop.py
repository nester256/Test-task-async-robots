from webapp.api.robot_control.router import robot_router


@robot_router.post(
    '/stop'
)
async def stop() -> None:
    pass
