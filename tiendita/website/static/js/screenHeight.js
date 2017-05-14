$( document ).ready(function() {
var windowHeight = $(window).height();
var navHeight = $("header").height()

$(".content-holder").css("height", windowHeight - navHeight);
console.log(windowHeight);
console.log(navHeight);

//$(".content-holder").css("padding-top", navHeight);;

});
