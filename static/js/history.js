$(document).ready(()=>{
    let collectionItem = $(".collection-item");
    collectionItem.mouseover(function(){
        $(this).addClass("active");
    });
    collectionItem.mouseleave(function(){
        $(this).removeClass("active");
    });
    $("#download_history_btn").click(function () {
        $.ajax({
            url: "/download_history",
            success: data=>{
                window.open("data:application/pdf,"+ escape(data))
            },
            error: err=>{
                console.log(err);
            }
        })
    });
});