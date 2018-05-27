$(document).ready(function () {
    let typeInput = $("input:text");
    typeInput.focusin(function () {
        $(this).siblings("label").addClass("active");
    });

    typeInput.focusout(function () {
        $(this).siblings("label").removeClass("active");
    });

    $("#submit_search").click(function () {
       $.ajax({
          url: "/search",
          data: {"key": $("#key").val()},
          success: data=>{

          },
          error: err=>{

          }
       });
    });
});