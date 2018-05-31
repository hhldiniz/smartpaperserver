$(document).ready(()=>{
    $("#signup_btn").click(()=>{
        let data = {
            "name": $("#user_name").val(),
            "username": $("#user_username").val(),
            "email": $("#user_email").val(),
            "password": $("#user_password").val()
        };
        $.ajax({
            url: "/signup",
            method: "POST",
            data: data,
            success: data=>{
                console.log(data);
                data = JSON.parse(data);
                if(data["result"])
                {
                    M.toast({html: "Cadastro realizado"});
                    setTimeout(()=>{
                        window.location.pathname = "/";
                    }, 1000);

                }
            },
            error: err=>{
                console.log(err);
            }
        });
    });
});