# __Rave Reviews__

![Mockup image](documentation/images/device-display.jpg)

[Live webpage](https://rave-reviews-app.herokuapp.com/)

This is the website for Rave Reviews. It is my third milestone project for the Code Institute Level 5 Diploma in Web Application Development. It has been designed with the focus of creating 'CRUD' functionality and to be responsive and accessible on all devices. Rave Reviews is a site accessed via registering an account and it was created for like-minded Drum and Bass enthusiasts to share their experiences and sets of their favourite raves / club nights and online events. The site utilises user authentication ensuring only those with accounts can access the content, leave reviews and comment on the reviews. The authentication also allows admin users to have privileges that access otherwise restricted areas as well as control over the content of the site and the users' reviews, comments, and uploads. Amazon S3 bucket has been used to allow the user to upload images to their profile page and when leaving a rave review.

## __CONTENTS__

1. [User Experience](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)

2. [Design](#design)
  * [Appearance & Colour Scheme](#appearance--colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database](#database)

3. [Features](#features)
  * [Base template Features](#base-template-features)
  * [Main Content Features](#main-content-features)

4. [Future Implementations](#future-implementations)

5. [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Databases](#databases)
  * [Frameworks](#frameworks)
  * [Libraries & Packages](#libraries--packages)
  * [Programs](#programs)

6. [Testing](#testing)

7. [APIs](#apis)

8. [Deployment](#deployment)
  * [Amazon Webservices](#amazon-webservices)
  * [Mongo Database](#mongo-database)
  * [Local Deployment](#local-deployment)
  * [Heroku](#heroku)

9. [Credits](#credits)

10. [Content](#content)

11. [Media](#media)

12. [Acknowledgements](#acknowledgements)

_ _ _

## __User Experience__

### __Project Goals__

I decided to create Rave Reviews based on my love for Drum and Bass as a teenager and into my early 20's. My friends and I are always discussing raves we've been to and the sets from them. Sharing our favourite tunes and sets so I thought it would be great to have a place all these recordings and memories could be stored.

In a sense this would be like a Facebook page but specifically for Drum and Bass enthusiasts where they can review raves, 
comment on others and share their favourite sets.

### __User Stories__

#### __Target Audience__

Target audience is for anyone with an interest in Drum and Bass. While raves are for 18-year-olds and over, the age one can appreciate the music and experiences from fellow enthusiasts is any age, so it would be restrictive to set a specific target audience. That said, I would imagine it will appeal mostly to those aged 16 - 50 as those are the ages that will have experienced joys of Drum and Bass and the raves most since its birth in the mid 90's.

#### __First Time Visitor Goals__

As a first-time user of the site I want to be able to:

1. Understand what the site is for and how to navigate through site.
2. Register for an account and create a profile.
3. Find rave reviews.
4. Create a rave review.

#### __Returning Visitor Goals__

As a returning registered user of the site, I want to be able to:

5. Log in to my account.
6. Create, edit, delete, and view my rave reviews.
7. Edit, delete and view my profile.
8. Search for other rave reviews from other members.
9. Leave comments for other members to read.

#### __Admin User__

As an administrator for the site I want to be able to:

10. Add, edit, or delete organisations.
11. Remove any content that could be offensive.
12. Ensure defensive programming to avoid deletions by mistake
13. Ensure defensive programming so a logged-out user can't access areas of the website only accessible via log in.

#### __Site Owner__

14. Automatically return a logged-out user to the logged-out home page, or anyone but Admin from restricted pages to the logged-in Home page if logged-in.
15. Relevant error page displayed should an invalid command or error occur.
16. I want the user to be able to contact me should they have any questions.

- - -

## __Design__

### __Appearance & Colour Scheme__

My aim is to make the site feel urban / street as Drum and Bass (DnB) is a raw music genre with its roots firmly set in the poorer areas of UK cities.
I designed my own logo in Illustrator and used oranges against dark grey and black as my colours reflecting the bright energy the music brings and the dark
and shady venues Dnb raves are held at. The 'DnB' is only used for the home page, and I created a bright electric blue styling for this to emulate the 
light shows and lasers you get in a rave.

![Colour Scheme](documentation/images/colour-palette.png)

![Logos](documentation/images/logos.png)

### __Typography__

To continue the urban theme, I chose a graffiti style font called 'PhillySans' and for main written text and a strong and easy-to-read.
sans serif font from the Google Fonts Library called 'Merriweather Sans'.

![PhillySans](documentation/images/phillysans.png)

![Merriweather Sans](documentation/images/merriweathersans.png)

### __Imagery__

As the members of Rave Reviews are able and encouraged to upload their own images, I have kept the site free from too many images. 
The times that images are used they are of pictures I have taken from raves I've attended.

### __Wireframes__

Wireframes have been designed for mobile, tablet and desktop.

<details><summary>Home</summary>
<img src="documentation/wireframes/index.png">
</details>
<details><summary>Register / Edit Profile</summary>
<img src="documentation/wireframes/register_edit_profile.png">
</details>
<details><summary>Login</summary>
<img src="documentation/wireframes/login.png">
</details>
<details><summary>Profile</summary>
<img src="documentation/wireframes/profile.png">
</details>
<details><summary>Rave Reviews</summary>
<img src="documentation/wireframes/raves.png">
</details>
<details><summary>Add / Edit Review</summary>
<img src="documentation/wireframes/add_edit_rave.png">
</details>
<details><summary>Organisations</summary>
<img src="documentation/wireframes/organisations.png">
</details>
<details><summary>Add / Edit Organisations</summary>
<img src="documentation/wireframes/add_edit_organisation.png">
</details>
<details><summary>Errors</summary>
<img src="documentation/wireframes/errors.png">
</details>
<details><summary>Contact</summary>
<img src="documentation/wireframes/contact.png">
</details>
<details><summary>Delete Modal</summary>
<img src="documentation/wireframes/delete_modal.png">
</details>

- - -

## __Database__

* The website is a data-centric one with HTML, CSS, Javascript and the Materialize framework as a frontend.
* The back end consists of Python and Flask, Jinja templates with a database of MongoDB open-source document-orientated database.

#### __User Journey__

![User Journey](documentation/images/rr_database_model.png)

#### __Database Schema__

![Database Schema](documentation/images/schema.png)

#### Mongo DB
- Mongo DB was used for the project as I knew project 4 would be using PostgreSQL and I am keen to understand both and their differences
- As Mongo DB is a NoSQL database, it stores data in a flexible, schema-less format using JSON-like documents. This can be advantageous for projects with evolving data schemas or when dealing with unstructured data, like user-generated content and reviews
- Upon review of both there's no reason why either couldn't be used but where users will have different information in their profiles and reviews Mongo DB's flexibility might also mean it's the more suitable option for this project

- rave_reviews database was created to store site information; it contains four collections described below:
  1. users - to store registered user information
  2. organisations - to store rave organisation information added by an admin user
  3. raves - to store the rave review information added by an admin/regular user
  4. comments - to store comment information for a review added by an admin/regular user

#### Users
- The users collection is used to store user information when they register and display it on their profile page
- The fields stored in the collection are user's username (String), password (String), first_name (String), last_name (String), fave_dj (String), fave_mc (String), fave_venue (String), fave_organisation (String), fave_set (String) with a unique identifier (primary key), "_id"(ObjectId)
- The user's password is encrypted using a generate_password_hash from a werkzeug.security Python library
- This allows users to return to the site, log in and access the sites content and features
- User stories covered: 2, 3, 4, 5, 7

  ![Users](documentation/images/users.png)

#### Organisations
- The organisations that reviews are added to are added by an admin user and displayed as selectable options when leaving a review
- The fields stored in the collection are the organisation name (String) with a unique identifier (primary key), "_id"(ObjectId)
- This allows admin to add, edit or remove organisations from the options panel when adding a review
- User stories covered: 10

  ![Organisations](documentation/images/organisations.png)

#### Raves
- Rave Reviews are added by regular and admin users
- The fields stored in the collection are the organisation_name (String), rave_image (String), rave_name (String), date (String), venue (String), rave_description (String), rave_set (String), banger (String), created_by (String) with a unique identifier (primary key), "_id"(ObjectId)
- When a user adds a review, it stores the organisation name (from the options in the organisations table) and a created_by (taken from the users table username field of the user who added the review) to create a link between the two collections
- The rave_name and rave_description have search indexes set up for searching functionality.
- Once the review is added it is stored in the reviews page allowing users access all review, to search for specific reviews or find their own reviews and edit or delete them
- Admin can delete any review
- User stories covered: 4, 6, 8, 11


  ![Raves](documentation/images/raves.png)

#### Comments 
- Comments are added to a review by a regular or admin user
- The fields stored in the collection are the comment_text (String), comment_created_by (String), commment_id (ObjectId) with a unique identifier (primary key), "_id"(ObjectId)
- When a user adds a comment, it stores the comment_id as the primary key of the review (taken from the _id in the raves table) and the comment_created_by field as the username of the user (taken from the username in the users table) who added the comment. This creates a link between the two collections and displays the user's name and comment on the correct review
- Once the comment is left it is displayed under the content of the review, for all users to read
- Admin can delete any comment
- User stories covered: 9, 11 

  ![Comments](documentation/images/comments.png)

#### __Amazon Web Services S3 Bucket__

While Mongodb stores the majority of the users' data in the database, images are stored in an Amazon Web services (AWS) S3(storage) bucket. I made this choice for performance purposes and so I could learn how to integrate the site with AWS, encouraging me to learn new skills while building the website.

![S3 Bucket](documentation/images/rave_review_bucket.png)

- - -

## __Features__

### __Base Template Features__

* __Favicon__ - I designed the favicon in Illustrator, the two 'R's form the logo which is also used as the home link in the left of the Navbar.

  ![Rave Reviews favicon](documentation/images/features/favicon.png)

* __Navbar__ - The Navbar is displayed on all pages and changes depending on whether the user is logged in or out or if admin when Organisations is then visible.

  Logged Out Navbar
  - Log In, Register & Home links
  - User Stories covered: 1, 2 & 5, 14

  ![Logged Out Navbar](documentation/images/features/logged-out-navbar.png)

  Logged In Navbar
  - Home, Profile, Rave Reviews, Leave Reviews & Log Out Links
  - User stories covered: 3, 4, 6 & 7

  ![Logged In NavBar](documentation/images/features/logged-in-navbar.png)

  Admin Logged In Navbar
  - Home, Profile, Rave Reviews, Leave Reviews, Organisation & Log Out Links
  - User stories covered: 10 & 11

  ![Admin Logged In NavBar](documentation/images/features/admin-logged-in.png)

* __Footer__ 
- The footer is displayed on all pages and includes social links, my GitHub link to this repository, a link to the contact page, the copyright year, and the logo.
- User stories covered: 16

  ![Footer](documentation/images/features/footer.png)

### __Main Content Features__

There are 14 pages which extend from a base template;

* __Logged Out Home__
* __Logged In Home__
* __Login__
* __Register__
* __Profile__
* __Edit Profile__
* __Rave Reviews__
* __Add Rave Review__
* __Edit Rave Review__
* __Organisations__
* __Add Organisations__
* __Edit Organisations__
* __Contact__
* __Errors__

### Logged Out Home
- Introduction to the site
- Log In or Register Button
- User redirected here if not logged in
- User Stories covered: 1, 2, 5 & 14

![Logged Out Home](documentation/images/features/logged-out-home.png)

### Logged In Home
- Navigation buttons to user reviews, rave reviews & leave review
- User stories covered: 3, 4, 6 & 7

![Logged In Home](documentation/images/features/logged-in-home.png)

### Login
- User name and password form input
- User stories covered: 5

![Login](documentation/images/features/login.png)

### Register
- Form with requirements that build the profile
- User stories covered: 2

![Register](documentation/images/features/register.png)

### Profile
- Features the details from the registration form
- Buttons for edit or delete profile and user's reviews with defensive modal or delete option
- User stories covered: 6, 7 & 12

![Profile](documentation/images/features/profile.png)

### Edit Profile
- Same form as registration with selected fields populated with the profile information
- User stories covered: 7

![Edit Profile](documentation/images/features/edit-profile.png)

### Rave Reviews
- Search for reviews
- Button for user's reviews
- Option to edit user's reviews
- Leave comments on all reviews
- Delete option if user's review with defensive modal
- User stories covered: 6, 8, 9 & 12

![Rave Reviews](documentation/images/features/rave-reviews.png)

![Rave Review](documentation/images/features/rave-review.png)

### Add Rave Review
- Form with requirements to create the review
- User stories covered: 4 & 6

![Add Rave Review](documentation/images/features/add-rave-review.png)

### Edit Rave Review
- Same form as add rave review with selected fields populated with the review information
- User stories covered: 6

![Edit Rave Review](documentation/images/features/edit-rave-review.png)

### Organisations
- Only accessible as 'Admin' user, user redirected to home if not Admin
- Edit or delete options for all organisations with defensive modal for delete button
- User stories covered: 10, 12 & 13, 14

![Organisations](documentation/images/features/organisations.png)

### Add Organisation
- Input field for organisation name
- User stories covered: 10

![Add Organisation](documentation/images/features/add-organisations.png)

### Edit Organisation
- Input field for organisation name
- User stories covered: 10

![Edit Organisation](documentation/images/features/edit-organisations.png)

### Contact
- Contact form that contacts the site owner directly via emailjs
- User stories covered: 16

![Contact](documentation/images/features/contact.png)

### Errors
- Specific error page returned depending on the error
- User stories covered: 15

![Errors](documentation/images/features/errors.png)

### Delete Modals
- Defensive programming has been used to avoid accidental deletions
- Anything with a delete option will have a modal pop up confirming the delete is intended.
- User stories covered: 12

![Delete](documentation/images/features/delete.png)

### Admin User Specifics
- Can delete or update any review that is offensive
- Can delete any comments that are offensive
- User stories covered: 11 

![Delete/Edit](documentation/images/features/delete-comments.png)

### Future Implementations

I am content with what was implemented but if I had more time there are a few bonus features I think could be added;

* Add site users with different privileges to avoid using jinja templating and one 'Admin' log in that has a superior role.
* Add change and reset password functionality to the profile section.
* Allow users to see other users profiles by clicking on their name under the review.
* Email verification to enhance user protection when logging in.
* Extend the css with an scss file allowing a cleaner css file and a more customisable Materialize-based site. I did attempt this and had it the files working on my site but ran out of time to troubleshoot why the Materialize secondary colours were not changing, so I removed it.
* Delete images from the S3 bucket when profiles or reviews are deleted. Sadly, I had no time to look in to this but as there is so much space in the bucket I don't see it as a problem. 
* On reflection I would not use Materialize, it is too restrictive and doesn't offer anywhere near as much styling or customisation as Bootstrap.

_ _ _

## __Technologies Used__

## Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Jinja]((https://jinja.palletsprojects.com/en/3.0.x/))

### Databases

- [MongoDB](https://www.mongodb.com/) - Non-relational database used to store the Rave Reviews information.
- [AWS S3](https://aws.amazon.com/s3/) - Services that provides object storage through a web service interface.

### Frameworks

- [Flask](https://pypi.org/project/Flask/) - A micro framework.
- [Materialize 1.0.0.](https://getbootstrap.com/) - Responsive CSS Framework. 

### Libraries & Packages

- [PyMongo](https://pypi.org/project/pymongo/) - Python Driver for MongoDB.

### Programs

- [Pip](https://pypi.org/project/pip/) - Tool for installing python packages.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
- [Git](https://git-scm.com/) - For version control.
- [Github](https://github.com/) - To save and store the files for the website.
- [GitPod](https://www.gitpod.io/) - A cloud development environment.
- [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.
- [Tiny PNG](https://tinypng.com/) To compress images for use in the readme.
- [Visual Studio Code](https://code.visualstudio.com/) - An integrated development environment from Microsoft.
- [Adobe Suite (Illustrator, Photoshop & InDesign)](https://www.adobe.com/uk/) - Graphic design software.
- [Giphy](https://giphy.com/) - Video to gif conversion website for user story testing section.
- [Font Awesome](https://fontawesome.com/search) - The icons used on the site from font awesome.
- [Diagrams.net](https://app.diagrams.net/) - Flow chart maker used for database models.
- [W3C validator](https://validator.w3.org/) - HTML validation testing.
- [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) - CSS validation testing.
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Accessibility testing.
- [jshint](https://jshint.com/) - Javascript validation testing.
- [pep8](http://ww7.pep8online.com/) - Python validation testing.
- [Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) - For performance, accessibility, progressive web apps, SEO analysis of the project code

_ _ _

## __Testing__

The testing information and results for this project are documented in [TESTING.md](TESTING.md)

_ _ _

## __APIs__

### Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid
3. Create an email service in the Email Services section and note the id
4. Create an email template in the Email templates section and note the id
5. Update the script sendEmail.js, method sendMail with your user id, email service id and email template id.

_ _ _

## __Deployment__

There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

### Amazon Web Services
1. Create an account at https://aws.amazon.com
2. Open the IAM application and create a new user
3. Set the AmazonS3FullAccess for the user and note the users AWS ACCESS and SECRET keys
![Iam](documentation/images/iam.png)
4. Open the S3 application and create a new bucket. For the purpose of this application the bucket name is rave-reviews-bucket but this can be updated.
5. With security best practices update the public access and policy bucket to enable the user created and the application access to read/write to the S3 bucket. Consult the AWS documentation if required: https://aws.amazon.com/s3/
![Policies](documentation/images/access.png)
6. The s3 bucket is now updated to be accessed by your application.
7. In necessary route files update the variables BUCKET and image_url with the correct information that you have set up, for example:
<br>
<code>BUCKET = "rave-reviews-bucket"</code><br>
<code>image_url = "https://rave-reviews-bucket.s3.eu-west-1.amazonaws.com/" </code>


### Mongo Database
Mongodb is the database used in the application
1. Create an account at mongodb
2. Create a database cluster
3. Select the cluster, and in the collections section create a database and create 4 collections under the database: raves, organisation, users & comments.
![Database](documentation/images/database.png)
4. In the database access, create a user and allow the user read/write access. Note the username.
5. In the network access tab, allow network access from the ip-address of the application connecting to the database.
6. In the Databases section click Connect, and select connect your application.
7. Note the MONGO_URI, MONGO_DBNAME and user, these parameters are used when deploying locally(env.py file) and deploying on the likes of heroku(config vars).

### Local Deployment
To run this project locally, you will need to clone the repository.
1. Login to GitHub (https://wwww.github.com).
2. Select the repository jamie2210/CI_MS3_RR.
3. Click the Code button and copy the HTTPS url, for example: https://github.com/jamie2210/CI_MS3_RR
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/jamie2210/CI_MS3_RR```

5. The repository will now be cloned in your workspace.
6. Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code><br>
<code>os.environ.setdefault("IP", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("PORT", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_URI", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_DBNAME", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
7. Install the relevant packages as per the requirements.txt file
8. Start the application by running <code>python3 app.py</code>

### Heroku
To deploy this application to Heroku, run the following steps.
1. In the app.py file, ensure that debug is not enabled, i.e. set to True.
2. Create a file called ProcFile in the root directory, and add the line <code>web: python app.py</code> if the file does not already exist.
3. Create a requirements.txt file by running the command <code>pip freeze > requirements.txt</code> in your terminal if the file doesn't already exist.
5. Both the ProcFile and requirements.txt files should be added to your git repo in the root directory.
6. Create an account on heroku.com.
7. Create a new application and give it a unique name.
8. In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo.
![Heroku dashboard](documentation/images/heroku_dashboard.png)
9. Select the branch for example master and enable automatic deploys if desired. Otherwise, a deployment will be manual
10. The next step is to set the config variables in the Settings section
![Config vars](documentation/images/config.png)
11. Set key/value pairs for the following keys: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY
12. Go to the dashboard and trigger a deployment
![Deploy](documentation/images/deploy.png)
13. This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app.
14. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue.

_ _ _

## __Credits__

* [Materialize](https://materializecss.com/) is used throughout for CSS styling and some javascript / jquery

* For Help with using AWS S3 buckets and python these were all very useful;

    https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2

    https://www.twilio.com/blog/media-file-storage-python-flask-amazon-s3-buckets

    https://blog.filestack.com/tutorials/upload-files-amazon-s3-bucket-using-python/

    https://www.youtube.com/watch?v=QSvw50mMQaQ

    https://www.youtube.com/watch?v=7gqvV4tUxmY

*   When adding a password confirmation Javascript feature that only enables the register button once both password entries are the same, this tutorial was very helpful;

    https://www.youtube.com/watch?v=n5E_gxkLo6A

*  For the pagination of the reviews these articles were of great help;

    https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

    https://pythonhosted.org/Flask-paginate/

    and these tutorials;

    https://www.youtube.com/watch?v=CnBYLXA9zXY

    https://www.youtube.com/watch?v=PSWf2TjTGNY&t=61s

* For the send-email functionality I used some code from the code institute learning platform.

* I used this stack overflow page to better understand exception handling;

  https://stackoverflow.com/questions/33239308/how-to-get-exception-message-in-python-properly

* For a better understanding on how to check for YouTube links in javascript I used this stack overflow thread;

  https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box

_ _ _

## __Content__

- [Font Awesome](#http://fontawesome.com)    
    - The icons used on the site from font awesome.
    
- Fonts<br>
    [Merriweather-sans](#https://fonts.google.com/specimen/Merriweather+Sans)    
    - The text font Merriweather Sans is from Google fonts
  
  [PhillySans](#https://www.dafont.com/philly-sans.font)
    - PhillySans was taken as a free font for personal use from dafont.

_ _ _ 

## __Media__

All images are either photos taken by me or uploaded by users of the site

All logos are designed by myself

_ _ _

## __Acknowledgements__

I would like to take the opportunity to thank;

- My mentor, Mo Shami, for his excellent feedback, advice support and guidance throughout.
- Tutor support from Code Institute for their swift response.
- The slack community of coders for immediate and helpful response.
- WAES College and my Tutor Michael for their support and help throughout.
- My friends and family who have created accounts and tested the site and given valid feedback helping me fix bugs I was otherwise unaware of.