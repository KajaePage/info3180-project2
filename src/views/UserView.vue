<template>
    <div class="Upload container">
    <h2>UserData</h2>
    </div>
    <UserProfile />
    <div></div>
 </template>

<script>
    import UserProfile from '@/components/UserProfile.vue'
    export default {
        data() {
        return {};
    },
    components: { UserProfile }
    };
</script>