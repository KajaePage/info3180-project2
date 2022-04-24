<template>
    <div class="Upload container">
    <h2>Car View</h2>
    </div>
    <ViewCar />
    <div></div>
 </template>

<script>
    import ViewCar from '@/components/ViewCar.vue'
    export default {
        data() {
        return {};
    },
    components: { ViewCar }
    };
</script>