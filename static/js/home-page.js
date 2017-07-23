/**
 * Created by dewyn on 03/07/17.
 */

$(document).ready(function () {
    console.log("Saludo");
    $("#buscar-videos-button").click(function () {
        console.log("click");
        $("#search").submit();
    });
});
