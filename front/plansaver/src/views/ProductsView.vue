<template>
    <nav>
      <h2>상품 조회</h2>
      <div>
        <RouterLink to='/products/deposits'>예금</RouterLink> |
        <RouterLink to='/products/savings'>적금</RouterLink> 
      </div>
    </nav>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<style scoped>

</style>