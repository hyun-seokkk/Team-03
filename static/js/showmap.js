  function initMap() {
    var location = localStorage.getItem("location");
    if (!location) {
      alert("위치 정보가 없습니다.");
      return;
    }
    
    var mapContainer = document.getElementById("map"); // 지도를 표시할 div
    var options = { // 지도를 생성할 때 필요한 기본 옵션
      center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
      level: 4, // 지도의 확대 레벨
    };
    
    var map = new kakao.maps.Map(mapContainer, options); // 지도 생성
    
    // 주소-좌표 변환 객체 생성
    var geocoder = new kakao.maps.services.Geocoder();
    
    // 주소로 좌표를 검색
    geocoder.addressSearch(location, function(result, status) {
      // 검색에 실패한 경우
      if (status !== kakao.maps.services.Status.OK) {
        alert("지도를 불러올 수 없습니다.");
        return;
      }

      // 검색한 주소에 대한 좌표값을 받아옴
      var latlng = new kakao.maps.LatLng(result[0].y, result[0].x);

      // 지도 중심을 검색한 위치로 이동
      map.setCenter(latlng);

      // 마커 생성
      var marker = new kakao.maps.Marker({
        map: map,
        position: latlng,
      });
    });
  }

  window.onload = function() {
    initMap();
  };