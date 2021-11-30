
## Project Abstract 
In an attempt to share university-owned equipment for making, processing, and characterizing materials with a wider community, many faculty member have been trying to establish and maintain a central repository to organize this information. Currently, a group attempts to catalog the information from various BSU departments so that it is organized for distribution. The information is then manually entered into a spreadsheet and shared other via a URL. This is a very time consuming and erroneous process of maintaining and disturbing this information. The proposal was to create a database with a web interface that can be used to manage and access the data.

We have built a web application that is hosted on BSU intranet that allows faculty and students to a place to manage and organize university-owned equipment. This application allows users to create, edit, update, and delete equipment items from a database. This improves the integrity of the data entered by validating the various form fields characterizing a piece of equipment. Furthermore, it enables a user to upload csv files to import data in a time efficient manner. This web application can be easily shared with a wider community via URL. This user-friendly application will greatly improve the experience in organizing the equipment owned by the University. 


## Project Description

For our Senior Capstone Project, we were tasked with creating a storage application for storing different pieces of equipment to replace our sponsor's current methodology for cataloging inventory: A large, shared Google Sheet. In this application, many pieces were built and then had to be integrated together to work seamlessly alongside each other.
- A login system. This was key to allow multiple people to have different functionality. Only certain people should be able to add, edit, or remove pieces of equipment, so the decision was made to create different groups that had different sets of permissions.
- A display system that can be used to search for specific pieces of equipment. We used JQuery DataTables since they came with search and sort functionality out of the box
- An upload system for csv files to make the addition of new items fast and simple
- Manual CRUD operations. A piece of equipment might break, or might be entered incorrectly, therefore it is required that the database should be able to be modified as needed. These functions are restricted to Faculty only.
- Security. It has been a big topic in the news recently, and there are proprietary pieces of equipment that might not to be shown to just anyone, so in order to keep that constrained, security was a priority while developing the application.


- How it works
- Screenshots
