# Gestione CSV con FastAPI e Docker

This project is a simple CRUD (Create, Reade, Update, Delete) using FASTAPI.
This API allows you to manage user data and store it in a CSV file. FASTAPI is used to handle HTTP request and response.

## How it works

1. POST /items: Add a new user to the CSV file.
2. GET /items: Retrieve the list of users stored in the CSV.
3. PUT /items/{id}: Update user information by ID.
4. DELETE /items/{id}: Delete a user by ID from CSV file.
