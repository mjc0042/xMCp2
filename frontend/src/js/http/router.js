/* eslint-disable */

import Vue from 'vue'
import Router from 'vue-router';
import AuthService from '../auth/AuthService'

import Home from '@/home';
import User from '@/user';
import Callback from '@/callback';
import RegisterUser from '@/components/registeruser';

Vue.use(Router);

const routes = [
  {
	path: '/',
	name: 'home-page',
	component: Home
  },
  {
	path: '/user/:userId', 
	name: 'user-page',
	component: User 
  },
  {
	path: '/register',
	name: 'register-user-page',
	component: RegisterUser
  },
  {
	path: '/callback',
	name: 'Callback',
	component: Callback
  },
  {
    path: '/product-list',
    name: 'ProductList',
    //component: ProductList,
    meta: { requiresAuth : true }
  },
  {
    path: '/product-create',
    name: 'ProductCreate',
    //component: ProductCreate,
    meta: { requiresAuth : true }    
  },
  {
    path: '/product-update/:pk',
    name: 'ProductUpdate',
    //component: ProductCreate
  }];

const router = new Router({
  mode: 'history',
  routes
});


router.beforeEach((to, from, next) => {
  console.log('routing ', from, AuthService.authenticated());
  if(to.meta.requiresAuth)
  {
    if(!AuthService.authenticated())
    {
      next('/');
    }
  }
  next();
});

export function authGuard(to, from, next) {

  if(!AuthService.authenticated()) {
    next('/');
  }
  next();

};

export default router;