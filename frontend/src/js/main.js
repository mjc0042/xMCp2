/* eslint-disable */
import Vue from 'vue';
import router from './http/router'
import store from './store'

import App from '../App.vue';

// Initiate application
new Vue({
  el: '#app',
  router : router,
  store: store,
  render: h => h(App)
});
