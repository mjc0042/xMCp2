<template>
	<div id="home-page" class="container">
	    <h1 class="row">Home Page</h1>
	    <ul class="item-tiles row">
			<div class="col-lg-4" v-for="product in products">
              <div class="card text-center">
                 <div class="card-body">
					  <div class="card-title">
						 {{ product.name }}
					  </div> 
					  <div class="card-text">
						 {{ product.price }}
					  </div>
				  </div>
			  </div>
			</div>
		</ul>
		<ul class="list-horizontal">
		  <li>
         <button class="btn btn-link btn-product-page" v-if="currentPageNum > 0" @click="getPreviousPage()"><i class="fa fa-angle-right" title="Previous"></i></button>
      </li>
		  <li v-for="page in pages" v-if="numberOfPages > 2">
		    <a class="btn btn-primary" @click="getPage(page.link)"></a>
		  </li>
		  <li><button class="btn btn-link btn-product-page" v-if="numberOfPages > 1" @click="getNextPage()"><i class="fa fa-angle-right" title="Next"></i></button></li>
		</ul>
	</div>
</template>

<script>
import { APIService } from './js/http/APIService';

const API_URL = 'http://localhost:8000';
const apiService = new APIService();

export default {
  name: 'home-page',

  data() {
    return {
      selectedProduct:null,
      products: [],
      numberOfPages:0,
      pages : [],
      currentPageNum: 0,
      numberOfProducts:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  }, 

  methods: {

	/**
	 * Create call to fetch products 
	 */
    getProducts() {

      this.loading = true;    

      apiService.getProducts().then((page) => {
        this.products = page.data;
        this.numberOfProducts = page.count;
        this.numberOfPages = page.numpages;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link = `/api/products/?page=${i}`;
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
        this.currentPageNum = 0;
      });
    },

    /**
     * Create call to fetch products
     */
    getPage(link) {
      this.loading = true;  
      apiService.getProductsByURL(link).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });     
    },

    /**
     * Get next page list of products
     */
    getNextPage() {
      this.loading = true;  
      this.currentPageNum++;
      apiService.getProductsByURL(this.nextPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });      

    },

    /**
     * Get previous page list of products
     */
    getPreviousPage(){
      this.loading = true;  
      this.currentPageNum--;
      apiService.getProductsByURL(this.previousPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });      

    },
    
    /**
     * Make call to delete a product
     */
    deleteProduct(product){
      apiService.deleteProduct(product).then((r)=>{
        console.log(r);
        if(r.status === 204)
        {
          alert("Product deleted");
          this.$router.go()

        }
      })
    },

    /**
     * Selecting a Product
     * @param product - information
     */
    selectProduct(product){
      this.selectedProduct = product;
    }
  },

  /**
   * On page load call
   */
  mounted() {
    console.log("Home page loaded: ");
    this.getProducts();
  },
}
</script>

<style lang="scss">

#home-page {
	margin-top: 50px;
}

#home-page .card {
    background: lightgray;
    margin-bottom: 5px;
    &:hover {
    	background: gray;
        cursor: pointer;
    }
}

</style>
