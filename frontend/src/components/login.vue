<template>
  <div id="login-popup">
    <!-- Modal Trigger -->
    <b-button v-b-modal.login-modal>Login</b-button>
    
    <!-- Login Modal -->
	<b-modal id="login-modal" title="Login" hide-footer ref="modal">
	  <div id="login-modal-err">{{ errorMessage }}</div>
	  <label for="user-name-input">User Name:</label>
	  <input id="user-name-input" class="form-control" type="text" placeholder="MyUserName" ref="login_username_input"> 
	  <label for="password-input">Password:</label>
	  <input id="password-input" class="form-control" placeholder="password" ref="login_password_input">
	  <div class="modal-footer">
	    <button type="button" class="btn btn-primary" v-on:click.prevent="login">Login</button>
	    <button type="button" class="btn btn-primary" v-on:click="navigateToRegisterUserPage">Register</button>
	    <button type="button" class="btn btn-secondary" v-on:click="closeLoginModal">Cancel</button>
	  </div>
	</b-modal>
  </div>
</template>

<script>
import bButton from 'bootstrap-vue/es/components/button/button';
import bModal from 'bootstrap-vue/es/components/modal/modal';
import bModalDirective from 'bootstrap-vue/es/directives/modal/modal';

export default {
  name: 'login-modal',
  
  components: {
	  'b-button': bButton,
	  'b-modal': bModal  
  },
  directives: {
	  'b-modal': bModalDirective
  },

  data() {
    return {
    	errorMessage: ''
    };
  }, 

  methods: {

	/**
	 * Create call to login user
	 */
    login() {
    	var _self = this;
        var _self_modal = this.$refs.modal;
        this.$store.dispatch('increment', 2);
        this.$store.dispatch('loginUser', { 
        		username: this.$refs.login_username_input.value, 
        		password: this.$refs.login_password_input.value}).then(response => {
        			_self_modal.hide();
        		}, error => {
        			_self.errorMessage = "Incorrect username or password.";
        		});
  	
        
    },
    
    /**
     * Change url to /register 
     */
    navigateToRegisterUserPage() {
		this.$router.push('register');
    },
    
    /**
     * Call to close LoginModal
     */
    closeLoginModal() {
    	this.$refs.modal.hide();
    }
  },
  
  /**
   * Clear login modal data on close
   */
  beforeDestory() {
	  this.errorMessage = '';
  }
}

</script>

<style type="scss">

#login-modal-err {
  width: 100%;
  text-align: center;
  color: red;
}

#login-modal .modal-footer button {
  width: 100%;	
}

</style>