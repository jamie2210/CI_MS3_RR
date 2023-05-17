/*jshint esversion: 6 */

/**
 * Jquery functions taken from materialize
 * and code institue tutorials
 */

$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.carousel').carousel();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.materialboxed').materialbox();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
        dateFormat: "dd MM yy",
        maxDate: null,
        showClearBtn: true,
        i18n: {
            done: "select"
        }
    });

    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute",
                "opacity": "0"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.0)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {});

/**
 * Select required elements
 */
const reviewModal = document.querySelector('.review-modal');

/**
 * Delete Modal functions
 */
function deleteReviewModal(rave_id) {
    const modal = document.querySelector(`#rave-modal-${rave_id}`);
    const modalBackground = document.querySelector(`#modal-background-${rave_id}`);
    modal.style.display = "block";
    modalBackground.style.display = "block";
}

function closeRaveModal(rave_id) {
    const modal = document.querySelector(`#rave-modal-${rave_id}`);
    const modalBackground = document.querySelector(`#modal-background-${rave_id}`);
    modal.style.display = "none";
    modalBackground.style.display = "none";
}

function deleteOrganisationModal(organisation_id) {
    const modal = document.querySelector(`#organisation-modal-${organisation_id}`);
    const modalBackground = document.querySelector(`#modal-background-${organisation_id}`);
    modal.style.display = "block";
    modalBackground.style.display = "block";
}

function closeOrgModal(organisation_id) {
    const modal = document.querySelector(`#organisation-modal-${organisation_id}`);
    const modalBackground = document.querySelector(`#modal-background-${organisation_id}`);
    modal.style.display = "none";
    modalBackground.style.display = "none";
}

function deleteUserModal(user_id) {
    const modal = document.querySelector(`#organisation-modal-${user_id}`);
    const modalBackground = document.querySelector(`#modal-background-${user_id}`);
    modal.style.display = "block";
    modalBackground.style.display = "block";
}

function closeUserModal(user_id) {
    const modal = document.querySelector(`#organisation-modal-${user_id}`);
    const modalBackground = document.querySelector(`#modal-background-${user_id}`);
    modal.style.display = "none";
    modalBackground.style.display = "none";
}

// Updates the copyright year in footer with the current year
const year = document.querySelector('#current-year');
year.innerHTML = new Date().getFullYear();

/**
 * Add email.js to contact form to send email directly to gmail account.
 * @param {sendEmail} contactForm 
 */

function sendMail(contactForm) {
    emailjs.send("service_xm3vl8h", "rave_reviews", {
            "from_name": contactForm.name.value,
            "message": contactForm.message.value,
            "from_email": contactForm.email.value,
            "reply_to": contactForm.email.value
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                swal("Thank you!", "Your message has been sent", "success"); // Use sweet alert to provide stlyed alert box for successfully sent message.
                contactForm.reset(); // Reset form after successful submission.
            },
            function (error) {
                console.log("FAILED", error);
                swal("Oh dear!", "Something went wrong, please try again", "error"); // Use sweet alert to provide stlyed alert box for unsuccessfully sent message.
            });
    return false; // Prevents form from submitting if there's an error.
}

/**
 * Password match function to ensure users passwords match
 * Alerts used to display when passowrds do or don't match
 * Register button disabled until passwords match
 */

const password = document.querySelector("#password");
const passwordAlert = document.querySelector(".password-alert");
const confirmPassword = document.querySelector("#confirm-password");
const errorAlert = document.querySelector(".alert");
const passwordTick = document.querySelector(".tick-icon");
const submitBtn = document.querySelector(".submit-btn");

/**
 * Checks if password is present to avoid listening on all pages and causing an error
 */
if (password !== null) {
    password.addEventListener("input", checkPassword);
  }

function checkPassword() {
    if (password.value.length < 8) {
    passwordAlert.style.display = "block";
    } else {
    passwordAlert.style.display = "none";
    }
}

/**
 * Checks if confirmPassword is present to avoid listening on all pages and causing an error
 */
if (confirmPassword !== null) {
    confirmPassword.addEventListener("input", checkPasswordsMatch);
  }

function checkPasswordsMatch() {
    if (confirmPassword.value !== "") {
        if (password.value === confirmPassword.value) {
            passwordTick.style.display = "block";
            errorAlert.style.display = "none";
            submitBtn.disabled = false;
        } else {
            passwordTick.style.display = "none";
            errorAlert.style.display = "block";
            submitBtn.disabled = true;
        }
    }
}


/* exported 
reviewModal,
deleteReviewModal,
closeRaveModal,
deleteOrganisationModal,
closeOrgModal,
deleteUserModal,
closeUserModal,
sendMail */
