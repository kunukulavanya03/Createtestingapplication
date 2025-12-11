## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create a .env file from the example: `cp .env.example .env`
3. Run the application: `uvicorn app.main:app --reload`

## API Endpoints
### /arithmetic/{operation}
Perform arithmetic operation
* Method: GET
* Path Parameters:
  + operation (string)
  + num1 (number)
  + num2 (number)
* Response:
  + result (number)

### /input
Validate user input
* Method: POST
* Request Body:
  + input (string)
* Response:
  + valid (boolean)
  + error (string)

### /data
Retrieve in-memory data storage
* Method: GET
* Response:
  + data (object)