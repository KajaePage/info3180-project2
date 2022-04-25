
<template>
    <div class="formcontainer">
        <h2 class="center">Login to your account</h2>
        <div class="card" style="width: 20rem; height: 17rem; margin-left: 5px; margin-left: 250px;">
        <LoginForm />
        </div>
    </div>
    
</template>


<script>
    import LoginForm from "@/components/LoginForm.vue";
    export default {
        data() {
        return {};
        },
    components: {LoginForm}
    };
    
</script>
<style>
.formcontainer{
    margin-left: 320px;
    margin-top: 120px;
}

.center{
    position: absolute;
    left: 570px;
    top: 130px;
    font-weight: bold;
}

.form-field-1{
    position: absolute;
    top: 20px;
    right: 30px;
    width: 80%;
}

.form-field-2{
    position: absolute;
    top: 100px;
    right: 30px;
    width: 80%;
}
.buttonlog{
    position: absolute;
    top: 200px;
    left: 34px;
    width: 80%;
    border-radius: 5px;
    color: white;
    padding: 10px;
    border-style: none;
}
</style>