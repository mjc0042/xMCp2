/* eslint-disable */
import Vue from 'vue';
import router from './http/router'

import App from '../App.vue';

// Initiate application
new Vue({
  el: '#app',
  router : router,
  render: h => h(App)
});
