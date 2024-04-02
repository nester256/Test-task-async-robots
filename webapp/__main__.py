""" This file is for running a web application using the Uvicorn server. """
import uvicorn

from conf.config import settings

if __name__ == '__main__':
    uvicorn.run('webapp.main:create_app', host=settings.BIND_IP, port=settings.BIND_PORT, factory=True, reload=True)
