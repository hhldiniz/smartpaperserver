/**
 * Created by Eric Duminil. Original code available at
 * https://stackoverflow.com/questions/23190056/hex-to-base64-converter-for-javascript#answer-41797377
 * @param hexstring
 * @returns {string}
 */
function hexToBase64(hexstring) {
    return btoa(hexstring.match(/\w{2}/g).map(function(a) {
        return String.fromCharCode(parseInt(a, 16));
    }).join(""));
}

function downloadPhoto() {
    $.ajax({
        url: "/user_photo",
        method: "GET",
        contentType: "image/png",
        success: data=>{
            let b64String = hexToBase64(data);
            $("#user_photo").attr("src",`data:image/png;base64,${b64String}`);
        },
        error: err=>{
            console.log(err);
        }
    });
}