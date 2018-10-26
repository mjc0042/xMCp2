<template>
	<div id="user-page" class="container">
	  <h2 class="row">User Page</h2>
	  <div class="row">Hello my name is {{ userId }}!</div>
	</div>
</template>

<script>

export default {
  name: 'user-page', 
  
  created: function () {
	   alert("User ID:" + this.$route.params.userId);
  },
  
  watch: {
	'$route' (to,from) {
	   // watch route changes
	   alert("User ID:" + this.$route.params.userId);
	}  
  },
  
  data () {
	return {
		userId: this.$route.params.userId
	}
  }
}

</script>


<style>

#user-page {
	margin-top: 50px;
}

</style>