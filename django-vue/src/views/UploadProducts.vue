<template>
  <div>
    <h2 class="text-center mt-3">Cargar Producto</h2>
    <form @submit.prevent="submitProduct" style="background-color: #f7f7f7; border: 1px solid #ccc; padding: 20px;">
      <fieldset :disabled="formDisabled">
        <legend>Producto</legend>
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="productData.name" class="form-control" required placeholder="Escribe el nombre del producto">
        </div>
        <div class="form-group">
          <label for="imagen">Imagen:</label>
          <input type="file" id="imagen" @change="handleImageUpload" class="form-control" accept="image/*" required>
        </div>
        <div class="form-group">
          <label for="categoria">Categoría:</label>
          <select id="categoria" v-model="productData.category" class="form-select" required>
            <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="descripcion">Descripción:</label>
          <textarea id="descripcion" v-model="productData.description" class="form-control" required placeholder="Escribe la descripción del producto"></textarea>
        </div>
        <div class="form-group">
          <label for="precio">Precio:</label>
          <input type="number" id="precio" v-model="productData.price" class="form-control" required placeholder="Ingrese el precio">
        </div>
        <div class="form-group">
          <label for="price_type">Tipo de Precio:</label>
          <select id="price_type" v-model="productData.price_type" class="form-select" required>
            <option value="unitario">Unidad</option>
            <option value="media-doc">Media Docena</option>
            <option value="docena">Docena</option>
            <option value="por-kilo">Kilo</option>
          </select>
        </div>
        <div class="form-group text-center">
          <button type="submit" class="btn btn-primary btn-lg" style="background-color: #007bff; border-radius: 10px;">Guardar Producto</button>
        </div>
      </fieldset>
    </form>
    <div v-if="successMessage" class="alert alert-success mt-3">{{ successMessage }}</div>
    <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
  </div>
</template>

<script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  export default {
    setup() {
      // Variables reactivas
      const productData = ref({
        name: '',
        image: null,
        category: '',
        description: '',
        price: null,
        price_type: 'unitario',
      });

      const categories = ref([]);
      const successMessage = ref('');
      const errorMessage = ref('');

      // Función para enviar el producto
      const submitProduct = () => {
        const formData = new FormData();
        formData.append('name', productData.value.name);
        formData.append('image', productData.value.image);
        formData.append('category', productData.value.category);
        formData.append('description', productData.value.description);
        formData.append('price', productData.value.price);
        formData.append('price_type', productData.value.price_type);

        axios
          .post('http://127.0.0.1:8000/api/products/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          })
          .then((response) => {
            successMessage.value = 'Producto guardado con éxito';
            errorMessage.value = '';
            productData.value = {
              name: '',
              image: null,
              category: '',
              description: '',
              price: null,
              price_type: 'unitario',
            };
          })
          .catch((error) => {
            successMessage.value = '';
            errorMessage.value = 'Error al guardar el producto. Por favor, verifica los campos y vuelve a intentarlo.';
          });
      };

      // Función para manejar la carga de imágenes
      const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
          productData.value.image = file;
        }
      };

      // Llamada a la API para cargar categorías al montar el componente
      onMounted(() => {
        axios
          .get('http://127.0.0.1:8000/api/categories/')
          .then((response) => {
            categories.value = response.data;
          })
          .catch((error) => {
            console.error('Error al cargar categorías:', error);
          });
      });

      return {
        productData,
        categories,
        successMessage,
        errorMessage,
        submitProduct,
        handleImageUpload,
      };
    },
  };
</script>