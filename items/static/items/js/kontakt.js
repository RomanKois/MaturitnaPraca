var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 48.199139, lng: 17.451514},
    zoom: 15
  });
  
  var marker = new google.maps.Marker({position:{lat: 48.199169, lng: 17.451524},
      map:map
  });
}
