<template>
	<nav id="page-header" class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
	  <div class="navbar-brand col-lg-3">
	    <router-link to="/">HIMALAYA</router-link> 
	  </div>
	  <div class="collapse navbar-collapse col-lg-10">
		<ul class="navbar-nav col-lg-12">
		  <li class="nav-item col-lg-8 search-bar">
			<form class="form-inline">
			  <div class="col-lg-8">
				<input class="mr-sm-2" type="search" placeholder="Search" aria-label="search"/>
		      </div>
			  <div class="col-lg-4">
			    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
			  </div>
			 </form>
		  </li>
		  <li class="nav-item dropdown" v-if="loggedIn">
			<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				Hello {{ activeUser.name }}!
		    </a>
			<div class="dropdown-menu" aria-labelledby="navbarDropdown">
		       <div class="dropdown-item">
		       	 <!-- <router-link v-bind:to="{ name : '/user', params: { userId: user }}">Profile</router-link> -->
		       	 <div class="dropdown-item" @click=goUserProfile>Profile</div>
		       </div>
			   <div class="dropdown-divider"></div>
			   <a class="dropdown-item" href="#">Logout</a>
			</div>
		  </li>
		  <li class="nav-item" v-if="!loggedIn">
            <login-modal></login-modal>
		  </li>
		</ul>
	  </div>
	</nav>
</template>

<script>

import USER_URL from './js/constants.js';
import LoginModal from './components/login.vue';

export default {
  name: 'page-header',
  
  components: {
	  'login-modal': LoginModal  
  },
  
  props: {
	  auth: { type: Object },
	  authenticated: { type: Boolean }
  },
  
  computed: {
	  loggedIn () {
		  return this.$store.getters.isUserActive;
	  },
	  activeUser() {
		  return this.$store.getters.getActiveUser;
	  }
  },

  methods: {
	  goUserProfile: function () {
		  this.$router.push(USER_URL + this.$options.user );
	  }
  },
  data () {
	  return {
	  }
  },
  
  /**
   * On load function
   */
  mounted: function() { }
}

</script>

<style>

.search-bar input {
  width: 100%;	
}

</style>