var map = L.map('map').setView([37.21, 10.12], 14);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {}).addTo(map);

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

var drawControl = new L.Control.Draw({
  draw: {
    polyline: false,
    circle: false,
    marker: true,
    polygon: false,
    rectangle: false,
    circlemarker: false,
  },
});
map.addControl(drawControl);

var lastMarker = null;
var lastPolygon = null;
map.on('draw:created', function (e) {
  var type=e.layerType;
  if (type=='polygon'){
    if (lastPolygon !== null) {
      map.removeLayer(lastPolygon);
    }
    drawnItems.clearLayers();
    var layer = e.layer;
    drawnItems.addLayer(layer);
    var geometry = JSON.stringify(layer.toGeoJSON().geometry);
    document.getElementById("geometry").value = geometry;
  }
  else{
  if (lastMarker !== null) {
    map.removeLayer(lastMarker);
  }
  drawnItems.clearLayers();
  var layer = e.layer;
  drawnItems.addLayer(layer);
  var markerPosition = layer.getLatLng();
  var lat = markerPosition.lat;
  var lng = markerPosition.lng;
  document.getElementById("lat").value = lat;
  document.getElementById("lng").value = lng;
  lastMarker=L.marker([lat,lng]).addTo(map);}
});