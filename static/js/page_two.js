// var myMap = L.map("map", {
//     center: [39.50, -98.35],
//     zoom: 5
//   });
  
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  }).addTo(myMap);
  
  var geoData = "data/brew.geoJSON";

  var geojson;
  
  d3.json(geoData, function(data) {
  
    geojson = L.heatLayer(data, {

        valueProperty: "Name",
  
    // Binding a pop-up to each layer
    onEachFeature: function(feature, layer) {
        layer.bindPopup("city " + feature.properties.city + "<br>Brewery Name:<br>" +
          "$" + feature.properties.name);
      }
    }).addTo(myMap);   
  
    var heat = L.heatLayer(heatArray, {
      radius: 20,
      blur: 35
    }).addTo(myMap);
  
  });
