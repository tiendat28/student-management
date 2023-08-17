<template>
    <div class="fixed w-full">
        <Header></Header>
        <div class="flex">
            <Sidebar></Sidebar>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/layout/client/teacher/sidebar.vue'
import Header from '@/components/layout/client/header.vue'

const Admin = {
    components:{
        Sidebar,
        Header
    }
}
export default Admin
</script>

<style scoped>

</style>