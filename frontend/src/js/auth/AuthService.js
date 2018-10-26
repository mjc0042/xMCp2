/* eslint-disable */
import EventEmitter from 'eventemitter3';
import router from '../http/router';
import auth0 from 'auth0-js';
//import Cookies from '../../../node_modules/cookies';

export default class AuthService {
  authenticated = this.isAuthenticated();
  authNotifier = new EventEmitter();

  constructor () {
    this.login = this.login.bind(this);
    this.setSession = this.setSession.bind(this);
    this.logout = this.logout.bind(this);
    this.isAuthenticated = this.isAuthenticated.bind(this);
  };

  auth0 = new auth0.WebAuth({
    domain: 'xmcp2.auth0.com',
    clientID: 'DwlC4FKS4wteOZK4omDJlI1C85SBo6',
    redirectUri: 'localhost:8080/',
    //audience: 'localhost:8080',
    responseType: 'token id_token',
    scope: 'openid profile'
  });

  login () {
      this.auth0.authorize();
  };

  handleAuthentication () {
    this.auth0.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        this.setSession(authResult);
        router.replace('/');
      } else if (err) {
        router.replace('/');
        console.log(err);
        alert(`Error: ${err.error}. Check the console for further details.`);
      }
    });
  };

  setSession (authResult) {
    // Set the time that the access token will expire at
    let expiresAt = JSON.stringify(authResult.expiresIn * 1000 + new Date().getTime());
    console.log('Setting session.', authResult);
    localStorage.setItem('access_token', authResult.accessToken);
    localStorage.setItem('id_token', authResult.idToken);
    localStorage.setItem('expires_at', expiresAt);
    this.authNotifier.emit('authChange', { authenticated: true });
  };

  logout () {
    // Clear access token and ID token from local storage
    localStorage.removeItem('access_token');
    localStorage.removeItem('id_token');
    localStorage.removeItem('expires_at');
    this.userProfile = null;
    this.authNotifier.emit('authChange', false);
    // navigate to the home route
    router.replace('/');
  };

  isAuthenticated () {
    // Check whether the current time is past the
    // access token's expiry time
    let expiresAt = JSON.parse(localStorage.getItem('expires_at'));
    return new Date().getTime() < expiresAt;
  };

  static getAuthToken() {
      //return Cookies.get('csrftoken'); 	
      return localStorage.getItem('access_token');
  };

  static authenticated() {
    let expiresAt = JSON.parse(localStorage.getItem('expires_at'));
    return new Date().getTime() < expiresAt; 
  };

  getUserProfile(cb) {
    var accessToken =  localStorage.getItem('access_token');
    console.log('Get user Profile.', localStorage);
    if(accessToken) {
    	return this.auth0.client.userInfo(accessToken, cb);
    }  else {
    	return null; 
    }
  };
}