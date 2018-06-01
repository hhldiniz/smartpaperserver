$(document).ready(function () {
    $(".modal").modal();
    $("#submit_search").click(()=> {
        $.ajax({
            url: "/search",
            data: {"key": $("#key").val()},
            success: data=>{

            },
            error: err=>{

            }
        });
    });

    $("#authenticate_btn").click(()=>{
        let data = {
            "username": $("#username").val(),
            "password": $("#password").val(),
            "remember": $("#remember_switch").val()};
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
    $("#logout_link").click(()=>{
       $.ajax({
           url:"/logout",
           success: data=>{
               data = JSON.parse(data);
               if(data["result"])
                   window.location.reload();
           },
           error: err=>{
               console.log(err);
           }
       })
    });
});