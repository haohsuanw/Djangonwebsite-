$(document).ready(function () {
	
$( "#gallery dd" ).on( "mouseenter", function(  ) {
	//mouse enter to dive
	var thisis=$( this );
    thisis.find("a").find("img").css("height","140px");
	thisis.find("h4").css("font-size","35px").css("color","#F2E1D1");
	//let img and text become big

});

	$( "#gallery dd" ).on( "mouseleave", function(  ) {
		//mouse leave
    var thisis=$( this );
    thisis.find("a").find("img").css("height","110px");
	thisis.find("h4").css("font-size","").css("color","#FFFFFF");
		//let img and text become original
		
});

	
	
});