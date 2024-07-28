function showMap() {
  var map = L.map('map');
  map.setView([55.7422, 37.5719], 11);
  L.tileLayer('http://192.168.1.9:5080/tile/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="#">Oleg Map</a>'
  }).addTo(map);
  var m = document.getElementById("map");
  m.style.width = "100vw";
  m.style.height = "50vh";
};
showMap();
