<template>
    <!-- Barra de navegación superior -->
    <nav class="navbar" style="background-color: #e3f2fd;">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">
            <img src="@/assets/img/logo.png" alt="" width="30" height="24" class="d-inline-block align-text-top">
            Rotiseria
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/">Inicio</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="/about">Acerca de nosotros</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="/upload">Agregar productos</a>
                </li>
            </ul>
            <form class="d-flex" role="search" @submit.prevent="submitForm">
                <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search" v-model="searchText">
                <button class="btn btn-outline-success" type="submit" @click="getSearch">Buscar</button>
            </form>
            </div>
        </div>
    </nav>
    
</template>

<script setup>
    import {ref, defineEmits} from 'vue'

    const searchText = ref('')

    const emitSearch = defineEmits(['getSearchText'])

    const getSearch = () => {
        emitSearch('getSearchText', searchText.value)
    }
</script>

<style>
    /* Estilos adicionales del footer*/
</style>
