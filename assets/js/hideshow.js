
$(document).ready (function(){
    $("#b1").click(function(){
    $("#d1").hide();
    });

    $("#b2").click(function(){
    $("#d1").show();
    });

    $("#b3").click(function(){
    $("#d1").slideToggle();
    });

    $("#b4").click(function(){
    $("#d1").delay(500).fadeToggle();
    $("#d2").delay(1000).fadeToggle();
    });


});
