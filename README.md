<h1 align="center">Contemporary Software Development Final Year Project 

<h2 align="center"> 🌍  </h2>

## **Project Introduction**

### *Title: **[Tracking your Carbon Footprint: A Python (Django) Sustainability Application](https://github.com/NeiloErnesto89/carbonprint)** - an carbon footprint tracker website and community*

*ATU DONEGAL - CSD Final Report Project - Django Framework Python Artefact*

This is a site aimed at people interested in being more ecofriendly who want to have a personalised experience and track their own carbon emissions.

*The Figures below show the current home page and the flight tracker section on mobile view*

#### Figure 1. Current Home Page on Browser
![home](/media/readme_docs/home_page_carbonprint.png "Current Home Page Browser" ) <h2>


#### Figure 2. Flight Tracker Section Mobile View with Responsive with Dropdown (Hamburger Icon)
![mvc](/media/readme_docs/flight_tracker_page_mobile.png "Flight Tracker Section Mobile with Dropdown" ) <h2>



### *Note for Tester*

*For the **testing purposes**, I suggest (at some stage) logging into the site as the **Admin/SuperUser**, using the following details*: 
- Username: **admin**   
- Password: **XXXXX** - provided in project report*

It's also important to note that an API secret key will need to be generate from the sites: Climatiq and OpenWeatherMap. These keys will need to be added to the **.env** file in the main directory of the **carbonprint** project.

**Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Requirements**](#requirements)
- [**Design**](#design)
- [**Database**](#database)
	- [**Database Schema**](#database-schema)
- [**Implementation**](#implementation)
- [**Testing**](#testing)
- [**Credits**](#credits)


## **Project Introduction**
The purpose of this project is to build a user-friendly web application to help user track and view their carbon footprint. The application will aim to enhance the users experience by providing up-to-date metrics and personalised feedback (via the users inputted information).

## **Requirements**

The following section details the requirements of the project. Functional requirements outline what a system can and cannot achieve, via the users’ actions. 

### *Software Requirements*
This application will be developed using the following software:
- Python 3.10.5
- Django
- HTML, CSS, JavaScript
- Git


## **Design**

The Django framework operates with an MVC (Model-View-Controller) pattern whereby, the model (like a class) defines the data structure, the view is the UI being presented to the user and the controller connects them together with programmatic logic.

#### Figure 3. Django MVC Architecture
![mvc](/media/readme_docs/djang_architecture.png "MVC" ) <h2>


## **Database**

SQLite is a lightweight, serverless, file-based database engine that doesn't require a separate database server to run nor any configuration, and, according to the SQLite official documentation (SQLite, 2023) it is the “most widely deployed database in the world”. 

### **Database Schema**
#### Figure 3. Django Database Schema utilising Models/Class
![database schema](/media/readme_docs/CSW_Project_DB_Schema.png "Django Database Schema" ) <h2>




## **Implementation**

Steps detailed of the implementation chapter of the project report. Models, Views, URL Routes and Templates and how they function together are all detailed in the report.

## **Testing**

Unit tests and manual tests undertaken to ensure the application is working as expected.

## **Credits** 

Credit Interview Bit of the MVC Figure 1. Django Database Schema utilising Models/Class
Credit ATU Donegal for the project brief and requirements
Credit to StackOverflow for the many questions and answers that helped me along the way