<template>
  <header>
      <nav>
        <RouterLink to="/">플랜세이버</RouterLink> |
        <RouterLink to="/map">지도</RouterLink> |
        <RouterLink to="/products">상품 조회</RouterLink> |
        <RouterLink to="/exchange">환율 조회</RouterLink> |
        <RouterLink to="/article">게시판</RouterLink> |
        <RouterLink to="/profile">프로필</RouterLink> |
        <RouterLink to="/signup">회원가입</RouterLink> |
        <RouterLink to="/login">로그인</RouterLink> 
      </nav>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>
