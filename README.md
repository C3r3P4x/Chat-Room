# TCP Chat Room Project

## Overview
This project is a simple TCP chat room implemented in Python. It allows multiple users to connect to a central server and communicate with each other in real-time via text messages.

## Features
- **Client-Server Architecture**: The chat room utilizes a client-server model where multiple clients connect to a central server.
- **TCP Communication**: Transmission Control Protocol (TCP) is used for communication between the clients and the server, ensuring reliable and ordered delivery of messages.
- **Real-time Messaging**: Users can send messages to the chat room, and they will be immediately broadcasted to all connected clients in real-time.
- **Basic User Interface**: Although the focus of the project is on functionality rather than aesthetics, a simple command-line interface (CLI) is provided for users to interact with the chat room.

## Usage
1. **Server Setup**: Run the server script (`server.py`) to initialize the chat room server.
   ```bash
   python server.py
