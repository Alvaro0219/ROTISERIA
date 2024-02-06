<template>
    <div>
      <!-- ... El contenido del cuerpo de la página ... -->
  
      <footer class="custom-footer bg-dark text-white text-center py-3">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <h4>Síguenos en redes sociales</h4>
            </div>
            <div class="col-12 mt-3">
              <a href="URL_DE_FACEBOOK" target="_blank" class="social-icon">
                <img src="@/assets/img/facebook.png" alt="Facebook">
              </a>
              <a href="URL_DE_INSTAGRAM" target="_blank" class="social-icon">
                <img src="@/assets/img/instagram.png" alt="Instagram">
              </a>
              <a href="URL_DE_WHATSAPP" target="_blank" class="social-icon">
                <img src="@/assets/img/whats.png" alt="Whatsapp">
              </a>
            </div>
          </div>
        </div>
        <p>&copy; 2023 Rotisería Delicioso Sabor</p>
      </footer>
    </div>
  </template>

  <script setup>

  </script>
  
  <style>
  /* Agrega aquí tus estilos personalizados si es necesario */
  .social-icon {
    margin: 0 10px;
  }
  
  .social-icon img {
    width: 40px; /* Ajusta el tamaño de la imagen según sea necesario */
    height: 40px;
  }
  
  .social-icon:hover img {
    opacity: 0.7; /* Cambia la opacidad de la imagen al pasar el cursor sobre ella */
  }
  </style>
  