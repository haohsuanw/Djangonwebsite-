$(document).ready(function () {
	
	$("#loadcomment").click(function (){
	    var work=$(this).attr('worktitle')
        var ajax_url=$(this).attr('data-ajax-url')

	  $.ajax({
          headers: {'X-CSRFToken': csrftoken},

    // The URL for the request
    url: ajax_url,

    // The data to send (will be converted to a query string)
    data: {
        work: work
    },

    // Whether this is a POST or GET request
    type: "POST",
    // The type of data we expect back
    dataType : "json",

	  })
  // Code to run if the request succeeds (is done);
  // The response is passed to the function
  .done(function( json ) {
      if(json.success='success'){
          var commentlist=json.commentlist
          var userlist=json.userlist
          var time=json.timelist

          $("#load").empty();
          if(commentlist.length>0){
              for(let i =0;i<commentlist.length;i++ ){

                  var str="<a href=/users/profile/"+userlist[i]+">"+userlist[i]+""
                  $("#load").append(str)
              $("#load").append(commentlist[i]).css("color", "white").css("font-family", "Gill Sanssans-serif").css( "text-align", "center");
                  $("#load").append(","+"Post time:"+time[i])
                   $("#load").append("<p></p>")


          }

          }
          else{
               $("#load").append("<p>There are no any comment about this work, try to write down your comment</p>")


          }






      }

      else{


          alert("Error:"+json.error);
      }
   //  $( "<h1>" ).text( json.title ).appendTo( "body" );
     //$( "<div class=\"content\">").html( json.html ).appendTo( "body" );
  })
  // Code to run if the request fails; the raw request and
  // status codes are passed to the function
  .fail(function( xhr, status, errorThrown ) {
    alert( "Sorry, there was a problem!" );
    console.log( "Error: " + errorThrown );

  })
  // Code to run regardless of success or failure;
  .always(function( xhr, status ) {
   // alert( "The request is complete!" );
  });







        })








  $("#content").submit(function () {
	  //form submit function

      var text = $("#textcontent").val();
	  //get textarea content
      var ajax_url=$(this).attr('data-ajax-url1')

      var id = $("#id").val();
      var work = $("#work").val();
      var name = $("#name").val();
      var age = $("#age").val();




    if (text == "") {
		//when textarea is null

      $("form").css("background", "red").find("div").find("dl").append("<p>Please write your comment</p>");
		//warning message
    } else {
      $("form").css("background", "white").find("div").find("dl").empty();
		//not empty delete warning message


    $.ajax({
          headers: {'X-CSRFToken': csrftoken},

    // The URL for the request
    url: ajax_url,

    // The data to send (will be converted to a query string)
    data: {
        work: work,
        id:id,
        name:name,
        age:age,
        text:text,

    },

    // Whether this is a POST or GET request
    type: "POST",
    // The type of data we expect back
    dataType : "json",

	  })
  // Code to run if the request succeeds (is done);
  // The response is passed to the function
  .done(function( json ) {
      if(json.success='success'){
          var commentlist=json.commentlist
          $("#load").empty();
          if(commentlist.length>0){
              for(let i =0;i<commentlist.length;i++ ){
              $("#load").append(commentlist[i]).css("color", "white").css("font-family", "Gill Sanssans-serif").css( "text-align", "center");
              $("#load").append("<p></p>")
                  $( "#reload" ).load(window.location.href + " #reload" );
              $("#deletethisaftersubmit").empty()

          }

          }
          else{
               $("#load").append("<p>There are no any comment about this work, try to write down your comment</p>")


          }






      }

      else{


          alert("Error:"+json.error);
      }
   //  $( "<h1>" ).text( json.title ).appendTo( "body" );
     //$( "<div class=\"content\">").html( json.html ).appendTo( "body" );
  })
  // Code to run if the request fails; the raw request and
  // status codes are passed to the function
  .fail(function( xhr, status, errorThrown ) {
    alert( "Sorry, there was a problem!" );
    console.log( "Error: " + errorThrown );

  })
  // Code to run regardless of success or failure;
  .always(function( xhr, status ) {
   // alert( "The request is complete!" );
  });






    }



    return false;
	  //to prevent web page reload


  });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

});
