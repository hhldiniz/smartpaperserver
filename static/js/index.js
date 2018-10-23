$(document).ready(function () {
    $(".modal").modal();
    let resultCollection = $(".result_collection");
    resultCollection.hide();
    $("#submit_search").click(()=> {
        $.ajax({
            url: "/",
            method: "POST",
            data: {"key": $("#key").val(), "hidden": $("#search_hidden").val()},
            success: data=>{
                data = JSON.parse(data);
                $(".collection-item").remove();
                for(let key in data)
                {
                    if(data.hasOwnProperty(key))
                        for(let result in data[key])
                        {
                            if(data[key].hasOwnProperty(result))
                            {
                                $(".result_collection").append(`<li class='collection-item'>${data[key][result]["name"]}</li>`);
                            }
                        }
                }
                resultCollection.show();
            },
            error: err=>{
                console.error(err)
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