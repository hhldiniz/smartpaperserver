$(document).ready(()=>{
    $("#signup_btn").click(()=>{
        let data = new FormData();
        data.append("name", $("#user_name").val());
        data.append("email", $("#user_email").val());
        data.append("username", $("#user_username").val());
        $.each($("#user_photo")[0].files, (i, file)=>{
           data.append("photo", file);
        });
        data.append("password", $("#user_password").val());
        console.log(data);
        $.ajax({
            url: "/signup",
            method: "POST",
            cache: false,
            contentType: false,
            processData: false,
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