<h1 align="center">Contemporary Software Development Final Year Project 

<h2 align="center"> 🌍  </h2>

## **Project Introduction and Brief**

### *Title: **[Carbonprint Emissions Site](https://github.com/NeiloErnesto89/carbonprint)** - an carbon footprint tracker website and community*

*ATU DONEGAL - CSD Project - Django Framework Python*

This is a site aimed at people interested in being more ecofriendly who want to have a personalised experience and track their own carbon emissions.

*The Figures below show the current home page and the flight tracker section on mobile view*

![home](/media/readme_docs/home_page_carbonprint.png "Current Home Page Browser" ) <h2>

*Figure x. Current Home Page on Browser*

![mvc](/media/readme_docs/flight_tracker_page_mobile.png "Flight Tracker Section Mobile with Dropdown" ) <h2>

*Figure x. Flight Tracker Section Mobile View with Responsive with Dropdown (Hamburger Icon)*


Keeping in line with the project requirements 

### *Note for Tester*

*For the **testing purposes**, I suggest (at some stage) logging into the site as the **Admin/SuperUser**, using the following details*: 
- Username: **admin**   
- Password: **XXXXX** 

**Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Requirements**](#requirments)
- [**Design**](#design)
    - [Wireframes](#wireframes)
- [**Database**](#database)
	- [**Dataebase Schema**](#database-schema)
- [**Implementation**](#implementation)
- [**Features**](#features)
	- [Existing features](#existing-features)
	- [Features left to implement](#features-left-to-implement)       
- [**Technology**](#technology)
- [**Testing**](#testing)	
    - [Unit Tests](#unit-tests)
    - [User Experiences](#user-experiences)
- [**Bugs**](#bugs)
- [**Credits**](#credits)
	- [Content](#content)
	- [Acknowledgements](#acknowledgements)

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


![mvc](/media/readme_docs/djang_architecture.png "MVC" ) <h2>

*Figure x. Django MVC Architecture*

## **Database**

SQLite is a lightweight, serverless, file-based database engine that doesn't require a separate database server to run nor any configuration, and, according to the SQLite official documentation (SQLite, 2023) it is the “most widely deployed database in the world”. 

#### **Database Schema**

![database schema](/media/readme_docs/CSW_Project_DB_Schema.png "Django Database Schema" ) <h2>

*Figure x. Django Database Schema utilising Models/Class*

## **Credits** 

Credit Interview Bit of the MVC Figure 1. Django Database Schema utilising Models/Class
Credit ATU Donegal for the project brief and requirements
Credit to StackOverflow for the many questions and answers that helped me along the way