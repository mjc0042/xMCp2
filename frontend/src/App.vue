<template>
  <div id="app">
    <nav-bar v-bind:auth="auth" v-bind:authenticated="authenticated"></nav-bar>
    <div class="container">
	  <router-view v-bind:auth="auth" v-bind:authenticated="authenticated"></router-view>
	</div>
  </div>
</template>

<script>

// Import all css dependencies
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/font-awesome/css/font-awesome.min.css";
//import "./css/main.css";
import "./css/products.css";

//Import all js dependencies
import "../node_modules/bootstrap/dist/js/bootstrap.min.js";

import Navbar from './navbar.vue';
import AuthService from './js/auth/AuthService';

const auth = new AuthService()

const { login, logout, authenticated, authNotifier } = auth

export default {
  name: 'app',
  
  components: {
      'nav-bar': Navbar	  
  },

  data () {
    authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    });
    return {
      auth,
      authenticated
    }
  },
  methods: {
    login,
    logout
  }
}

</script>

