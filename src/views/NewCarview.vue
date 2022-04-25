
<template>
    <div class="form container">
        <h2 style="font-weight: bolder; margin-left: 49px; margin-left: 245px; margin-bottom: 20px;">Add New Car</h2>
        <div class="card" style="width: 40rem; height: 43rem; padding:20px; margin-left: 49px; margin-left: 245px;">
        <CarForm />
        </div>
    </div>
    
</template>


<script>
    import CarForm from "@/components/CarForm.vue";
    export default {
        data() {
        return {};
        },
    components: {CarForm}
    };
    
</script>
<style>
body{
    background-color: #f3f4f6;
}
.card{
     box-shadow: 2px 4px #c2c3c5;
}
.make{
    position: absolute;
    top: 20px;
    left: 40px;
}
.model{
    position: absolute;
    top: 20px;
    right: 40px;
}

.color{
    position: absolute;
    top: 100px;
    left: 40px;
}
.year{
    position: absolute;
    top: 100px;
    right: 40px;
}

.price{
    position: absolute;
    top: 180px;
    left: 40px;
}

.type{
    position: absolute;
    top: 180px;
    right: 40px;
}

.transmission{
    position: absolute;
    top: 265px;
    left: 40px;
}
.des{
    position: absolute;
    top: 360px;
    left: 40px;
}

.up{
    position: absolute;
    top: 510px;
    left: 40px;
}
.buttonsave{
    position: absolute;
    top: 620px;
    left: 35px;
    border-radius: 5px;
    margin-left: 6px;
    width: 20%;
    color: white;
    padding: 10px;
    border-style: none;
}

input{
    border-radius: 5px;
}

textarea{
    border-radius: 5px;
}

select{
    border-radius: 5px;
    width: 255px;
    padding: 7px;
}
</style>