<template>
    <div class="fixed w-full h-screen">
        <div class="flex w-full h-screen">
            <Sidebar></Sidebar>
            <div class="bg-[#f1f5f9] w-full">
                <Header></Header>
                <div class="p-8 min-h-[calc(100vh-190px)]">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/layout/admin/sidebar.vue'
import Header from '@/components/layout/admin/header.vue'

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