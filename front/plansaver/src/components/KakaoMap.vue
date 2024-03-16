<template>
  <div class="container">
    <input type="text" v-model="location" />
    <input type="submit" value="검색" @click="showNearbyBanks" />
    <div id="map"></div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  data() {
    return {
      location: null,
      infoWindow: null,
    };
  },
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
  },
  methods: {
    addKakaoMapScript() {
      const script = document.createElement('script');
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        'https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=0d20b54cf8ee778791133765274ed4ad&libraries=services,clusterer,drawing';
      document.head.appendChild(script);
    },
    initMap() {
      let container = document.getElementById('map');
      let options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      };

      this.map = new kakao.maps.Map(container, options);

      watch(
        () => this.location,
        () => {
          this.showNearbyBanks();
        }
      );

      kakao.maps.event.addListener(this.map, 'click', () => {
        if (this.infoWindow) {
          this.infoWindow.close();
        }
      });
    },
    showNearbyBanks() {
      let ps = new kakao.maps.services.Places(this.map);

      ps.keywordSearch(this.location, (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
          const center = new kakao.maps.LatLng(data[0].y, data[0].x);
          this.map.panTo(center);

          ps.categorySearch('BK9', this.placesSearchCB, {
            location: center,
            radius: 1000,
          });
        }
      });
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        for (var i = 0; i < data.length; i++) {
          this.displayMarker(data[i]);
        }
      }
    },
    displayMarker(place) {
      var marker = new kakao.maps.Marker({
        map: this.map,
        position: new kakao.maps.LatLng(place.y, place.x),
      });

      kakao.maps.event.addListener(marker, 'click', () => {
        if (this.infoWindow) {
          this.infoWindow.close();
        }

        this.infoWindow = new kakao.maps.InfoWindow({
          content: `<div class="infowindow-content">${this.splitString(place.place_name)}</div>`,
        });
        this.infoWindow.open(this.map, marker);
      });
    },
    splitString(str) {
      // 띄어쓰기가 있으면 줄바꿈
      return str.replace(' ', '<br>');
    },
  },
};
</script>

<style>
.container {
  margin-right: 10px;
}
#map {
  width: 700px;
  height: 500px;
}
.infowindow-content {
  font-family: Arial, sans-serif;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 10px;
  padding: 10px;
  max-width: 200px;
}
</style>