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
		  <li class="nav-item dropdown" v-if="authenticated">
			<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				Hello {{ $options.user }}!
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
		  <li class="nav-item" v-if="authenticated">
		    <button class="btn btn-primary btn-margin" v-if="!authenticated" @click="login()">Log In</button>
		  </li>
		</ul>
	  </div>
	</nav>
</template>

<script>

export default {
  name: 'page-header', 
  
  user: 'Mike',
  
  props: {
	  auth: { type: Object },
	  authenticated: { type: Boolean }
  },

  methods: {
	  goUserProfile: function () {
		  this.$router.push('/user/' + this.$options.user );
	  },
	  login: function () {
		  console.log("Attempted login");
	  }
  },
  data () {
	  return {
	  }
  },
  
  /**
   * On load function
   */
  mounted: function() {
	 console.log('navbar mounted.', authenticated); 
  }
}

</script>

<style>

.search-bar input {
  width: 100%;	
}

</style>