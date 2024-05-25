# Backend

This is the backend application for the Motivation App. It is built using Python and Flask framework.

## Project Structure

The backend application has the following files and directories:

- `app.py`: This is the main file of the backend application. It sets up the Flask server and defines the routes for handling requests.
- `models/Motivation.py`: This file contains the `Motivation` class which represents a motivation sentence. It has properties like `id` and `text` to store the data of a motivation sentence.
- `routes/motivation_routes.py`: This file defines the routes for handling motivation-related requests. It imports the `Motivation` class and defines endpoints for fetching and returning a list of motivation sentences.
- `requirements.txt`: This file lists the Python dependencies required for the backend application.

## Getting Started

To run the backend application, follow these steps:

1. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

2. Start the Flask server by running the following command:
   ```
   python app.py
   ```

3. The backend application will be running on `http://localhost:5000`.

## API Endpoints

The backend application provides the following API endpoints:

- `GET /motivation`: Returns a list of motivation sentences.
- `POST /motivation`: Adds a new motivation sentence to the list.

## Dependencies

The backend application requires the following dependencies:

- Flask==2.0.1
- Flask-Cors==3.0.10

You can install these dependencies by running the command mentioned in the "Getting Started" section.

For more information, please refer to the [frontend README](../frontend/README.md).

**Note: This file is intentionally left blank. Please refer to the frontend README for more information about the frontend application.**