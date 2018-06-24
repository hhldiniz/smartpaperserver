$(document).ready(()=>{
    $("#logout_link").click(()=>{
        $.ajax({
            url:"/logout",
            success: data=>{
                data = JSON.parse(data);
                if(data["result"])
                {
                    // if(window.location.pathname === "#!" || window.location.pathname === "#")
                        window.location.reload();
                    // else
                    //     window.location.pathname="";
                }
            },
            error: err=>{
                console.log(err);
            }
        })
    });
});
