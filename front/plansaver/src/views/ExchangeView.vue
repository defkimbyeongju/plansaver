<template>
  <div>
    <h1>환율 변환기</h1>
    <label for="amount">금액 입력:</label>
    <input v-model="amount" type="number" id="amount" />

    <label for="fromCurrency">변환하고자 하는 통화:</label>
    <select v-model="fromCurrency">
      <option v-for="currency in currencies" :key="currency.id" :value="currency.id">
        {{ currency.cur_nm }} ({{ currency.cur_unit }})
      </option>
    </select>

    <label for="toCurrency">변환할 통화:</label>
    <select v-model="toCurrency">
      <option v-for="currency in currencies" :key="currency.id" :value="currency.id">
        {{ currency.cur_nm }} ({{ currency.cur_unit }})
      </option>
    </select>

    <button @click="convert">환율 변환</button>

    <div v-if="convertedAmount !== null">
      <p>{{ amount }} {{ fromCurrencyData.cur_unit }}는 {{ convertedAmount.toFixed(2) }} {{ toCurrencyData.cur_unit }}(으)로 변환됩니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted, watch } from 'vue';

const currencies = ref(null);
const store = useCounterStore()
onMounted(() => {
  store.getExchanges();
});

watch(store, () => {
  currencies.value = store.exchanges;
})

const amount = ref(null);
const fromCurrency = ref(null);
const toCurrency = ref(null);
let fromCurrencyData = null;
let toCurrencyData = null;
const convertedAmount = ref(null);

const convert = () => {
  if (amount.value && fromCurrency.value && toCurrency.value) {
    fromCurrencyData = currencies.value.find(currency => currency.id === fromCurrency.value);
    toCurrencyData = currencies.value.find(currency => currency.id === toCurrency.value);
    if (fromCurrencyData && toCurrencyData) {
      const exchangeRate = parseFloat(fromCurrencyData.deal_bas_r.replace(',', '')) / parseFloat(toCurrencyData.deal_bas_r.replace(',', ''));
      convertedAmount.value = amount.value * exchangeRate;
    }
  }
};
</script>

<style scoped>
/* 필요한 경우 스타일 추가 */
</style>