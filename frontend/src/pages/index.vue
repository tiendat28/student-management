<template>
    <div class="relative bg-slate-900">
        <Header></Header>
        <Banner></Banner>
        <About></About>
        <Course></Course>
        <New></New>
        <Partner></Partner>
        <Footer></Footer>
    </div>
</template>

<script>
import Header from '@/components/home/header.vue'
import Banner from '@/components/home/banner.vue'
import About from '@/components/home/about.vue'
import Course from '@/components/home/courses.vue'
import New from '@/components/home/new.vue'
import Partner from '@/components/home/partner.vue'
import Footer from '@/components/home/footer.vue'
const HomePage = {
    components: {
        Header,
        Banner,
        About,
        Course,
        New,
        Partner,
        Footer
    }
}
export default HomePage
</script>

<style scoped>

</style>