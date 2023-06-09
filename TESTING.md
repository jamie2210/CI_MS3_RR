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
    * [Device Testing](#device-testing)
    * [Browser Compatibility](#browser-compatibility)
    * [Testing User Stories](#testing-user-stories)
3. [Bugs](#bugs)

I consistently tested throughout the build of the project with Chrome developer tools, utilising print statements in python and checking for device compatibility at each stage of the development.
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
When pasting in my index errors and warnings flagged were all linked to Materialize.

When validating just my own custom CSS file it passes with no errors with only 1 warning as it could not read the Google Fonts import.
<details><summary>style.css</summary>
<img src="documentation/testing/css_validation.png">
</details><br>

### __JavaScript Validation__

JSHint JS Validation Service was used to validate the Javascript files. No significant issues were found. Only undefined variables flagged were those used for the emailjs functions.

OnClick buttons were flagged as unused, but /* exported */ feature was used to remove the flags as they are called in the HTML files.

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

To ensure the site is accessible as possible I have taken the following steps;

- Using semantic HTML.
- Descriptive alt attributes on images.
- Label functions and links to ensure clarity of the roles of each button, icon or clickable feature.
- Ensuring that there is a sufficient colour contrast throughout the site (There are contrast flags throughout the WAVE reporting but I am happy with the way the site is represented in these case as a low contrast was my intention and part of the design. I am happy with the visibility of each flag so have left them as they are and they are all labelled with descriptions.)

[Wave accessibility](#https://wave.webaim.org/) was used to test the websites accessibility

All pass with no errors apart from the forms as the drop down option has no form label which is a Materialize feature and something I cannot adjust.

Due to the log in WAVE can only access limited links, these are shared for demonstration to how the rest of the sites pages are structured for optimal accessibility.

Logged Out Home [results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/)

Log In [results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/login)

Register [Results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/register)

Errors [Results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/profile/)

### __Performance__

Performance testing was done using lighthouse in chrome developer tools testing the performance, accessibility, best practices, and SEO of the website. Some of the scores are lower than I'd like them to be but for most of them, the lower ones especially, it was from labels or formatting within Materialize I which I could not change so it's not something I'm too worried about.
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

### __Developer Feature Testing__

| Feature | Testing Performed | Pass/Fail |
| --- | --- | --- |
| Links | Check all links navigate correctly | Pass |
| Buttons | Check all buttons perform correct action | Pass |
| Modals | Check all delete options have defensive modals and modal buttons perform correctly | Pass |
| Create | Check add profile, organisation, review and comment functions work and add information to the database | Pass |
| Read | Check all profiles organisations reviews and comments display as expected | Pass |
| Update | Check edit profile, organisation, review and comment functions work and update information to the database | Pass |
| Delete | Check delete profile, organisation, review and functions work and delete information to the database | Pass |
| Delete Comments | Delete comments associated to a specific review | Pass |
| Pagination | Check pagination works as soon as there are more than 4 reviews | Pass |
| Search | Search index applies to all text fields apart from date | Pass |
| Email | Filled out form sends email to developers address | Pass |
| Image Upload | Check invalid file formats are rejected and valid display correctly | Pass |
| YouTube Link | Check all types of urls are formatted within the function and display correctly | Pass |
| Non YouTube Link | Check function ignores the url and displays nothing with no errors | Pass |
| Javascript | All JS alert functions notify the user with the correct information | Pass |
| Logged Out Users | All logged out users are returned to the logged out home page| Pass|
| Logged in users | All logged in users are returned to the logged in home page if on a page only for Admin | Pass
| Admin | Privileged access to Organisations and CRUD functions across entire site | Pass |
| User | Can access, edit and delete their profile and reviews only, leave comments on all reviews |
| Errors | All error codes covered with return button working | Pass |

### __Testing User Stories__

`First Time Visitor Goals`

1. Understand what the site is for and how to navigate through site.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Introduction Banner | Logged out landing home page | Introduction explains the use of the site | Works as expected |

<details><summary>Logged Out Home Page</summary>
<img src="documentation/images/features/logged-out-home.png">
</details>
<br>

2. Register for an account and create a profile.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Register Button / Link | Click button or link | Registration form page | Works as expected |
| Create Profile | Fill out form and create profile | Profile page loaded | Works as expected |

<details><summary>Register Button / Links</summary>
<img src="documentation/images/features/logged-out-home.png">
</details>
<details><summary>Create Profile</summary>
<img src="documentation/user-stories/create-profile.gif">
</details>
<br>

3. find Rave Reviews.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Rave Reviews Button / Link | Click button or link | Rave Reviews page | Works as expected |

<details><summary>Find Reviews</summary>
<img src="documentation/user-stories/find-reviews.gif">
</details>
<br>

4. Create a rave review.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Leave Reviews Button / Link | Click button or link | Review form page uploaded, fill out form, 'add review' | Works as expected |

<details><summary>Find Review Form</summary>
<img src="documentation/user-stories/find-review-form.gif">
</details>
<details><summary>Add Review</summary>
<img src="documentation/user-stories/add-review.gif">
</details>
<br>

`Returning Visitor Goals`

5. Log in to my account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Log In | Click button or link | Fill in user-name and password | Works as expected |

<details><summary>Log In</summary>
<img src="documentation/user-stories/login.gif">
</details>
<br>

6. Create, edit, delete and view my rave reviews.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Leave Review | Click Leave Review button or link | Fill in form requirements | Works as expected |
| Edit Review | Click Edit button | Fill in form requirements | Works as expected |
| Delete Review | Click Delete button | Confirm deletion on modal | Works as expected |
| View Review | Click My Reviews button | See users reviews | Works as expected |

<details><summary>Add Review</summary>
<img src="documentation/user-stories/add-review.gif">
</details>
<details><summary>Edit Review</summary>
<img src="documentation/user-stories/edit-review.gif">
</details>
<details><summary>Delete Review</summary>
<img src="documentation/user-stories/delete-review.gif">
</details>
<details><summary>View Reviews</summary>
<img src="documentation/user-stories/view-reviews.gif">
</details>
<br>

7. Edit, delete and view my profile.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| View Profile | Click profile link | View profile | Works as expected |
| Edit Profile | Click Edit button | Fill in form requirements | Works as expected |
| Delete Review | Click Delete button | Confirm deletion on modal | Works as expected |

<details><summary>View Profile</summary>
<img src="documentation/user-stories/view-profile.gif">
</details>
<details><summary>Edit Profile</summary>
<img src="documentation/user-stories/edit-profile.gif">
</details>
<details><summary>Delete Profile</summary>
<img src="documentation/user-stories/delete-profile.gif">
</details>
<br>

8. Search for other rave reviews from other members.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Search Reviews | Type in search criteria | See reviews listed | Works as expected |

<details><summary>Search Reviews</summary>
<img src="documentation/user-stories/search.gif">
</details>
<br>

9. Leave comments for other members to read.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Leave Comments | Write comment and post it | See comment under review | Works as expected |

<details><summary>Leave Comments</summary>
<img src="documentation/user-stories/comments.gif">
</details>
<br>

`Admin User`

10. Add, edit or delete organisations.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add Organisation | Click Add organisation button | Fill in required form | Works as expected |
| Edit Organisation | Click edit organisation button | Fill in required form | Works as expected |
| Delete Organisation | Click delete organisation button | Confirm deletion on Modal | Works as expected |

<details><summary>Add / Edit / Delete Organisation</summary>
<img src="documentation/user-stories/organisations.gif">
</details>
<br>

11. Remove any content that could be offensive.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Delete Comments | Click delete comments button | Confirm deletion on Modal | Works as expected |
| Delete Review | Click delete review button | Confirm deletion on Modal | Works as expected |

<details><summary>Delete Comments</summary>
<img src="documentation/user-stories/delete-comments.gif">
</details>
<details><summary>Delete Any Review</summary>
<img src="documentation/user-stories/delete-any-review.gif">
</details>
<br>

12. Ensure defensive programming to avoid deletions by mistake

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Delete Anything | Click delete button | Modal pops up to confirm correct content to delete | Works as expected |

<details><summary>Delete Profile</summary>
<img src="documentation/user-stories/delete-profile.gif">
</details>
<br>

13. Ensure defensive programming so a logged-out user or non-Admin can't access restricted areas of the website.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Log Out | Enter URL of restricted access | returned to home page | Works as expected |

<details><summary>Return Restricted user</summary>
<img src="documentation/user-stories/return-restricted.gif">
</details>
<br>

`Site Owner` 

14. Automatically return a logged-out user to the logged-out home page, or anyone but Admin from restricted pages to the logged-in Home page if logged-in.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Log Out | User logs out | Returned to home page | Works as expected |

<details><summary>Log out</summary>
<img src="documentation/user-stories/logout.gif">
</details>
<details><summary>Restricted Page Return</summary>
<img src="documentation/user-stories/restricted.gif">
</details>
<br>

15. Relevant error page displayed should an invalid command or error occur.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Error Page | Enter invalid url | Error page displayed | Works as expected |

<details><summary>Error Page</summary>
<img src="documentation/user-stories/error.gif">
</details>
<br>

16. I want the user to be able to contact me should they have any questions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Form | Fill out form and send | email is sent to site owners email account | Works as expected |

<details><summary>Contact Form</summary>
<img src="documentation/user-stories/contact.gif">
</details>
<br>
_ _ _

## __Bugs__

__1. Image Upload__

It was flagged by a friend that it may be a good feature to remove the necessity of having a profile picture. 

- When attempting to create a profile with the 'required' removed the user is refused with the flash message 'Invalid file format. Please use 'JPG', 'jpeg', 'PNG''
- This is set to ensure the images that are uploaded are the correct format to ensure they display properly.
- Below is the code I have tried to make the register function allow an empty image upload. I got to a point where the flash message would not show if no image was present but instead of registering the account it reset the page. 
- With more time I'd like to look in to this further to make it work but for now as time is limited I will leave the image field as 'required'.
- As a work around I added a Jaavscript function to alert the user if the file is a correct format or not. 

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
``` Javascript
function checkProfileImage() {
    if (profileImage.value === "") {
        imageCorrect.style.display = "none";
        imageIncorrect.style.display = "none";
    } else if (imageType.test(profileImage.value)) {
        imageCorrect.style.display = "block";
        imageIncorrect.style.display = "none";
    } else {
        imageCorrect.style.display = "none";
        imageIncorrect.style.display = "block";
    }
}
```

__2. Search Pagination__

When a search is performed with more than 4 reviews it paginates the same way the review page does. The issue with this is once the next page is clicked the page resets, goes to the next page but the search field is removed so all reviews are displayed.

The same issues occurs for the 'My Reviews' button.

 - Sadly with limited time I have been unable to resolve this issue so to work around it I have removed the per_page which sets the 4 at which to paginated from.
 - This means the reviews page will still paginated but when searching for reviews or clicking 'My Reviews' a list will be generated allowing the user to access all reviews in over 4.
 - It's not perfect but allows for a better user experience, with more time I would look into another way of allowing the pagination to remain.
 - removed code: <code>per_page = 4</code>

__3. Password__

When creating the password if it does not match the correct requirements the user is only notified it does not match, rather than alert the user what they must include.

 - To fix this I added an alert that is called on by Javascript explaining the password must be at least 8 characters long if it is not and allowing all types of characters for the password. Previously it only allowed numbers and letters, this also allows for more secure login access.

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

__4. YouTube Upload__ 

A user doesn't need to upload a Youtube video, but if text is entered in the YouTube feild that isn't a YouTube link an error occurs where 404 error page is generated within the YouTube upload div, creating an odd error with a new webpage portal inisde the video area.

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
 - As the input field isn't required, I need a defensive mechanism to ensure an url that was not in the correct format would be ignored and returned as an empty string.
 - I also wanted to ensure that should someone upload a YouTube video that's already formatted to embed this too would also work.

 - To do this I updated the modify YouTube function.

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

 - When testing on mobile, once a user copies a link from the YouTube app it is always in the youtu.be format. It is also sometimes the same from web browsers.
 - This stops the function from working correctly as it is only editing a watch?v= format. 
 - To over come the issue I added the following code to the function.

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

 - I am now happy with how it all works and feel it is safe proofed against incorrect url uploads and YouTube link formats.
 - I still find some Youtube links don't work when uploaded but I think this now down to restrictive settings on the video set by the owner to prevent embedding or sharing on sites.

__5. Iphone Organisation Selection__

When selecting the organisations on some Iphones it would not select the Organisation clicked, but one that is 2 up in the row. 

 - I do not know how to fix this issue as it is a Materialize feature and one I don't have access to edit.
 - It was only flagged by one user out of many, so I am assuming it doesn't happen all the time or on all devices.

__6. Accordion Issue__

 - The Materialize Accordion should close when another opens but it doesn't. I have followed the instructions form the website and added the correct jquery.
 - My assumption is that as I have integrated cards within my accordion somewhere along the line I have intruded this feature.
 - It's annoying but it doesn't change the way the website is meant to function, with more time I'd like to get it sorted though.

__7. Delete Comments__

 - It's an important feature to me as admin to be able to remove distasteful comments or reviews.
 - While testing my user stories I realised I could only remove comments by delete the entire review. This was not ideal.
 - My first attempt was to build a javascript function that could hide all comments, affectively turning them off.

```javascript
function handleComments(comment_id) {
    const comments = document.querySelectorAll(`#comments-${comment_id}`);
    const commentSection = document.querySelectorAll(`#comment-section-${comment_id}`);
    for (var i = 0; i < comments.length; i++) {
        if (comments[i].style.display === 'none') {
          comments[i].style.display = 'block';
        } else {
          comments[i].style.display = 'none';
        }
      }
      
      for (var j = 0; j < commentSection.length; j++) {
        if (commentSection[j].style.display === 'none') {
          commentSection[j].style.display = 'block';
        } else {
          commentSection[j].style.display = 'none';
        }
      }
    }
```
 - This code worked until the page refreshed and the original settings returned, which prevented from it working properly.
 - It then dawned on me that if use this function then it stops others being able to comment.
 - As a result, I built a delete comment function in python

```python
def delete_comment(rave_id):
    """
    This function deletes comments from a rave review
    """
    try:
        # finds the rave name the comments are assocaited to
        rave = mongo.db.raves.find_one({"_id": ObjectId(rave_id)})
        rave_name = rave['rave_name']
        # Delete all associated comments
        mongo.db.comments.delete_many({"comment_id": ObjectId(rave_id)})
        # f string adds rave name to the flash message once deleted
        flash(f"Comments for {rave_name} are Gone!")
    except Exception as e:
        flash("An exception occurred while deleting the review" + str(e))
    return redirect(url_for("raves.get_raves"))
```
 - There's a slight flaw in that I can only delete all comments rather than specific ones but due to time restraints this will do for now.