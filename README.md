# Test Task

### Description
Test task simulating the interaction of the backend and robots

### How install
During development, I used containerization to simplify launching and installing dependencies
- You need install docker
- ```git clone https://github.com/nester256/TestTask```
- `cd TestTask`

### How run
Add a .env file with data. To make it easier, you can rename .env_example -> .env
#### For start app:
- ```docker-compose up --build```
#### To stop app: 
- Press `ctrl + c`
- ```docker-compose down -v```
    
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

Please note that all request and response parameters are automatically documented in Swagger, providing a detailed description of each endpoint's inputs and outputs.