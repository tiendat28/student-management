<template>
    <div class="relative bg-slate-900">
        <Header></Header>
        <Banner></Banner>
        <Course></Course>
        <Footer></Footer>
    </div>
</template>

<script>
import Header from '@/components/home/header.vue'
import Banner from '@/components/home/banner.vue'
import Course from '@/components/home/courses.vue'
import Footer from '@/components/home/footer.vue'
const HomePage = {
    components: {
        Header,
        Banner,
        Course,
        Footer
    }
}
export default HomePage
</script>

<style scoped>

</style>