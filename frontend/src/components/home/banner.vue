<template>
   <div class="flex justify-between items-center p-0 mx-auto md:flex md:justify-between md:items-center">
        <v-carousel hide-delimiters height="600">
            <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
            ></v-carousel-item>
        </v-carousel>
    </div>
</template>

<script>
const Banner = {
    data(){
        return {
            items: [
                {src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'},
                {src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'},
                {src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'},
                {src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'},
            ],
        }
    }
}
export default Banner
</script>

<style>

</style>