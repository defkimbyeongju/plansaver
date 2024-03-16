<template>
    <div v-if="deposits">
      <table>
        <thead>
          <tr>
            <th>공시 제출일</th>
            <th>은행</th>
            <th>상품명</th>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
            <!-- Add other column headers based on your deposit structure -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="deposit in paginatedDeposits" :key="deposit.id">
            <td>{{ deposit.dcls_month }}</td>
            <td>{{ deposit.kor_co_nm }}</td>
            <td>{{ deposit.fin_prdt_nm }}</td>
            <td>{{ deposit.intr_rate_6 }}</td>
            <td>{{ deposit.intr_rate_12 }}</td>
            <td>{{ deposit.intr_rate_24 }}</td>
            <td>{{ deposit.intr_rate_36 }}</td>
            <!-- Add other columns based on your deposit structure -->
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

const deposits = ref(null);
const store = useCounterStore();
const currentPage = ref(1);
const itemsPerPage = 10;

const getDeposits = () => {
  store.getDeposits();
};

onMounted(() => {
  getDeposits();
});

watch(store, () => {
  deposits.value = store.deposits;
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
  if (!deposits.value) return 0;
  return Math.ceil(deposits.value.length / itemsPerPage);
});

const paginatedDeposits = computed(() => {
  if (!deposits.value) return [];
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return deposits.value.slice(startIndex, endIndex);
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