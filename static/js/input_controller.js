$(document).ready(()=>{
    let typeInput = $("input:text");
    typeInput.focusin(function () {
        $(this).siblings("label").addClass("active");
    });

    typeInput.focusout(function () {
        $(this).siblings("label").removeClass("active");
    });
});

