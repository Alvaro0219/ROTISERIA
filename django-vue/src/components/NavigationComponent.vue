<template>
    <!-- Sección de cabecera para categorías de productos -->
    <section class="py-4 bg-light">
      <div class="container text-center">
        <h2>Rotiseria</h2>
        <div class="d-flex flex-wrap justify-content-center" v-if="$route.path !== '/about' && $route.path !== '/upload'">
          <!-- Itera botones según la cantidad de categorías -->
          <button type="button" class="btn btn-outline-dark mx-2 text-truncate category-button" v-for="category in categories" :key="category.id" 
          @click="getCategory(category.id, category.name)">{{ category.name }}</button>
        </div>
      </div>
    </section>
</template>
  
<script setup>
    // Traer datos de la API de Django usando axios
    import axios from 'axios'
    import {ref, defineEmits, onMounted} from 'vue'

    const categories = ref([])
    const categoryID = ref(null)
    const categoryName = ref(null)

    //Coponente que emite eventos
    const emit = defineEmits(['getCategoryID'])

    //Metodo para obtener la categoria al presionar el boton
    const getCategory = (id, name) => {
      emit('getCategoryID', id, name)
    }

    onMounted(() => {
      // Obtiene las categorías de la API de Django
      axios.get('http://localhost:8000/api/categories/')
          .then(response => {
            // Rellena el array 'categories' con los datos de la API
            categories.value = response.data
          })
          .catch(error => {
            console.log(error)
          })
    })

</script>
  
  <style scoped>
  .category-button {
    width: 150px; /* Establece un ancho fijo para los botones */
    white-space: nowrap; /* Evita el desbordamiento de texto */
    overflow: hidden;
    text-overflow: ellipsis;
  }
  </style>