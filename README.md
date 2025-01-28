# API Docker Bash Executor

This repository contains a simple API that connects to a Docker container to execute Bash commands. The API is designed to be lightweight and easy to use, allowing you to run shell commands inside a Docker container from an HTTP request.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Execute Bash commands inside a Docker container via HTTP requests.
- Lightweight and easy to set up.
- Supports custom Docker images.
- Returns the output of the executed command.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Node.js**: [Install Node.js](https://nodejs.org/) (if you want to modify or run the API locally)
- **Docker Compose** (optional): [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/api-docker-bash-executor.git](https://github.com/lucaspereirasouza/DeepSeek-API-Bash.git)
   ```

2. Run Docker compose for running the virtual machine
   ```bash
   Docker compose up
   ```

## Usage

Once the container is running, you can send HTTP requests to the API to execute Bash commands inside the Docker container.

### API Endpoints

- **POST /execute**

  Execute a Bash command inside the Docker container.

  **Request Body:**

  ```json
  {
    "command": "your-bash-command-here"
  }
  ```

  **Response:**

  ```json
  {
    "output": "command-output-here",
    "error": "error-message-if-any"
  }
  ```

### Examples

1. **Using `curl` to execute a command:**

   ```bash
   curl -X POST http://localhost:3000/execute \
   -H "Content-Type: application/json" \
   -d '{"command": "echo Hello, World!"}'
   ```

   **Response:**

   ```json
   {
     "output": "Hello, World!\n",
     "error": ""
   }
   ```

2. **Using `curl` to execute a command that fails:**

   ```bash
   curl -X POST http://localhost:3000/execute \
   -H "Content-Type: application/json" \
   -d '{"command": "ls /nonexistent"}'
   ```

   **Response:**

   ```json
   {
     "output": "",
     "error": "ls: cannot access '/nonexistent': No such file or directory\n"
   }
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you have any suggestions or find any bugs. :D

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to better fit your project's needs!
