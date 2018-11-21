import Vue from 'vue';
import Vuex from 'vuex';
import { APIService } from '@/js/http/APIService';

Vue.use(Vuex);

const apiService = new APIService();

export default new Vuex.Store({
	state: {
		'user': {},
		'isUserActive': false,
		'test': 0
	},
	getters: {
		getActiveUser(state) {
		    return state.user;	
		},
		isUserActive(state) {
			return state.isUserActive;
		}
	},
	mutations: {
		setActiveUser(state, user) {
			state.user = user;	
		},
		setIsUserActive(state, isUserActive) {
				state.isUserActive = isUserActive;
		},
		increment: (state,num) => { 
			return new Promise((resolve, reject) => {
					state.test = state.test + num
					resolve();
			});
		}
		
	},
	actions: {
	    setActiveUser(context, user) {
	    	context.commit('setActiveUser', user);
	    },
	    setIsUserActive(context, isUserActive) {
	        context.commit('setIsUserActive', isUserActive);	
	    },
	    /**
	     * Login User Action
	     * 
	     * @param context - Vuex context
	     * @param payload - Login info: { username, password }
	     */
	    loginUser(context, payload) {
	    	return new Promise((resolve, reject) =>{
	    		apiService.loginUser(payload.username, payload.password).then((response) => {
	    		    if (response.status === 'OK') {
	    		    	context.dispatch('setActiveUser', response.data);
	    		    	context.dispatch('setIsUserActive', true);
	    		    	resolve(response);
	    		    }
	    		    else {
	    		    	reject(response);
	    		    }
	    		}, error => {
	    		    reject(error);	
	    		});
	    	});
	    },
	    async increment(context, num) {
	    	await context.commit('increment', num);
	    }
	}
});