
<h1 align="center">Urban Pulse</h1>
<h3 align="center"> A YOLO based web app for Vehicle detection and counting</h3>
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"> 
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white">
  <img src="https://github.com/PRASUN-SITAULA/carbonWise/assets/89672957/106f3a07-d14a-4ee9-9e0c-c8cfbc635a79">
</p>


## Description
The current state of traffic management in Kathmandu, as well as many other urban areas
globally, is facing significant challenges. Conventional manual approaches have proven to be inadequate, leading to the development of a software-based solution that utilizes computer vision and deep learning. 
Our system utilizes a YOLO-based object detection model to address traffic management problems by implementing vehicle tracking, classification, counting, and speed measurement.

ROI has been employed which is also a necessary component for our software-based speed measurement. The implementation of this system can help to improve traffic
management and road safety.
<!-- <video src="https://github.com/PRASUN-SITAULA/carbonWise/assets/109226874/b4fc2eea-f489-45e3-9c49-d2fbfa681274"></video> -->


## Table of Contents

- [Features](#features)
- [Vehicle Classification](#Classification)
- [Technologies](#technologies)
- [Installation Guide](#installation-guide)
- [Screenshots](#screenshots)
- [Credits](#credits)
- [License](#license)


## Features
- **User Interface**: Clean and easy to navigate User Interface.
- **Vehicle Detection**: Detect vehicles on a particular Region of Interest.
- **Vehicle Counting**: Count vehicles based on classification type.
- **Speed Measurement**: Software based speed measurement of vehicles.


## Vehicle Classification
The system classifies the vehicles in six categories:
- **2 Wheeler**
- **Car**
- **Bus**
- **Minibus**
- **Truck**
- **Tempo**


## Technologies

This project is built using the following technologies:

- **React**: Frontend library for building user interfaces.
- **Vite**: Frontend build tool for faster development.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **FastAPI**: Creating API for integration.
- **YOLO**: Trained AI model for detecting vehicles.


## Installation Guide 

### Clone this repository
```bash
git clone https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking.git
```
### Go into the repository
```bash
cd Vehicle-Detection-and-Tracking
```
### Install packages
Navigate to the frontend directory
```bash
yarn install
```

Navigate to the app directory
```bash
pip install -r requirements.txt
```

### Run the server
Navigate to the app directory.
```bash
python api.py
```
### Run the Frontend
Navigate to the frontend directory
```bash
yarn dev
```
### Visit the Page
```bash
Open your browser and navigate to http://localhost:5173.
```


## Screenshots
<img width="942" alt="landing" src="https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking/assets/89672957/6ad6f8ee-bf5c-46db-abb5-385646aaca4d">

<img width="945" alt="feature1" src="https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking/assets/89672957/a9462374-73e7-4f96-b698-61e1dec2da34">

<img width="944" alt="feature2" src="https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking/assets/89672957/681f9e4c-39f9-465c-94ff-70054226a67a">

<img width="940" alt="feature3" src="https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking/assets/89672957/f74f8709-8dd7-4e6c-84ac-ebfd7502b81b">

<img width="953" alt="Upload" src="https://github.com/NayanPandey371/Vehicle-Detection-and-Tracking/assets/89672957/195270f2-f602-4725-9531-6cb2dddc8998">


## Credits
[Nayan Pandey](https://github.com/NayanPandey371)
[Nirmal Rana](https://github.com/CRei-7)
[Prasun Sitaula](https://github.com/PRASUN-SITAULA)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.