$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.carousel').carousel();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      showclearBtn: true,
      i18n: {
        done: "select"
      }
    });
  });