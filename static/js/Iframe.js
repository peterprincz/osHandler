$( document ).ready(function() {
    $.get( "get_butterfly_address", function( data ) {
        setTimeout(function(){
            $("#Iframe").attr("src", "http://" + data.ip_address);
            var iframe = document.getElementById("Iframe")
            iframe.contentWindow.focus();
            }, 4000);
    });
});