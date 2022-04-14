//This script loads all the items in results.json

  	$.getJSON( "/results.json", function( data ) {
  	var items = [];
  	$.each( data, function( key, val ) {
    	items.push( "<div class=\"col-3\" style=\"margin-bottom:25px;\"><div class=\"card\"><div style=\min-height:350px;max-height:350px;overflow:hidden;\">\
    	<img src=\""+ val.image + "\" class=\"card-img-top\" style=\"background-size:cover;\" alt=\"Image loading.\"> \
    	</div><div class=\"card-body\"> \
    			<h5 class=\"card-title\">" + val.name + "</h5> \
    			<p class=\"card-text\" style=\"min-height:50px;\">" + val.title + "</p> \
    		</div>\
    		<ul class=\"list-group list-group-flush\"> \
    			<li class=\"list-group-item\"><small>" + val.building + "</small></li> \
    			<li class=\"list-group-item\"><small>" + val.number + "</small></li> \
    			<li class=\"list-group-item\"><small>" + val.email + "</small></li> \
    		</ul> \
    	</div> \
    	</div>" );
  	});

  	$( "<div/>", {
    	"class": "row justify-content-center",
    	html: items.join( "" )
  	}).appendTo( "#staff" );
	});

