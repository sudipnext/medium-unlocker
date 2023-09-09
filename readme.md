# Medium-Unlocker
## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the documentation for the **Medium-Unlocker** REST API. This API provides the ability to unlock and retrieve content from URLs, leveraging Google Web Cache. It allows you to access web content without direct access to the original website.

## Getting Started
``` 
https://medium-unlocker.onrender.com/unlock/?url={your url of medium article here}
```

## Running Locally on your Machine

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Pip, the Python package manager, is installed.

### Installation

To set up and run the API locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/sudipnext/medium-unlocker.git

2. Create a VirtualEnvironment:

   ```bash
   py -m venv env
        or 
   python3 -m venv env
3. Activate the VirtualEnv:
    ```bash
   source env/scripts/activate
        For Linux/MacOs
    Google it

4. Install:

   ```bash
   pip install requirements.txt
5. Run:
    ```bash
    python manage.py runserver
6. Open the Server Let's say 
    ```
    http://127.0.0.1:8000/ 
    ```
    and put ?url=```Your Favourite Premium Medium Article Link```


7. Enjoy



## Contributing

We welcome contributions from the community. If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository.**

   Click the "Fork" button at the top right corner of this repository to create a copy in your own GitHub account.

2. **Create a new branch for your feature or bug fix.**

   You can create a new branch in your forked repository using Git. For example:

   ```bash
   git checkout -b feature-your-feature-name

## License

This project is licensed under the BSD License.
