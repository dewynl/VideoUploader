/*
/!**
 * Created by dewyn on 07/07/17.
 *!/
$(document).ready(function (e) {
    $(".borrarVideo").click(function (e) {
        //e.preventDefault();
        console.log($(this).val());
        $(this).attr("formaction", "/borrar/" + $(this).val());
        $(this).attr("formmethod", "post");
        $(this).submit();
    })
});

*/
