<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Lab 7</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item" v-if="!isvalid">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item" v-if="!isvalid">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li class="nav-item"  v-if="isvalid">
              <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
            </li>
            <li class="nav-item"  v-if="isvalid">
              <RouterLink class="nav-link" to="/cars/new">New Car</RouterLink>
            </li>
            <li class="nav-item"  v-if="isvalid">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import shared from '@/shared';
import { RouterLink } from "vue-router";
export default {
    data() {
      return {
          token: null
      }        
    },
    
    created() {
        this.isValidJwt = shared.isValidJwt;
    },
    mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
    }
    if (localStorage.username) {
      this.username = localStorage.username;
    }
    },
    computed: {
        isvalid() {
            return this.isValidJwt(this.token);
        }
    }
    }
</script>

<style>
/* Add any component specific styles here */
</style>