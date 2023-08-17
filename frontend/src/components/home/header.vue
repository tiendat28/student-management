<template>
    <div class="bg-slate-900 sticky top-0 z-10">
        <div class="container flex justify-between items-center p-4 mx-auto md:flex md:justify-between md:items-center">
            <div>
                <router-link to="/" class=" text-xl font-bold md:text-2xl xl:text-3xl flex">
                    <div>
                        <v-icon :size="40" color="#06b6d4">mdi-shimmer</v-icon>
                        <span class="px-3 text-[#06b6d4]">FiveDream</span>
                    </div>
                </router-link>
            </div>
            <div class="flex">
                <ul :class="showMenu ? 'flex' : 'hidden'" 
                    class=" flex justify-center items-center space-y-4 md:flex md:space-y-0 md:flex-row md:items-center md:space-x-10 md:mt-0 cursor-pointer uppercase">
                    <a href="#about" class="font-bold hover:border-b-4 hover:border-[#06b6d4]">
                        <li>giới thiệu</li>
                    </a>
                    <a href="#courses" class="font-bold hover:border-b-4 hover:border-[#06b6d4]">
                        <li>khóa học</li>
                    </a>
                    <a href="#news" class="font-bold hover:border-b-4 hover:border-[#06b6d4]">
                        <li>tin tức</li>
                    </a>
                    <a href="#contact" class="font-bold hover:border-b-4 hover:border-[#06b6d4]">
                        <li>liên hệ</li>
                    </a>
                </ul>

                <div class="pl-[30px]">
                    <v-btn @click="login()" style="text-color: white" color="#06b6d4">Login</v-btn>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
const Header = {
    methods: {
        login(){
            this.$router.push('/login')
        }
    }
}
export default Header
</script>

<style scoped>
.v-application a {
    color: #cbd5e1;
}

</style>