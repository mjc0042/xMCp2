import axios from 'axios';
import AuthService from '../auth/AuthService';

const API_URL = 'http://localhost:8000';

export class APIService {

	/**
	 * Constructor
	 */
    constructor() { }

    /**
     * API CALL: Get all products
     */
    getProducts() {
        const url = `${API_URL}/api/products/`;
        console.log('Getting all products', AuthService.getAuthToken());
        return axios.get(url, { 
        	headers: { 
        		Authorization: `Bearer ${AuthService.getAuthToken()}`,
        		'X-CSRFToken': `${AuthService.getAuthToken()}`	
        	}}).then(response => response.data);
    };
    
    /**
     * API CALL: Get product by ID
     */
    getProduct(pk) {
        const url = `${API_URL}/api/products/${pk}`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }}).then(response => response.data);
    };  
    
    /**
     * API CALL: Get product by URL
     */
    getProductsByURL(link){
        const url = `${API_URL}${link}`;
        console.log('Getting products by URL.');
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }}).then(response => response.data);
    };
    
    /**
     * API CALL: Delete product by ID
     */
    deleteProduct(product){
        const url = `${API_URL}/api/products/${product.pk}`;
        return axios.delete(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }});
    };
    
    /**
     * API CALL: Create Product
     */
    createProduct(product){
        const url = `${API_URL}/api/products/`;
        const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.post(url,product,{headers: headers});
    };
    
    /**
     * API CALL: Update Product
     */
    updateProduct(product){
        const url = `${API_URL}/api/products/${product.pk}`;
        const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.put(url,product,{headers: headers});
    };  
}
