## Automated Traffic Sign Detection and Recognition (Prototype Phase)

## Project Overview

This project is part of my Final Year Project (FYP).  
The aim is to develop an **Automated Traffic Sign Detection and Recognition System** using **Deep Learning  

Currently, this submission is a **prototype version**, demonstrating:

- A login and registration system (with SQLite database).  
- A simple GUI (built using Tkinter).  
- An image upload feature.  
- Dummy recognition of traffic signs (random predictions).  

The prototype sets the foundation for the final system, where a trained deep learning model (CNN/YOLO) will be integrated.



## Features in Prototype
- User registration and login system.  
-  Upload image of a traffic sign.  
-  Display uploaded image in the UI.  
-  Dummy recognition of traffic signs (Stop Sign, Yield Sign, Speed Limit, No Entry).  
-  Modular code (database, auth, recognition, UI, main).  



##  Technologies Used
- **Python 3.10+**
- **Tkinter**  GUI framework  
- **SQLite3**  Local database  
- **PIL (Pillow)**  Image processing  
- **Random module**  For dummy recognition  



##  Project Structure

FYP-Traffic-Sign-Recognition-prototype
│
├── database.py # Handles database initialization and user data
├── auth.py # User login and registration logic
├── recognition.py # Dummy recognition logic (to be replaced with ML model later)
├── ui.py # User Interface (Login, Upload window)
├── main.py # Entry point of the application
└── README.md # Project documentation



## Prototype Workflow

- User registers or logs in.

- User uploads a traffic sign image.

- The system displays the image.

- A dummy recognition label is shown (random prediction).


## Future Work (Final FYP)

- Integrate a real deep learning model (CNN/YOLO) for recognition.

- Use datasets like GTSRB, LISA, or custom datasets.

- Add real-time video stream recognition.

- Improve the GUI (PyQt or mobile app version).

- Deploy as a desktop app or Android application.


## Supervisor

- Name: Zaid Ismail
- Email: zaid.ismail@vu.edu.pk


## Author

- Name: Yahya
- Reg # BC230415847
- kakakhel49@yahoo.com
