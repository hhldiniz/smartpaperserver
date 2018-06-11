$(document).ready(()=>{
   $("#sources_form").append("<div class='col s8'><button class=\"btn waves-effect waves-light\" type=\"button\" id=\"submit_search\" name=\"action\">Submit\n" +
       "<i class=\"material-icons right\">send</i>\n" +
       "</button></div>");
   $("#submit_search").click(()=>{
    let data = new FormData();
    $("#form_source_container");
    $.ajax({
        url: "/sources",
        method: "POST",
        data: data,
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