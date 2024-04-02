# Test Task

### Description
Test task simulating the interaction of the backend and robots

### How install
During development, I used containerization to simplify launching and installing dependencies
- You need [install docker](https://docs.docker.com/engine/install/)
```shell
git clone https://github.com/nester256/TestTask
```
```shell
cd TestTask
```

### How run
Add a .env file with data. To make it easier, you can rename .env_example -> .env
#### For start app:
```shell 
docker-compose up --build
```
#### To stop app: 
- Press `ctrl + c`
```shell
docker-compose down -v
```
    
### After start
- Project runs up two docker containers: web, web_db

### API Endpoints
All the API endpoints provided by this project are documented using Swagger. This means that you can interactively explore and test each endpoint by navigating to the `/swagger` route after running the application.

#### Start Robot
- Method: POST
- URL: /robot/start
- Description: Start a robot with provided parameters.

#### Stop Robot
- Method: POST
- URL: /robot/stop
- Description: Stop a running robot with the specified task ID.

#### Get Robot History Page
- Method: POST
- URL: /robot/history
- Description: Get a page of robot history.
