<template>
    <div>
        haha
    </div>
    
</template>

<script>
const Home = {
    data(){
        return{
            data: [],
            editdata:{id:'', users:'', password:'', surname: '', name: '', email: '', active: 'true'},
        }
    },
    methods:{
        getAccount(){
            const token = localStorage.getItem('token')
            if (!token) {
                this.$router.push('/login');
            } else {

            }
        },
    },
    mounted(){
      this.getAccount()
    }
}
export default Home
</script>

<style scoped>

</style>