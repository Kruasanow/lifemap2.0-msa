var map = L.map('map').setView({lon: 0, lat: 0}, 2);

L.tileLayer('http://192.168.1.9:5080/tile/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="#">Oleg Map</a>'
}).addTo(map);

L.control.scale().addTo(map);

L.marker({lon: 0, lat: 0}).bindPopup('The center of the world').addTo(map);
