$(document).ready(function () {
    $(".modal").modal();
    let resultCollection = $(".result_collection_container");
    let searchForm = $("#search_form");
    let backToSearch = $("#back_to_search");
    backToSearch.hide();
    backToSearch.click(()=>{
        searchForm.show();
        resultCollection.hide();
    });
    resultCollection.hide();
    searchForm.show();
    $("#submit_search").click(()=> {
        $.ajax({
            url: "/",
            method: "POST",
            data: {"key": $("#key").val(), "hidden": $("#search_hidden").val()},
            success: data=>{
                data = JSON.parse(data);
                $(".collection-item").remove();
                console.log(typeof(data[1][0]["name"]));
                for(let obj in data[1][0]["name"])
                {
                    if(data[1][0]["name"].hasOwnProperty(obj))
                        $(".result_collection").append(`<li class="collection-item">${data[1][0]["name"][obj]}</li>`);
                }
                resultCollection.show();
                searchForm.hide();
                backToSearch.show();
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