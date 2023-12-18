# Task Manager App

The Task Manager is a web application designed to manage projects and tasks efficiently. Users can create projects, add tasks to them, and keep track of their progress. The application provides user authentication features, including login, logout, and sign-up functionalities.

## App Design

The application is built using Python for the backend, incorporating the Flask web framework. The frontend is developed using React, with Bootstrap for styling. The project utilizes two main models: the Project model and the Task model. The structure includes seven HTML templates, seven views, and two application-specific models.

## Technologies Used

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)
[![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Functionality

- Users can sign up for an account to access the application.
- After logging in, users can create projects to organize their tasks.
- Each project can have multiple tasks with details such as description, due date, etc.
- Users can mark tasks as completed and track their progress.
- The application provides a user-friendly interface for project and task management.


## Getting Started

To run the Wardrobify app locally, follow these instructions:

1. Clone the repository:
```bash
git clone https://gitlab.com/katrine-lombardo-public/task-manager.git
```

2. Navigate to the project directory:
```bash
cd task-manager
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the Flask application:
```bash
flask run
```

6. Open another terminal window, navigate to the frontend directory, and install the frontend dependencies:
```bash
cd frontend
npm install
```

7. Run the React development server:
```bash
npm start
```

8. Open your browser and go to http://localhost:3000 to access Task Manager.

Feel free to explore, contribute, and enhance the Task Manager experience! If you encounter any issues or have suggestions, please open an issue on this repository.
