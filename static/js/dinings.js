var map; // 지도 객체를 전역 변수로 선언

// localStorage에서 위치 정보를 읽어와서 LatLng 객체를 생성합니다.
var savedLatitude = localStorage.getItem('latitude');
var savedLongitude = localStorage.getItem('longitude');
var position = new kakao.maps.LatLng(savedLatitude, savedLongitude);

function initMap() {
  // 지도를 생성합니다.
  var container = document.getElementById('map');
  var options = {
    center: position || new kakao.maps.LatLng(33.450701, 126.570667),
    level: 3
  };
  map = new kakao.maps.Map(container, options);

  // 이전에 저장한 위치가 있을 경우 지도에 표시
  var location = localStorage.getItem("location");
  if (location) {
    var locationElement = document.getElementById("location");
    locationElement.innerHTML = location;
    loadLocation(); // 이전에 저장된 위치 정보를 불러옵니다.
  } else {
    getLocation(); // 이전에 저장된 위치 정보가 없으면 현재 위치를 찾습니다.
  }
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;

      // 사용자 위치 마커 생성
      var markerPosition = new kakao.maps.LatLng(latitude, longitude);
      var marker = new kakao.maps.Marker({
        position: markerPosition
      });
      marker.setMap(map);

      // 지도 중심 위치 변경
      var centerPosition = new kakao.maps.LatLng(latitude, longitude);
      map.setCenter(centerPosition);
    });
  } else {
    alert("위치 정보를 가져올 수 없습니다.");
  }
}

function loadLocation() {
  var location = localStorage.getItem("location");
  if (location) {
    var locationElement = document.getElementById("location");
    locationElement.innerHTML = location;
  }
}

window.onload = function() {
  initMap(); // 지도 초기화 함수를 호출합니다.
};

function clearLocation() {
  localStorage.removeItem("location");
  var locationElement = document.getElementById("location");
  locationElement.innerHTML = "";
}