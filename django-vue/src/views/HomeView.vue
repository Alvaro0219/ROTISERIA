<template>
  <!--NAVIGATION-->
  <NavbarComponent @getSearchText="search"/>

  <!--NAVIGATION-->
  <NavigationComponent @getCategoryID="categoryID" />
  <!--Retorno segun categorias-->
  <div class="mb-3" v-if="categoryReceived">
    <h3>Productos de la categoria <strong>{{ categoryReceived }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los productos</button>
    <div class="alert alert-warning mt-3" role="alert" v-if="filteredproducts.length === 0">
      No existen productos de la categoria <strong>{{ categoryReceived }}</strong>
    </div>
  </div>

  <div class="mb-3" v-if="searchTextRule">
    <h3>Productos con el texto <strong>{{ searchTextRule }}</strong></h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los productos</button>
    <div class="alert alert-warning mt-3" role="alert" v-if="filteredproducts.length === 0">
      No existen productos con el texto <strong>{{ searchTextRule }}</strong>
    </div>
  </div>

    <div>
      <div class="row">
        <!-- Iteramos por cada producto cargado -->
        <div class="col-md-4 mb-4" v-for="product in filteredproducts" :key="product.id">
          <div class="card">
            <div class="img-container">
              <img :src="product.image" class="card-img-top" alt="Imagen de {{ product.name }}">
            </div>
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <p class="card-subtitle">{{ product.category_name }}</p>
              <p class="card-text">{{ product.description }}</p>
            </div>
            <div class="card-footer">
              PRECIO: $ {{ product.price }} por {{ product.price_type_description }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>

<script setup>
    import axios from 'axios'
    import NavigationComponent from '@/components/NavigationComponent.vue'
    import NavbarComponent from '@/components/NavbarComponent.vue'
    import  {ref, onMounted} from 'vue'

    const products = ref([])
    const filteredproducts = ref([])
    const categoryReceived = ref(null)
    const searchTextRule = ref(null)

    const search = (searchText) => {
      categoryReceived.value = null
      searchTextRule.value = searchText
      
      if (searchText) {
        //Filtro los datos
        filteredproducts.value = products.value.filter((product) => {
          //Bajamos nombre,descripcion y busqueda a minusculas
          const productName = product.name.toLowerCase();
          const productDescription = product.description.toLowerCase();
          const searchTerm = searchText.toLowerCase();
          
          //que me retorne el filtro de los productos que incluya lo que manda el usuario desde la caja de busqueda 
          return (
            productName.includes(searchTerm) ||
            productDescription.includes(searchTerm)
          )
        })
      } else {
        filteredproducts.value = products.value
      }
    }

    //Obtener categorias
    const categoryID = (categoryID, categoryName) => {
        searchTextRule.value = null
        categoryReceived.value = categoryName
        //Filtramos de acuerdo al ID que presiona el user
        if (categoryID) {
          filteredproducts.value = products.value.filter((product) => product.category === categoryID)
        } else {
          filteredproducts.value = products.value
        }
      }

    const resetFilter = () => {
        categoryReceived.value = null
        searchTextRule.value = null
        filteredproducts.value = products.value
      }

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/products/')
        .then(response => {
            products.value = response.data
            filteredproducts.value = products.value
        })
        .catch(error => {
            console.log(error)
        })  
    }) 
        
</script>

<style>
.card {
    border: 2px solid gray !important;
    /* Define fixed dimensions for each card */
    width: 100%;
}

.img-container {
    /* Define a fixed height for the image container */
    height: 200px;
    /* Ensure images cover the entire container without distortion */
    overflow: hidden;
}

.card-img-top {
    /* Set the image to cover the container and maintain aspect ratio */
    object-fit: cover;
    width: 100%;
    height: 100%;
}
</style>