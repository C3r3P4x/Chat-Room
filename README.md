# TCP Chat Room Project

## Overview
This project is a simple TCP chat room implemented in Python. It allows multiple users to connect to a central server and communicate with each other in real-time via text messages.

## Features
- **Client-Server Architecture**: The chat room utilizes a client-server model where multiple clients connect to a central server.
- **TCP Communication**: Transmission Control Protocol (TCP) is used for communication between the clients and the server, ensuring reliable and ordered delivery of messages.
- **Real-time Messaging**: Users can send messages to the chat room, and they will be immediately broadcasted to all connected clients in real-time.
- **Basic User Interface**: Although the focus of the project is on functionality rather than aesthetics, a simple command-line interface (CLI) is provided for users to interact with the chat room.

## Installation
To use this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/tcp-chat-room.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tcp-chat-room
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

   This will install all the necessary Python packages listed in the `requirements.txt` file.

4. Once the dependencies are installed, you can proceed to run the server and connect clients as described in the [Usage](#usage) section.


## Usage
1. **Server Setup**: Run the server script (`server.py`) to initialize the chat room server.
   ```bash
   python server.py
