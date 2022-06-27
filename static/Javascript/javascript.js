function initialize() {

	var mapOptions, map, marker, searchBox,
		infoWindow = '';
		infoWindow = '',
		addressEl = document.querySelector( '#map-search' ),
		latEl = document.querySelector( '.latitude' ),
		longEl = document.querySelector( '.longitude' ),
		element = document.getElementById( 'map-canvas' );
		element = document.getElementById( 'map-canvas' ),
		city = document.querySelector( '.reg-input-city' );

	mapOptions = {
		// How far the maps zooms in.
		zoom: 8,
		// Current Lat and Long position of the pin/
		center: new mapboxgl.LatLng( -34.397, 150.644 ),
		center: new mapboxgl.LatLng( 18.5204, 73.8567 ),
		// center : {
		// 	lat: -34.397,
		// 	lng: 150.644
		// },
		disableDefaultUI: false, // Disables the controls like zoom control on the map if set to true
		scrollWheel: true, // If set to false disables the scrolling on the map.
		draggable: true, // If set to false , you cannot move the map around.
		// mapTypeId: mapboxgl.MapTypeId.HYBRID, // If set to HYBRID its between sat and ROADMAP, Can be set to SATELLITE as well.
		// maxZoom: 11, // Wont allow you to zoom more than this
		// minZoom: 9  // Wont allow you to go more up.
	};
	/**
	 * Creates the map using google function mapboxgl.Map() by passing the id of canvas and
	 * mapOptions object that we just created above as its parameters.
	 *
	 */
	// Create an object map with the constructor function Map()
	map = new mapboxgl.Map( element, mapOptions ); // Till this like of code it loads up the map.
	/**
	 * Creates the marker on the map
	 *
	 */
	marker = new mapboxgl.Marker({
		position: mapOptions.center,
		map: map,
		// icon: 'http://pngimages.net/sites/default/files/google-maps-png-image-70164.png',
		draggable: true
	});
	/**
	 * Creates a search box
	 */
	searchBox = new mapboxgl.places.SearchBox( addressEl );
	/**
	 * When the place is changed on search box, it takes the marker to the searched location.
	 */
	mapboxgl.event.addListener( searchBox, 'places_changed', function () {
		var places = searchBox.getPlaces(),
			bounds = new mapboxgl.LatLngBounds(),
			i, place, lat, long,
			addresss = places[0].formatted_address;
		for( i = 0; place = places[i]; i++ ) {
			bounds.extend( place.geometry.location );
			marker.setPosition( place.geometry.location );  // Set marker position new.
		}
		map.fitBounds( bounds );  // Fit to the bound
		map.setZoom( 15 ); // This function sets the zoom to 15, meaning zooms to level 15.
		// console.log( map.getZoom() );
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();
		latEl.value = lat;
		longEl.value = long;
		// Closes the previous info window if it already exists
		if ( infoWindow ) {
			infoWindow.close();
		}
		/**
		 * Creates the info Window at the top of the marker
		 */
		infoWindow = new mapboxgl.InfoWindow({
			content: addresss
		});
		infoWindow.open( map, marker );
	} );


		/**
	/**
	 * Finds the new position of the marker when the marker is dragged.
	 */
	mapboxgl.event.addListener( marker, "dragend", function ( event ) {
		var lat, long, address;
		var lat, long, address, resultArray, citi;

		console.log( 'i am dragged' );
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();
		var geocoder = new mapboxgl.Geocoder();
		geocoder.geocode( { latLng: marker.getPosition() }, function ( result, status ) {
			if ( 'OK' === status ) {  // This line can also be written like if ( status == mapboxgl.GeocoderStatus.OK ) {
				address = result[0].formatted_address;
				resultArray =  result[0].address_components;

				// Get the city and set the city input value to the one selected
				for( var i = 0; i < resultArray.length; i++ ) {
					if ( resultArray[ i ].types[0] && 'administrative_area_level_2' === resultArray[ i ].types[0] ) {
						citi = resultArray[ i ].long_name;
						console.log( citi );
						city.value = citi;
					}
				}
				addressEl.value = address;
				latEl.value = lat;
				longEl.value = long;
			} else {
				console.log( 'Geocode was not successful for the following reason: ' + status );
			}
			// Closes the previous info window if it already exists
			if ( infoWindow ) {
				infoWindow.close();
			}
			/**
			 * Creates the info Window at the top of the marker
			 */
			infoWindow = new mapboxgl.InfoWindow({
				content: address
			});
			infoWindow.open( map, marker );
		} );
	});


}
