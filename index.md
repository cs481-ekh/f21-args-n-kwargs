
## Project Abstract 
In an attempt to share university-owned equipment for making, processing, and characterizing materials with a wider community, many faculty member have been trying to establish and maintain a central repository to organize this information. Currently, a group attempts to catalog the information from various BSU departments so that it is organized for distribution. The information is then manually entered into a spreadsheet and shared other via a URL. This is a very time consuming and erroneous process of maintaining and disturbing this information. The proposal was to create a database with a web interface that can be used to manage and access the data.

We have built a web application that is hosted on BSU intranet that allows faculty and students to a place to manage and organize university-owned equipment. This application allows users to create, edit, update, and delete equipment items from a database. This improves the integrity of the data entered by validating the various form fields characterizing a piece of equipment. Furthermore, it enables a user to upload csv files to import data in a time efficient manner. This web application can be easily shared with a wider community via URL. This user-friendly application will greatly improve the experience in organizing the equipment owned by the University. 

## Members
- Ian Whitney
- Nick Stolarow
- Michael Cleverdon

## Project Description

For our Senior Capstone Project, we were tasked with creating a storage application for storing different pieces of equipment to replace our sponsor's current methodology for cataloging inventory: A large, shared Google Sheet. In this application, many pieces were built and then had to be integrated together to work seamlessly alongside each other.
- A login system. This was key to allow multiple people to have different functionality. Only certain people should be able to add, edit, or remove pieces of equipment, so the decision was made to create different groups that had different sets of permissions.
- A display system that can be used to search for specific pieces of equipment. We used JQuery DataTables since they came with search and sort functionality out of the box
- An upload system for csv files to make the addition of new items fast and simple
- Manual CRUD operations. A piece of equipment might break, or might be entered incorrectly, therefore it is required that the database should be able to be modified as needed. These functions are restricted to Faculty only.
- Security. It has been a big topic in the news recently, and there are proprietary pieces of equipment that might not to be shown to just anyone, so in order to keep that constrained, security was a priority while developing the application.


### The Login System
The login system was designed to allow only certain people to add or edit different pieces of equipment, but without the hassle of adding people into the user database manually. Thus, we created an authentication system that will let you sign up for an account and send a verification email to the newly created account's email. This goes back to the security topic that was listed earlier. Without a secondary authentication, there wouldn't be any way to prove that whoever signed up for an account with an email actually had access to that email. Anyone could say that they have a faculty boisestate account and gain access to every piece of equipment in the application, which isn't very secure at all. There is also a nice workflow for resetting password when people inevitably forget their password and need to reset it.
![Login Page](/assets/images/login.png)

### The DataTable
The datatable is the centerpiece of this project. It's what everyone who will be coming to the app will need to use in order to get the information they want. This means that it has to have data immediately visible that people would need to know. In order to fulfill all of these requirements best, we used the JQuery DataTables plugin that had builtin search and sorting features. But, because our UI space was limited, it was decided that the number of columns to display in the table would have to be limited. However, since hiding information from users isn't always the best idea, so we also incorporated a way to view all of the data on a piece of equipment by adding a popup view for the data. Overall, we feel like the UI has a cohesive design to it that promotes user interaction without any interruptions

### CSV Upload and Data Manipulation
The last part of our application is all about data manipulation, which is limited to people with faculty permissions. This includes adding items, removing items, or editing existing items. The best way to add multiple items in an easy fashion would be the CSV Upload functionality, which essentially boils down to:
- Downloading the template CSV file
- Filling it out
- Uploading it back to the app so the database can add all the new items

It's incredibly useful to be able to be able to add multiple items at once, but ultimately it might be easier just to add the one new item and be done with it. Which is why we also created a way to add a single item right from the home screen. In the top bar, there's a button called "Add Item" which will open a popup so that the fields can be filled out and the item can be created right then and there. Besides adding, there also is the ability to edit and delete items from the data table screen as well. As a faculty, there will be two buttons on the right of every piece of equipment. The pencil and paper icon is for editing, which will open a popup for editing. Once the changes have been made and the save button at the bottom has been clicked, the item will be updated in the database and the page will be updated to show the item's changes. Clicking the trashcan icon will show a popup asking to confirm the delete. This is to prevent accidentally clicking the trash can icon and instantlly deleting items from the database. When the confirm button has been clicked, the item will then be deleted from the database and the page will be reloaded to show the changes
