<template>
    <div v-if="savings">
      <table>
        <thead>
          <tr>
            <th>공시 제출일</th>
            <th>은행</th>
            <th>상품명</th>
            <th>예치방식</th>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
            <!-- Add other column headers based on your savings structure -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="savings in paginatedSavings" :key="savings.id">
            <td>{{ savings.dcls_month }}</td>
            <td>{{ savings.kor_co_nm }}</td>
            <td>{{ savings.fin_prdt_nm }}</td>
            <td>{{ savings.rsrv_type_nm }}</td>
            <td>{{ savings.intr_rate_6 }}</td>
            <td>{{ savings.intr_rate_12 }}</td>
            <td>{{ savings.intr_rate_24 }}</td>
            <td>{{ savings.intr_rate_36 }}</td>
            <!-- Add other columns based on your savings structure -->
          </tr>
        </tbody>
      </table>
    </div>
    <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <a class="page-link" href="#" aria-label="Previous" @click="previousPage">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: page === currentPage }">
          <a class="page-link" href="#" @click="changePage(page)">{{ page }}</a>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <a class="page-link" href="#" aria-label="Next" @click="nextPage">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';

const savings = ref(null);
const store = useCounterStore();
const currentPage = ref(1);
const itemsPerPage = 10;

const getSavings = () => {
  store.getSavings();
};

onMounted(() => {
    getSavings();
});

watch(store, () => {
  savings.value = store.savings;
});

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1;
  }
};

const totalPages = computed(() => {
  if (!savings.value) return 0;
  return Math.ceil(savings.value.length / itemsPerPage);
});

const paginatedSavings = computed(() => {
  if (!savings.value) return [];
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return savings.value.slice(startIndex, endIndex);
});

const changePage = (page) => {
  currentPage.value = page;
};

</script>

<style scoped>
/* Add your styles here if needed */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>