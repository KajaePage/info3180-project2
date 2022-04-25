<script>
export default {
    data() {
        return {
            message: ""
        };
    },
}
</script>

<template>
    <div class="container">
        <img alt="Car Image" class="Car" src="@/assets/RedCar.jpeg" width="650" height="710" />
    <div class="content">
        <h1>Buy and Sell</h1>
        <h1 class="b">Cars Online </h1>
        <p> United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell ars online. Find a Great Price on the Vehicle You Want.</p>
        <button class="register">Register</button>
        <button class="login">Login</button>
    </div>
    </div>
</template>

<style>
.Car{
  padding: 0%;
}
img{
  position: absolute;
  top:0px;
  left: 57.7%;
}
.content{
  margin-top: 150px;
  margin-left: 50px;
}
h1{
  font-size: 60px;
  font-weight: bold;
}
.b{
  padding-bottom: 20px;
}
p{
  margin-right: 68.7%;
  padding-bottom: 10px;
  font-size: 16px;
  color:#91949b;
}

.register{
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 40px;
  padding-right: 40px;
  margin-right: 15px;
  border-radius: 5px;
  border-color: #3b82f6;
  border-style: none;
  background-color: #3b82f6;
  color: white;
  margin-bottom: 130px;
}

.login{
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 50px;
  padding-right: 50px;
  border-radius: 5px;
  border-color: #0fb881;
  border-style: none;
  background-color: #0fb881;
  color: white;
}
</style>