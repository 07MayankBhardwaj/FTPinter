
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


# FTP client-server using Tkinter 

Client Side : 



I have implement an FTP client using the Tkinter library in Python. The client connects to a remote FTP server and allows the user to perform various operations such as changing the directory, creating a directory, deleting a directory or file, downloading a file, uploading a file, and closing the connection.

The code imports the necessary libraries such as tkinter, os, ftplib, stegano, and PIL. It defines various functions such as connectServer(), loginServer(), displayDir(), changeDirectory(), createDirectory(), deleteDirectory(), deleteFile(), downloadFile(), uploadFile(), and closeConnection() to handle the different operations.

The GUI of the FTP client is implemented using Tkinter widgets such as Label, Entry, Button, and Text. The client connects to the remote FTP server using the IP address and port number entered by the user. Once connected, the user can enter the login credentials and login to the server. The current directory and file structure of the server are displayed in a listbox.

The user can perform various operations on the server such as changing the directory, creating a directory, deleting a directory or file, downloading a file, and uploading a file. The user can select a file for upload using a file dialog box. The client also uses the stegano library to hide and retrieve messages in images. Finally, the user can close the connection to the server.

Server Side : 

This is a Python script that uses the pyftpdlib library to create an FTP server.The script first imports the necessary modules from pyftpdlib to create an FTP server: DummyAuthorizer, FTPHandler, and FTPServer. It also imports the built-in os module.Next, the script defines the main() function, where the server is instantiated and configured.The authorizer object is created to manage users. The script defines a new user 'venom' with the password 'venom123' and full read/write permissions. It also creates an anonymous user with read-only permissions.

The FTPHandler class is then instantiated and configured to use the authorizer created earlier. The handler banner is also customized with a string returned when the client connects.The script then creates an FTP server object that listens on the address '127.0.0.1' and port number 2121. Connection limits are set to limit the number of connections the server can accept.

Finally, the main() function is called and the server is started by calling the serve_forever() method on the FTPServer object.

Overall, this script creates a simple FTP server that allows users to connect and transfer files with read and write permissions. The server is configured to limit the number of connections it accepts, and the banner can be customized to display a message when users connect.




## Documentation

[Documentation](https://linktodocumentation)

I developed a Graphical User Interface (GUI) based FTP server for my Raspberry Pi 4. The purpose of this tool is to enable seamless transfer of files between my Windows and Linux computers and my Raspberry Pi.

The application is designed to work within a home network and is configured to use the IP address of the network, such as "192.168.101.*", and a port number of 2121. To ensure security, the application requires a username and password for access to the FTP server running on the Raspberry Pi.

While the tool can be used to connect to global FTP services such as Hostinger FTP server or third-party FTP providers, it is optimized for local use within a home network.

Overall, this FTP server provides a user-friendly and secure way to transfer files to and from the Raspberry Pi within a home network environment.


## Installation

Install my-project with just few steps : 

```bash
git clone https://github.com/07MayankBhardwaj/FTPinter.git

Client Code Prerequisites:
~Python 3.x
~PyQt5 library (pip install pyqt5)
~ftplib library (should be installed by default with Python 3.x)

Server Code Prerequisites:
~Python 3.x
~pyftpdlib library (pip install pyftpdlib)
~os library (should be installed by default with Python 3.x)

```
    
## Deployment

To deploy this project run

```bash
  python3 client.py
  python3 server.py
```


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd FTPinter
```

Install dependencies

```bash
  pip install pyftplib
  pip install tk
  pip install Pillow
```

Navigate to the ftp server folder

```bash
  first start - Server.py (change username & passcode)
  second start - Client.py
```


# Code Explaination : 

# Client side code-wise explanation of the Python script :

The code defines several functions for connecting to an FTP server, logging in, and performing various FTP commands such as changing directories, creating and deleting directories, and downloading and deleting files. 

The first function, `connectServer()`, retrieves the IP address and port number from input fields, attempts to connect to the server using `ftp.connect()`, and displays any resulting messages in a text box. If the connection is successful, it prompts the user to enter login credentials.

The second function, `loginServer()`, retrieves the login and password from input fields, attempts to log in using `ftp.login()`, and displays any resulting messages in a text box. If the login is successful, it hides the login form and displays the server directory in a list box using the `displayDir()` function.

The third function, `displayDir()`, retrieves a list of directories from the server using `ftp.nlst()`, clears and populates a list box with the directories, and displays it to the user.

The next several functions are FTP commands that are triggered by user input. The `changeDirectory()` function attempts to change the current directory on the server using `ftp.cwd()`, and then displays the updated directory using `displayDir()`. The `createDirectory()` function attempts to create a new directory on the server using `ftp.mkd()`, and then displays the updated directory using `displayDir()`. The `deleteDirectory()` function attempts to delete a directory on the server using `ftp.rmd()`, and then displays the updated directory using `displayDir()`. The `deleteFile()` function attempts to delete a file on the server using `ftp.delete()`, and then displays the updated directory using `displayDir()`. The `downloadFile()` function attempts to download a file from the server using `ftp.retrbinary()` and write it to a local file using `open()`, and then displays the updated directory using `displayDir()`. 

In all of these FTP command functions, any resulting messages are displayed in a text box. The `displayDir()` function is called at the end of each of these functions to update the displayed directory.

## Received folder : 

=> ftp.cwd('received') ~ This will ensure that any file uploaded by the user will go to the "received" folder.

I have Modified the uploadFile() function to allow the user to select a file from their local system and upload it to the FTP server's "received" folder. 

## Download folder :

=> down = open("download/" + file, "wb")

It then opens a new file in binary write mode in the "download" folder to write the downloaded content to.


----------------------------------------------------------------------------------

# Server side code-wise explanation of the Python script:

1. Importing modules
The script starts by importing the necessary modules - `os`, `DummyAuthorizer`, `FTPHandler`, and `FTPServer` from the `pyftpdlib` package.

2. Defining main function
The `main()` function is defined that performs the following tasks:

3. Instantiating a dummy authorizer
The `DummyAuthorizer` class is used to instantiate a dummy authorizer for managing 'virtual' users. The `add_user()` method of the `DummyAuthorizer` class is used to define a new user with the username 'venom', password 'venom123', home directory '.', and full r/w permissions. The `add_anonymous()` method of the `DummyAuthorizer` class is used to define a read-only anonymous user with the current working directory as the home directory.

4. Instantiating an FTPHandler class
The `FTPHandler` class is instantiated and its `authorizer` attribute is set to the `authorizer` object created in the previous step. The `banner` attribute of the `FTPHandler` class is set to a custom message that will be displayed when a client connects.

5. Defining address and port
The `address` tuple is defined to specify the IP address and port number that the FTP server will listen on.

6. Instantiating an FTPServer class
The `FTPServer` class is instantiated with the `address` tuple and `handler` object created in the previous steps. The `max_cons` attribute is set to limit the maximum number of connections that the server can handle simultaneously. The `max_cons_per_ip` attribute is set to limit the maximum number of connections that a single IP address can have.

7. Starting FTP server
The `serve_forever()` method of the `FTPServer` class is called to start the FTP server and listen for incoming client connections. The script will run indefinitely until the server is shut down or interrupted.

8. Executing main function
Finally, the `main()` function is called only if the script is being executed directly, as opposed to being imported as a module by another script. This is done using the `__name__ == '__main__'` condition.




## Demo

Insert gif or link to demo


## Authors

- [@07MayankBhardwaj](https://github.com/07MayankBhardwaj)

