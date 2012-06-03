codeAddress = function(){
	var address = $('#zipcode_input').val();
	geocoder.geocode({
		'address' : address
	}, function(results, status) {
		if(status == google.maps.GeocoderStatus.OK) {
			map.setCenter(results[0].geometry.location);
			map.setZoom(13);
		} else {
			//alert("Geocode was not successful for the following reason: " + status);
		}
	});
}

setSchool = function(school,type){
	
	console.log(type)
	
	if(type == 'High'){
		$('#high_school').val(school);
		$('#high_school_complete').css('display','inline');
	}else if (type == 'Middle'){
		$('#middle_school').val(school);
		$('#middle_school_complete').css('display','inline');
	}else if(type == 'Elementary'){
		$('#elementary_school').val(school);		
		$('#elementary_school_complete').css('display','inline');
	}
	
	return false;
}

$(function() {
	$('#zipcode_form').submit(function() {
		codeAddress();
		return false;
	});
});