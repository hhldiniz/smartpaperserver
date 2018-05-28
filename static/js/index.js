$(document).ready(function () {
    $(".modal").modal();
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