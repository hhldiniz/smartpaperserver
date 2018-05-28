$(document).ready(function () {
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