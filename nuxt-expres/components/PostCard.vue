<script setup>
defineProps(["id", "title", "content", "image"]);
</script>

<template>
    <div class="bg-cyan-50 rounded-lg shadow-md overflow-hidden m-4 px-2">
        <div class="p-1 py-4">
            <h3 class="font-semibold text-lg mb-2 text-center">{{ title }}</h3>
            <nuxt-img :src="image" placeholder="Elise is here" loading="lazy" sizes="sm:100vw md:50vw lg:400px" />
            <p class="text-gray-500 text-sm mb-2 px-2">Content: {{ content }}</p>
            <div class="mt-4 p-2 text-right">
                <NuxtLink :to="{ name: 'posts-slug', params: { slug: 125 } }"
                    class="bg-rose-500 hover:bg-rose-600 text-white font-medium py-2 px-4 rounded">Get Details</NuxtLink>
            </div>
        </div>
    </div>
</template>

<style scoped>
.h-400 {
    height: 400px;
}

.w-300 {
    width: 300px;
}
</style>
