$(document).ready(()=>{
    let source_count = 1;
    $('.fixed-action-btn').floatingActionButton();
    $("#add_source_btn").click(()=>{
        source_count+=1;
        $("#sources_form").append(" <div class=\"col s8\">\n" +
            "<input type=\"url\" id=\"source-input\""+source_count+" class=\"input-field source-input\">\n" +
            "<label for=\"source-input\""+source_count+">Fonte de dados</label>\n" +
            "</div>");
    });
    $("#save_sources").click(()=>{
        let data = new FormData();
        $(".source-input").each((index, obj)=>{
            data.append($(obj).attr("id"), $(obj).val());
        });
        $.ajax({
            url: "/sources",
            method: "POST",
            data: data,
            contentType: false,
            processData: false,
            success: data=>{
                data = JSON.parse(data);
                if(data["result"])
                    M.toast({html: "Cadastro realizado"});
            },
            error: err=>{
                console.log(err);
            }
        });
    });
});