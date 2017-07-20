/**
 * Created by dewyn on 03/07/17.
 */
$(document).ready(function () {

    console.log("PROBANDO 1, 2, 3");
    $("#privado").click(function () {
        if(document.getElementById("privado").checked){
            console.log("Checked");
            $(".usuarios-permitidos").removeClass("hidden");
            $(".usuarios-permitidos").removeClass("hidden");
        } else {
            console.log("Unchecked");
            $(".usuarios-permitidos").addClass("hidden");
        }
    });

    $("#input").blur(function () {
        if (!$("#input").val()) {
            $("#ingresarTitulo").removeClass("hidden");
        } else {
            $("#ingresarTitulo").addClass("hidden");
        }
    });

});