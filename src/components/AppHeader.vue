<template>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bf-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"><i class="fa fa-car" style="font-size: 20px;color:white;"></i> United Auto Sales</a> 
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
            <li class="nav-item"  v-if="isvalid">
              <RouterLink class="nav-link" to="/users/{{localStorage.user_id}}">My Profile</RouterLink>
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
nav {
  background-color: #202938;
}
i{
  margin-right: 5px;
}
</style>