# Seeheimat | alps ~ wellness

![Am I Responsive](docs/am-i-responsive.PNG)
TODO: make responsive image here

**Developer: Paul Pfister**

💻 [Visit live website](https://)  
(Ctrl + click to open in new tab)

## Table of Contents

- [About](#about)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Design](#design)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Structure](#structure)
    - [Website pages](#website-pages)
    - [Database](#database)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
  - [Manual testing](#manual-testing)
  - [Automated testing](#automated-testing)
  - [Tests on various devices](#tests-on-various-devices)
  - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
- [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

### About

Seeheimat | alps ~ wellness is a business concept that offers wellness wellness treatments, gastro and accommodation all in one place - Seeheimat - translated from German means "home at the lake". The business is not existent right now but the concept is to offer a place where people can relax, eat and sleep all in one place. The business is located in the alps so the name is fitting for the location.

<hr>

### User Goals

- To create a booking for treatment service
- To be able to view edit and cancel bookings
- To view menus, a blog and contact info
- Fully responsive and accessible

### Site Owner Goals

- To provide a full web applicationto handle the bookings
- to organize the bookings and plan for the future
- Provide a modern application with an easy navigation

<hr>

## User Experience

### Target Audience

- Tourists visiting the area
- Past and new customers for the business
- People looking for a wellness treatment
- People with backpain or other issues that need treatment

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>

## User Stories

### Users

1. As a site user I can easily navigate through the site (Must have)
2. As a site user I can easily navigate through the site and see informations (Must have)
3. As a site user I want to see the team members of the company (Should have)
4. As a site user I want to easily contact the site owner (Must have)
5. As a site user I want to see the opening hours and the location of the company (Should have)
6. As a site user I want to easily book an appointment (Must have)
7. As a site user I want to read my bookings (Must have)
8. As a site user I want to update my booking (Must have)
9. As a site user I want to be able to delete my booking (Must have)
10. As a site user I want to get notified if an Action took place - so the site needs to write a message when operation with CRUD operations (Must have)
11. As a site user I expect that the site works on all common devices (Must have)
12. As a site user i want to see what services I can book (Must have)
13. As a User I can not book a table already booked so that my booking is valid and not double booked (Must have)
14. As a site user I want to book valid appointments - no dates in the past (Must have)
15. As a site user i want to login to CRUD my bookings (Must have)
16. As a site user I need to sign up to book an appointment (Must have)
17. As a site user I expect that just myself and the admin can see my bookings - so the bookings need to be filtered (Must have)

### Admin / Authorised User

18. As a site admin i can make a booking for my customers (Must have)
19. As a site admin I need to read all bookings and appointments (Must have)
20. As a site admin I need to be able to update all bookings (Must have)
21. As a site admin I need to be able to delete all bookings (Must have)
22. As an site admin I need to be able to to manage all bookable services (Must have)

### Site Owner

23. As a site owner I want to ship new informations and news into my blog so my current customers can get additional informations (Should have)
24. As a site owner I want that nobody can book the same appointment at a time (Must have)
25. As a site owner I need to accept or reject bookings to handle time (Must have)

### Milestones & User Stories

- GitHub Kanban was used to track all open user stories
- Milestones were used to track the progress of the project

####################

<details><summary>Milestones</summary>

![All Milestones](docs/milestones/milestones_all.PNG)
![Milestone 1](docs/milestones/milestone_1.PNG)
![Milestone 2](docs/milestones/milestone_2.PNG)
![Milestone 3](docs/milestones/milestone_3.PNG)
![Milestone 4](docs/milestones/milestone_4.PNG)

</details>

<details><summary>User Stories</summary>

![User stories](docs/user-stories/user-stories.PNG)

</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colors

I chose more light colors with low contrast to give the user a relaxing feeling when visiting the site. The colors are also used to give the user a feeling of being in the alps.

########################

### Structure

#### Website pages

The site was designed to be easy to navigate and user friendly. The user should immediately see what the business is for and what the offer is.

The footer also contains a social media link to the business' instagram site.

- The site consists of the following pages:
  - Home
  - Register
  - Login
  - Logout
  - Bookings
  - Bookings List
  - Edit Booking
  - Contact Us
  - Services (Treatments)
  - Blog
  - Blog Post Details
  - 404 Page
  - 500 Page

#### Database

- Built with Python and the Django framework with a database of CodeInstitute's Postgres - the project is deployed with heroku

<details><summary>Show diagram</summary>
<img src="docs/db-diagram.png">
</details>

##### User Model

The User Model contains the following:

- user_id
- password
- last_login
- is_superuser
- username
- email
- date_joined

##### Service Model

The Service Model contains the following:

- service_id
- name
- description
- price
- duration

##### Contact Model

The Contact Model contains the following:

- message_id
- name
- email
- subject
- message
- created_at

##### Booking Model

The Booking Model contains the following:

- booking_id (PrimaryKey)
- created_date
- requested_date
- requested_time
- service (ForeignKey)
- user (ForeignKey)
- name
- email
- status

##### Post Model

The Post Model contains the following:

- post_id (PrimaryKey)
- title
- slug
- author (ForeignKey)
- featured_image
- content
- created_on
- status
- excerpt
- updated_date

##### Comment Model

The Comment Model contains the following:

- comment_id (PrimaryKey)
- post (ForeignKey)
- author (ForeignKey)
- body
- approved
- created_on

### Wireframes

The wireframes were created using Balsamiq

#### Home

<details><summary></summary>
<img src="docs/wireframes/home.png">
</details>

#### Blog

<details><summary></summary>
<img src="docs/wireframes/blog.png">
</details>

#### My Bookings

<details><summary></summary>
<img src="docs/wireframes/booking_list.png">
</details>

#### booking

<details><summary></summary>
<img src="docs/wireframes/booking.png">
</details>

#### Contact Page

<details><summary></summary>
<img src="docs/wireframes/contact.png">
</details>

#### Login

<details><summary></summary>
<img src="docs/wireframes/login.png">
</details>

#### Services

<details><summary></summary>
<img src="docs/wireframes/services.png">
</details>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

########################
