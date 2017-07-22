/**
 * Created by dewyn on 03/07/17.
 */
$(document).ready(function () {

    var ok = true, usersOK = true;

    $("#privado").click(function () {
        if(document.getElementById("privado").checked){
            console.log("Checked");
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

    $("#video_submit").click(function (e) {
        verifyBlankFields();
        if (ok && usersOK){
            console.log("Ta OK");
            $("#submit_video_form").submit();
        }
    });

    $("#upload_file").on("change", function () {
        var type = this.files[0].type;
        console.log(type);
        if  (type.substring(0, 5) !== "video"){
            $("#video_notif").removeClass("hidden");
            ok = false;
            console.log("No es un video");
        } else {
            $("#video_notif").addClass("hidden");
            ok = true;
        }
    });

    $("#featured_image").on("change", function () {
        var type = this.files[0].type;
        if  (type.substring(0, 5) !== "image"){
            ok = false;
            $("#thumb_notif").removeClass("hidden");
            console.log("No es una foto");
        } else {
            $("#thumb_notif").addClass("hidden");
            ok = true;
        }
    });


    function verifyBlankFields() {
        console.log("Verifying...");
        //region Verificar campos vacios
        if (!$("#input").val() || !$("#upload_file").val() || !$("#featured_image").val()){
            console.log("Algo vacio");
            $("#camposVacios").removeClass("hidden");
            ok = false;
        } else {
            console.log("Todo bien.");
            $("#camposVacios").addClass("hidden");
            ok = true;
        }

        if ($("#privado").checked && !$("usuarios").val()){
            $("#usersVacio").removeClass("hidden");
            usersOK = false;
        } else {
            $("#usersVacio").addClass("hidden");
            usersOK= true;
        }
        //endregion
    }

});