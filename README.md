# Gestione CSV con FastAPI e Docker

This project is a simple CRUD (Create, Reade, Update, Delete) using FASTAPI.
This API allows you to manage user data and store it in a CSV file. FASTAPI is used to handle HTTP request and response.

## How it works

1. POST /items: Add a new user to the CSV file.
2. GET /items: Retrieve the list of users stored in the CSV.
3. PUT /items/{id}: Update user information by ID.
4. DELETE /items/{id}: Delete a user by ID from CSV file.


## Building the Docker Image

To build the Docker image for this project, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory where the `Dockerfile` is located:

   ```bash
   cd /path/to/your-csv-crud-fastapi-docker

Execute the command:
   `docker build -t csv-crud-fastapi-docker` .

Once the image is built, you can run a container with the following command:
    `docker run -d -p 8001:8000 csv-crud-fastapi-docker`
    

Open the postman collection and test the project


