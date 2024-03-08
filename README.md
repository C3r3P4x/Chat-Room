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
    git clone https://github.com/mudassir-javed/Chat-Room.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Chat-Room
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
   ```

   This command will start the server and prepare it to accept incoming connections from clients.

2. **Client Connection**: Once the server is running, you can connect to it using the client script (`myclient.py`). Multiple instances of the client script can be run to create multiple clients joining the server.

   ```bash
   python myclient.py <server_ip> <port>
   ```

   - Replace `<server_ip>` with the IP address of the server.
   - Replace `<port>` with the port number on which the server is running.

   Each instance of the client script represents a unique client connecting to the chat room.

3. **Chatting**: Once connected, users can send messages to the chat room by typing them into the CLI interface and pressing Enter. Messages will be broadcasted to all connected clients in real-time.

4. **Exiting**: To exit the chat room, users can type a predefined exit command (e.g., `/exit`) or simply close the client application.

By following these steps, you can effectively set up and use the TCP chat room, connecting multiple clients to the server and engaging in real-time communication.

## Credits

This project was created by [mudassir-javed](https://github.com/mudassir-javed).

If you find this project useful, consider giving it a star on GitHub and sharing it with others.
