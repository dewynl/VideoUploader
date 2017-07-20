$(document).ready(function () {
    var current_page = 1;
    pager();

    function pager(){
        $.get( "/api/get/videos/" + current_page, function( data ) {
            $( "#showingVideos" ).html( data );
        });
    }
    $('#pager').click(function(e){
        current_page++;
        pager();
        e.preventDefault();
    });
});