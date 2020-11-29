$(document).ready(function () {
  var search = window.location.search;
	//get search content
  var urlParams= new URLSearchParams(search);
  
  var searchresult = urlParams.get("search");
	//get value
	

  if (searchresult == 'deer') {
	  //if result is deer
	$("#present").empty().append("Waitting to redriect to:", searchresult);
	  //give a message to page center to let users know we will redirect to another page


    setTimeout(
      function () {

        window.location.href = "./listdetail";
		  //redirect to target page


      }, 3000);

  } else {
    $("#present").append("Please Research again, We Can not Found the Result:", searchresult);
	  //give a warning message to ask user to search again


  }


});
