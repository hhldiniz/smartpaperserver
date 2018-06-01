$(document).ready(()=>{
    $("#logout_link").click(()=>{
        $.ajax({
            url:"/logout",
            success: data=>{
                data = JSON.parse(data);
                if(data["result"])
                    window.location.pathname=""
            },
            error: err=>{
                console.log(err);
            }
        })
    });
});
