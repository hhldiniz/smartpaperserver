$(document).ready(()=>{
    let collectionItem = $(".collection-item");
    collectionItem.mouseover(function(){
        $(this).addClass("active");
    });
    collectionItem.mouseleave(function(){
        $(this).removeClass("active");
    });
});