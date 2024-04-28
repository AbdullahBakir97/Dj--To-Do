# Django Todo App
![2024-04-28 (5)](https://github.com/AbdullahBakir97/Dj--To-Do/assets/127149804/2b5ad633-2a3e-4da4-bf2e-4e1d7b291f5e)
![2024-04-28 (6)](https://github.com/AbdullahBakir97/Dj--To-Do/assets/127149804/fce56ce9-ad76-41c0-9187-be391b00158f)


## Overview

This Django Todo App is a simple web application that allows users to create, manage, and organize their tasks in a todo list format. Users can add new tasks, mark tasks as completed, update task details, and delete tasks.

## Features

- User-friendly interface for managing todo tasks
- Add new tasks with titles and optional descriptions
- Mark tasks as completed or uncompleted
- Update task details such as title and completion status
- Delete tasks from the todo list
- Responsive design for seamless usage on different devices

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **SQLite**: A lightweight, serverless database engine that integrates seamlessly with Django for storing task data.
- **HTML/CSS**: Frontend markup and styling for the user interface.
- **JavaScript**: Enhances interactivity and dynamic behavior on the client side.
- **Bootstrap**: Provides pre-designed components and responsive layout utilities for frontend development.
- **jQuery**: Simplifies DOM manipulation and event handling in JavaScript.
- **AJAX**: Allows asynchronous communication with the server for seamless task updates without page reloads.

## Setup Instructions

1. *Clone the repository to your local machine*:

```
git clone https://github.com/AbdullahBakir97/Dj--To-Do
```
2. *Navigate to the project directory*
```
cd django-todo-app
```
3. *Install the project dependencies*
```
pip install -r requirements.txt
```
4. *Apply database migrations*
```
python manage.py migrate
```
5. *Start the development server*
```
python manage.py runserver
```

7. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- **Creating a New Task**: Click on the "Add New Todo" button and enter the task title in the provided input field. Optionally, you can add a description for the task. Click "Save" to add the task to the todo list.
- **Marking a Task as Completed**: Click on the checkbox or button associated with a task to mark it as completed. The task will be visually distinguished as completed.
- **Updating a Task**: Click on the "Edit" button next to a task to edit its details such as title and completion status. Make the necessary changes and click "Save" to update the task.
- **Deleting a Task**: Click on the "Delete" button next to a task to remove it from the todo list.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
