/**
 * Created by dewyn on 03/07/17.
 */
$(document).ready(function () {

    var ok = true, usersOK = true, fotoOK = false, videoOK;

    $("#privado").click(function () {
        if(document.getElementById("privado").checked){
            console.log("Checked");
            $(".usuarios-permitidos").removeClass("hidden");
        } else {
            console.log("Unchecked");
            $(".usuarios-permitidos").addClass("hidden");
        }
    });

    $("#titulo").blur(function () {
        if (!$("#input").val()) {
            $("#ingresarTitulo").removeClass("hidden");
        } else {
            $("#ingresarTitulo").addClass("hidden");
        }
    });

    $("#video_submit").click(function (e) {
        verifyBlankFields();
        console.log(ok + "|" + usersOK + "|" + fotoOK + "|" + videoOK)
        if (ok && usersOK && fotoOK && videoOK){
            console.log("Ta OK");
            $("#submit_video_form").submit();
        }
    });

    $("#upload_file").on("change", function () {
        var type = this.files[0].type;
        console.log(type);
        if  (type.substring(0, 5) !== "video"){
            $("#video_notif").removeClass("hidden");
            videoOK = false;
            console.log("No es un video");
        } else {
            $("#video_notif").addClass("hidden");
            videoOK = true;
        }
    });

    $("#thumbnail_file").on("change", function () {
        var type = this.files[0].type;
        if  (type.substring(0, 5) !== "image"){
            fotoOK = false;
            $("#thumb_notif").removeClass("hidden");
            console.log("No es una foto");
        } else {
            $("#thumb_notif").addClass("hidden");
            fotoOK = true;
        }
    });


    function verifyBlankFields() {
        console.log("Verifying...ok");
        console.log(ok + "|" + usersOK);
        //region Verificar campos vacios
        if (!$("#titulo").val() || !$("#upload_file").val() || !$("#thumbnail_file").val()){
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