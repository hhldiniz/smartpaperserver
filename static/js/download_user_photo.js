$(document).ready(()=>{
   function downloadPhoto() {
        $.ajax({
            url: "/user_photo",
            method: "GET",
            success: data=>{
                console.log(data);
            },
            error: err=>{
                console.log(err);
            }
        });
   }
   downloadPhoto();
});