# __Rave Reviews Testing__

![Mockup image](docs/device-display.jpg)

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



1. Log in to my account.
2. Create, edit, delete and view my rave reviews.
3. Create, edit, delete and view my profile.
4. Search for other rave reviews from other members.

#### __Admin User__

As an administrator for the site I want to be able to:

1. The only one with access to Add or remove organisations.
2. The only one with access to remove any content that could be offensive.


|`Admin User` |
|   |   |   |   |   |
| Add or Remove Organisations Privilege | If logged in as Admin access to organisations, if not redirect to home page  | Attempted to load organisation pages as user and Admin | If user not admin redirected to home page, if admin access allowed | Pass |
| Remove Content Privilege | Only access to delete offensive reviews is Admin | Delete button present on all reviews for Admin. Button only present to user's personal reviews | Review deleted | Pass |

|`Site Owner` |
|   |   |   |   |   |
| Defensive Programming (user in session) | When user logged out any page only for liged in access will automatically redirect to the logged outhome page | Attempt to enter pages for logged In Access Only | Redirected to home page | Pass |
| Defensive Prgramming (deletion) | Before any deletion a modal pops up confirming the user wishes to delete | Attempt to delete Organisation, Profile & Review | Defensive modal pops up | Pass |
| Error Page | Button redirects the user to the home page | Clicked button | Redirected to home page | Pass |

#### __Site Owner__

1. Automatically return a logged out user to the logged out home page if not on a page they shouldn't be.
2. Ensure defensive programming to avoid deletions by mistake
3. Relevant error page displayed should an invalid command or error occur.

_ _ _

## __Bugs__
