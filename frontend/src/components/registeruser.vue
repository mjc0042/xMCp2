<template>
  <div id="register-user-page">
    <form>
	  <div class="form-row">
		<div class="form-group col-md-6">
		  <label for="create-account-name">Name</label>
		  <input type="text" class="form-control" id="create-account-name" placeholder="John Smith">
		</div>
		<div class="form-group col-md-6">
		  <label for="create-account-email">Email</label>
		  <input type="email" class="form-control" id="create-account-email" placeholder="Email">
		</div>
		<div class="form-group col-md-6">
		  <label for="create-account-password">Password</label>
		  <input type="password" class="form-control" id="create-account-password" placeholder="password">
		</div>
		<div class="form-group col-md-6">
		  <label for="create-account-verify-password">Verify Password</label>
		  <input type="password" class="form-control" id="create-account-verify-password" placeholder="password">
		</div>
	  </div>
	  <div class="form-group">
		<label for="create-account-address">Address</label>
		<input type="text" class="form-control" id="create-account-address" placeholder="1234 Main St">
	  </div>
	  <div class="form-row">
		<div class="form-group col-md-6">
		  <label for="create-account-city">City</label>
		  <input type="text" class="form-control" id="create-account-city">
		</div>
		<div class="form-group col-md-4">
		  <label for="create-account-state">State</label>
		  <select id="create-account-state" class="form-control">
			<option selected>Choose...</option>
			<option v-for="state in states">{{ state }}</option>
		  </select>
		</div>
		<div class="form-group col-md-2">
		  <label for="create-account-zip">Zip</label>
		  <input type="text" class="form-control" id="create-account-zip">
		</div>
	  </div>
	  <button type="submit" class="btn btn-primary" v-on:click="registerUser">Create Account</button>
	</form>
  </div>
</template>

<script>

export default {
  name: 'register-user-page',

  data() {
    return {
    	state: ['Alaska','Alabama','Arizona','Arkansas','California','Colorado',
    		'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
    		'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
    		'Maine','Maryland','Massachussetts','Michigan','Minnesota','Mississippi',
    		'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
    		'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
    		'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee',
    		'Texas','Utah','Vermont','Virginia','Washington','Washington D.C.',
    		'West Virginia','Wisconsin','Wyoming']
    };
  }, 

  methods: {

	/**
	 * Create call to register user
	 */
    registerUser() {

    	console.log('Attempting to register user.');
		apiService.createUser().then((userData) => {
			  console.log('Registered user: ', userData);
	    });
    }
  },
}

</script>

<style>
</style>