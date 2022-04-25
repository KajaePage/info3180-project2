<template>
    <div class="Upload container">
    <h2>My Profile</h2>
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