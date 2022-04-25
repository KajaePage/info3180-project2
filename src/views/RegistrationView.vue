
<template>
    <div class="form container">
        <h2 style="font-weight: bolder; margin-left: 49px; margin-left: 245px; margin-bottom: 20px;">Register New User</h2>
        <div class="card" style="width: 40rem; height: 35rem; padding:20px; margin-left: 49px; margin-left: 245px;">
            <RegistrationForm />
        </div>
    </div>
    
</template>


<script>
    import RegistrationForm from "@/components/RegistrationForm.vue";
    export default {
        data() {
        return {};
        },
    components: {RegistrationForm}
    };
    
</script>
<style>
body{
    background-color: #f3f4f6;
}
.card{
     box-shadow: 2px 4px #c2c3c5;
}
.form-field1{
    position: absolute;
    top: 20px;
    left: 40px;
}
.form-field2{
    position: absolute;
    top: 20px;
    right: 40px;
}
.form-field3{
    position: absolute;
    top: 100px;
    left: 40px;
}
.form-field4{
    position: absolute;
    top: 100px;
    right: 40px;
}

.form-field5{
    position: absolute;
    top: 180px;
    left: 40px;
}

.form-field6{
    position: absolute;
    top: 265px;
    left: 40px;
}

.form-field7{
    position: absolute;
    top: 405px;
    left: 40px;
}

.buttonreg{
    position: absolute;
    top: 498px;
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
</style>