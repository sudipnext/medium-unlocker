# Medium-Unlocker
<img src="https://i.imgur.com/zeVvy4B.png" alt="alt text" width="50"/>

###### Image Credit:- *https://www.facebook.com/akumaaayush*

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

## Running using Extension

### Installing the Extension

1. Download the zip file of repository from `<> code` button or `extension.zip` folder from the releases section on right hand side.
2. Extract the files.
3. Go to:
``` Browser settings -> extensions -> manage extensions ```
4. Enable Developer mode
5. Click on `Load Unpacked` and select the `extension` folder from the extracted files.
6. You are good to go!

### Using the Extension

1. Pin the extension for easy access.
2. while you're on premium article tab, select `parse` button on extension.
3. Enjoy reading!

## Contributing

We welcome contributions from the community. If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository.**

   Click the "Fork" button at the top right corner of this repository to create a copy in your own GitHub account.

2. **Create a new branch for your feature or bug fix.**

   You can create a new branch in your forked repository using Git. For example:

   ```bash
   git checkout -b feature-your-feature-name


# Disclaimer & Notes

- **Educational Purpose**: This tool was created for educational purposes, showcasing vulnerabilities in some online systems.

- **Respect Intellectual Property**: Bypassing paywalls can infringe on the rights of content creators. Support them by purchasing a content subscription if you find value in their work.

- **Violation of Terms of Service**: Using this tool may violate the terms of service of platforms like Medium. Use this tool responsibly and at your own risk.

- **Note on Medium's Security**: As of the creation of this tool, platforms like Medium have not implemented stringent methods to enforce their paywall universally. This lack of rigid enforcement is a demonstration of potential vulnerabilities.

- **Ethical Use**: The absence of strict enforcement on Medium's part does not justify or endorse the misuse of this tool. Always consider the ethical implications of your actions.

- **Potential Legal Consequences**: Distributing or using tools that bypass paywalls can expose users to legal consequences. Be aware of laws and regulations in your jurisdiction.

The creator of this tool and its contributors are not responsible for any misuse, consequences, or actions resulting from the software's use. Choose your actions responsibly.

This software is licensed under the BSD 3-Clause License. See the LICENSE file for details.

