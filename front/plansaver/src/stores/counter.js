import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const deposits = ref(null)
  const savings = ref(null)
  const exchanges = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  // DRF에 deposits 조회 요청을 보내는 action
  const getDeposits = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposits/new-deposits/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      deposits.value = res.data
      // console.log(deposits)
    })
    .catch((err) => {
      console.log(err)
    })
  }
  const getSavings = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposits/new-savings/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      savings.value = res.data
      // console.log(deposits)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const getExchanges = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/exchange-rate/exchange/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
    .then((res) => {
      exchanges.value = res.data
      console.log(exchanges)
    })
    .catch((err) => {
      console.log(err)
    })
  }


  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function(payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function(payload) {
    const {username, password} = payload
    axios({
      method:'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((res) => {
      console.log(res)
      token.value = res.data.key
    })
    .catch((err) => {
      console.log(err)
    })
  }
  return {getDeposits, API_URL, deposits, getExchanges, exchanges, articles, getArticles, signUp, logIn, token, isLogin, getSavings, savings}
}, { persist: true })
