$(document).ready(function () {
    $(".modal").modal();
    $("#submit_search").click(()=> {
        $.ajax({
            url: "/",
            method: "POST",
            data: {"key": $("#key").val()},
            success: data=>{
                $("#search_result_text").text(data);
                $("#search_result").modal("open");
            },
            error: err=>{

            }
        });
    });

    $("#authenticate_btn").click(()=>{
        let data = {
            "username": $("#username").val(),
            "password": $("#password").val(),
            "remember": $("#remember_switch").val(),
            "hidden": $("#login_hidden").val()
        };
        $.ajax({
            data: data,
            method: "POST",
            url: "/authenticate",
            success: data=>{
                data = JSON.parse(data);
                if(data["result"])
                    window.location.reload();
            },
            error: err=>{
                console.log(err);
            }
        });
    });
});