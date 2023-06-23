<template>
    <div>
        <Header></Header>
        <Navigation></Navigation>
    </div>
</template>

<script>
import Header from '@/components/header/header.vue'
import Navigation from '@/components/navigation/navigation.vue'
const Home = {
    data(){
        return{
            data: [],
            editdata:{id:'', users:'', password:'', surname: '', name: '', email: '', role:'', active: 'true'},
        }
    },
    components:{
        Header,
        Navigation
    }
}
export default Home
</script>

<style scoped>

</style>