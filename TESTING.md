# __Rave Reviews Testing__

![Mockup image](documentation/images/device-display.jpg)

[Live webpage](https://rave-reviews-app.herokuapp.com/)

## __Contents__

1. [Automated Testing](#automated-testing)
    * [HTML Validation](#HTML-validation)
    * [CSS Validation](#CSS-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
    * [Accessibility](#accessibility)
    * [Performance](#performance)
2. [Manual Testing](#manuel-testing)
    * [Device testing](#performing-tests-on-various-devices)
    * [Browser compatibility](#browser-compatibility)
    * [Testing user stories](#testing-user-stories)
3. [Bugs](#bugs)

I consistently tested throughout the build of the project with Chrome developer tools, utilising print statements in python and checking for device compatibility at each stage opf the development.
_ _ _ 

## __Automated Testing__

### __HTML Validation__

The W3C Markup Validation Service was used to validate the HTML of the website. All pages pass with no errors.

Logged Out Home [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2F)

Logged In Home [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Flogged_in_home)

Log In [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Flogin)

Register [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fregister)

Profile [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fprofile%2Fdnbharry)

Edit Profile [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fedit_profile%2F644ff1b57bd099cfccc82783)

Get Raves [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fget_raves%2F)

Add Rave [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fadd_rave)

Edit Rave [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fedit_rave%2F64512efa538d5c6ccbaf95c4)

Get Organisations [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fget_organisations)

Add Organisations [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fadd_organisation)

Edit Organisations [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fedit_organisation%2F64568e7130db687d1fc3cac1)

Contact [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2Fcontact)

Errors [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Frave-reviews-app.herokuapp.com%2F457hdfr)


### __CSS Validation__

The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
When pasting in my index errors and warnings were flagged all linked to Materialize.

When validating just my own custom CSS file it passes with no errors with only 1 warning as it could not read the Google Fonts import.
<details><summary>style.css</summary>
<img src="documentation/testing/css_validation.png">
</details><br>

### __JavaScript Validation__

JSHint JS Validation Service was used to validate the Javascript files. No significant issues were found. Only undefined variables flagged were those used for the emailjs functions.

OnClick buttons were flagged as unused, but /* exported */ feature was used to remove the flags as they are called in the html files.

<details><summary>script.js</summary>
<img src="documentation/testing/jshint.png">
</details><br>

### __Python Validation__

[pep8ci](#https://pep8ci.herokuapp.com/) was the linter used to check the python code, all clear with no errors.
<br>

<details><summary>Index</summary>
<img src="documentation/testing/linter/index.png">
</details>

<details><summary>Authentication</summary>
<img src="documentation/testing/linter/authentication.png">
</details>

<details><summary>Raves</summary>
<img src="documentation/testing/linter/raves.png">
</details>

<details><summary>Organisations</summary>
<img src="documentation/testing/linter/organisations.png">
</details>

<details><summary>Error Handlers</summary>
<img src="documentation/testing/linter/error-handlers.png">
</details>
<br>

### __Accessibility__

To ensure the site is accesible as possible I have taken the following steps;

- Using semantic HTML.
- Descriptive alt attributes on images.
- Label functions and links to ensure clarity of the roles of each button, icon or clickable feature.
- Ensuring that there is a sufficient colour contrast throughout the site (There are contrast flags throughout the WAVE reporting but I am happy with the way the site is represented in these case as a low contrast was my intention and part of the design. I am happy with the visiblility of each flag so have left them as they are and they are all labelled with descriptions.)

[Wave accessibility](#https://wave.webaim.org/) was used to test the websites accessibility

All pass with no errors apart from the forms as the drop down option has no form label which is a Materialize feature and something I can not adjust.

Due to the log in WAVE can only access limited links these are sahred for demonstration to how the rest of the sites pages are structured for optimal accessibility.

Logged Out Home [results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/)

Log In [results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/login)

Register [Results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/register)

Errors [Results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/profile/)

### __Performance__

Performance testing was done using lighthouse in chrome developer tools testing the performance, accessibility, best practices and SEO of the website. Some of the scores are lower than I'd like them to be but for most of them, the lower ones especialy, it was from labels or formatting within Materialize I which I could not change so it's not something I'm too worried about.
<br>
<details><summary>Logged Out Home</summary>
<img src="documentation/testing/lighthouse/logged-out-home.png">
</details>

<details><summary>Logged In Home</summary>
<img src="documentation/testing/lighthouse/logged-in-home.png">
</details>

<details><summary>Log In</summary>
<img src="documentation/testing/lighthouse/login.png">
</details>

<details><summary>Register</summary>
<img src="documentation/testing/lighthouse/register.png">
</details>

<details><summary>Profile</summary>
<img src="documentation/testing/lighthouse/profile.png">
</details>

<details><summary>Edit Profile</summary>
<img src="documentation/testing/lighthouse/edit-profile.png">
</details>

<details><summary>Get Raves</summary>
<img src="documentation/testing/lighthouse/get-raves.png">
</details>

<details><summary>Add Rave</summary>
<img src="documentation/testing/lighthouse/add-rave.png">
</details>

<details><summary>Edit Rave</summary>
<img src="documentation/testing/lighthouse/edit-rave.png">
</details>

<details><summary>Organisations</summary>
<img src="documentation/testing/lighthouse/organisations.png">
</details>

<details><summary>Add Organisation</summary>
<img src="documentation/testing/lighthouse/add-organisation.png">
</details>

<details><summary>Edit Organisation</summary>
<img src="documentation/testing/lighthouse/edit-organisation.png">
</details>

<details><summary>Contact</summary>
<img src="documentation/testing/lighthouse/contact.png">
</details>

<details><summary>Errors</summary>
<img src="documentation/testing/lighthouse/errors.png">
</details>

_ _ _

## __Manuel Testing__

### __Device testing__
The website was tested on the following devices:
- MacBook Pro
- iPad Tablet
- Google Pixel 5
- iPhone 12

In addition, the website was tested using Google Chrome Developer Tools device toggle option for all available device options.

### __Browser Compatibility__

The website was tested on the following browsers:
- Google Chrome
- Apple Safari
- Mozilla Firefox

### __Testing user stories__

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
`First Time Visitor Goals`
| Understand what the site is for and how to navigate through site. | Logged out landing home page introduuction explains the use of the site | Go to home page as a new user | Explaintion is clear and present | Pass |
| Register For An Account | User creates an account | Clicks 'Register' links, enters correct details | Account is created | Pass |
| Find & Read Rave Reviews | Once logged in buttons and links will take user to reviews page where all reviews are accessible | Click 'Rave Reviews' buttons or links | Review page and all reviews are loaded | Pass |
| Create Rave Review | User can fill out the form and create a review | Click 'Leave Review' link or button | Form is present, once all necessary fields are fillled out, review is created | Pass |
`Returning Visitor Goals`
__Profile__
| View Profile | Once logged in user is directed to their profile page | User logs in | Profile page is loaded with all information of the user | Pass |
| Edit Profile | If user is on their profile page, user can edit their profile | Click 'Edit Profile' button | Edit profile page with information pre-populated on the form | Pass |
| Delete Profile | If user is their profile page, user can delete their profile | Click 'Delete Profile' button | Defenisve modal pops up asking user to confirm the deletion of the specified profile, once delelted user is redirected to the logged out home page | Pass |
__Log In__
| Log In To My Account | Registered user can log in via the log in button and navbar link | Clicks links, enters correct details | User logged in | Pass |
__Reviews__
| Create Rave Review | User can fill out the form and create a review | Click 'Leave Review' link or button | Form is present, once all necessary fields are fillled out, review is created | Pass |
| Read Rave Review | Once logged in user can find reviews and read all reviews from other members | Click 'Rave Reviews' link | Rave review page is loaded with all reviews available | Pass |
| Edit Rave Review | If review is the user's, user can edit the review | Click 'Edit Review' button | Edit review page with information pre-populated on the form | Pass |
| Delete Rave Review | If review is the user's, user can delete the review | Click 'Delete Review' button | Defenisve modal pops up asking user to confirm the deletion of the specified review, once delete user is redirected to the rave reviews page | Pass |
| Leave Comments  | User can write and post comments on each review | Leave comments on multiple reviews | Comments are posted and user name is displayed with comment | Pass |
__Search__
| Search For Rave Reviews | User can use the search bar to search for specific reviews | Type in different reviews by name, venue and title key words | Search brings up the inteded specified reviews | Pass |
`Admin User`
| Add or Remove Organisations Privilege | If logged in as Admin access to organisations, if not redirect to home page  | Attempted to load organisation pages as user and Admin | If user not admin redirected to home page, if admin access allowed | Pass |
| Remove Content Privilege | Only access to delete offensive reviews is Admin | Delete button present on all reviews for Admin. Button only present to user's personal reviews | Review deleted | Pass |
`Site Owner` 
| Defensive Programming (user in session) | When user logged out any page only for liged in access will automatically redirect to the logged outhome page | Attempt to enter pages for logged In Access Only | Redirected to home page | Pass |
| Defensive Prgramming (deletion) | Before any deletion a modal pops up confirming the user wishes to delete | Attempt to delete Organisation, Profile & Review | Defensive modal pops up | Pass |
| Error Page | Button redirects the user to the home page | Clicked button | Redirected to home page | Pass |
_ _ _

## __Bugs__

__1. Image Upload__

It was flagged by a friend that it may be a good feature to remove the necessity of having a profile picture. 

- When attempting to create a profile with the 'required' removed the user is refused with the flash mesaage 'Invalid file format. Please use 'JPG', 'jpeg', 'PNG''
- This is set to ensure the images that are uploaded are the correct format to ensure they display properly.
- Below is the code I have tried to make the register function allow an empty image upload. I got to a point where the flash message would not show if no image was present but instead of registering the account it reset the page. 
- With more time I'd like to look in to this further to make it work but for now as time is limited I will leave the image field as 'required'.

```Python (Register function)
        image_url = upload("profile_image")
        if image_url is None:
            pass
        elif image_url == "invalid":
            if request.files.get("profile_image"):
                flash("Invalid file format. Please use 'JPG', 'jpeg', 'PNG'")
            return redirect(url_for("authentication.register"))
        else:
            pass
```
``` Python (uploaded function)
        if file_key not in request.files:
        return None
    # Retrieve the file from the request using the provided file key
    f = request.files[file_key]

    # Check if the file exists and the extension is allowed
    if not allowed_file(f.filename):
        return 'invalid'
    # Check if the file is empty
    if not f:
        return None
```

__2. Search Pagination__

When a search is performed with more than 4 reviews it paginates the same way the review page does. The issue with this is once the next page is clicked the page resets, goes to the next page but the search feidl is removed so all reviews are displayed.

The same issues occurs for the 'My Reviews' button.

 - Sadly with limited time I have been unable to resolve this issue so to work around it I have removed the per_page which sets the 4 at which to paginated from.
 - This means the reviews page will still paginated but when searching for reviews or clicking 'My Reviews' a list will be generated allowing the user to access all reviews in over 4.
 - It's not perfect but allows for a better user experience, with more time I would look into another way of allowing the pagination to remain.
 - removed code: <code>per_page = 4</code>

__3. Password__

When creating the password if it does not match the correct requirements the user is only notified it does not match, rather than alert the user what they must include.

 - To fix this I added an alert that is called on by javascript explaining the password must be at least 8 characters long if it is not and allowing all types of characters for the password. Previously it only allowed numbers and letters, this also allows for more secure login access.

 ```html
    <div class="password-alert">
        <i class="fas fa-exclamation-circle error-icon"> </i>
        <span class="password-text">Password must be at least 8 characters long</span>
    </div>
```
```javascript
    function checkPassword() {
        if (password.value.length < 8) {
        passwordAlert.style.display = "block";
        } else {
        passwordAlert.style.display = "none";
        }
    }
 ``` 

__4. Youtube Upload__ 

A user doesn't need to upload a youtube video, but if text is entered in the youtube feild that isn't a youtube link an error occurs where 404 error page is generated within the YouTube uplaod div.

 - To fix this I had to update the HTML, Javascrpt and Python code to avoid and future issues. 
 - First I added alerts to the input field to let the user know if the supplied link was in the correct format or not.
 
```html
        <div class="youtube-incorrect">
            <i class="fas fa-exclamation-circle error-icon"> </i>
            <span class="error-text">Incorrect format, must be a YouTube url (or leave blank)</span>
        </div>
        <div class="youtube-correct">
            <i class="fa-regular fa-circle-check"></i>
            <span class="error-text">Correct YouTube format</span>
        </div>
```
 - Then I added the necessary javascrip to call on each alert depending on what was entered in the form

```Javascript
    const youtubeLink = /^(?:https?:\/\/)?(?:m\.|www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
    function checkFaveSet() {
        if (faveSet.value === "") {
            youtubeCorrect.style.display = "none";
            youtubeIncorrect.style.display = "none";
        } else if (youtubeLink.test(faveSet.value)) {
            youtubeCorrect.style.display = "block";
            youtubeIncorrect.style.display = "none";
        } else {
            youtubeCorrect.style.display = "none";
            youtubeIncorrect.style.display = "block";
        }
    }
```
 - As the input field isn't required I need a defensive mechanism to ensure an url that was not in the correct format would be ignored and returned as an emtpy string.
 - I also wanted to ensure that should someone upload a youtube video that's already formatted to embed this too would also work.

 - To do this I updated the modify youtube function.
``` Python
    def modify_youtube_link(link):
    if "youtube.com" in link or "youtu.be" in link:
        if "embed/" not in link:
            if "watch?v=" in link:
                link = link.replace("watch?v=", "embed/")
    else:
        link = ""
    return link
```

__Further Testing__

 - When testing on mobile once a user copies a link from the YouTube app it is always in the youtu.be format. It is also sometimes the same from web browsers.
 - This stops the function from working correctly as it is only editing a watch?v= format. 
 - To over come the issue I added the following code to the fucntion.
```Python
      elif "youtu.be" in link:
        link = link.replace(
            "youtu.be/", "www.youtube.com/embed/")
```
 - When testing further on mobiles I found another way to share which creates a differently structured url with "&feature=share" at the end. Other than that it is the same as a "watch?v=? link so I added another command to fix it should that type of url be used.
```Python
    if "watch?v=" in link:
        link = link.replace("watch?v=", "embed/")
        link = link.replace("&feature=share", "")
```

 - I am now happy with how it all works and feel it is safe proofed against incorrect url uploads and Youtube link formats.

__5. Iphone Organisation Selection__

When selecting the organisations on some Iphones it would not select the Organisation clicked, but one that is 2 up in the row. 

 - I do not know how to fix this issue as it is a Materialize feature and one I don't have access to edit.
 - It was only flagged by one user out of many so I am assuming it doesn't happen all the time or on all devices.

__6. Accordion Issue__

 - The Materialize Accordion should close when another opens but it doesn't. I have followed the instructions form the website and added the correct jquery.
 - My assumption is that as I have intergrated cards within my accordion someowehre along the line I have intruded this feature.
 - It's annoying but it doesn't chang ethe way the website is meant to function, with more time I'd like to get it sorted though.
