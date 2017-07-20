/**
 * Created by dewyn on 03/07/17.
 */
$(document).ready(function () {
    var tiempoReconectar = 1000;
    var webSocket;
    //region WebSocket
    function conectar(){
        webSocket = new WebSocket("ws://" + location.hostname + ":" + location.port + "/verifications");
        webSocket.onopen = function(e) {console.log("Conectado - status " + this.readyState);};
        webSocket.onclose = function(e) {console.log("Desconectado - status " + this.readyState);};
        webSocket.onmessage = function(mensaje) {recibirMensaje(mensaje);};
    }

    function verificarConexion(){
        if(!webSocket || webSocket.readyState === 3){
            conectar();
        }
    }
    setInterval(verificarConexion, tiempoReconectar); //para reconectar.

    $("#logInButton").click(function (e) {
        e.preventDefault();
        var username = $("#username").val();
        var clave = $("#clave").val();
        webSocket.send("login~" + username + "~" + clave);
    });

    function recibirMensaje(mensaje) {
        if (mensaje.data === "goodCredentials"){
            $("#badCredentials").addClass("hidden");
            $("#logInForm").unbind("submit").submit();
        } else {
            $("#badCredentials").removeClass("hidden");
        }
    }
});