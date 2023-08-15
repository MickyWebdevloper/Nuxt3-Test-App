<script setup>

defineProps(["id", "title", "description", "slug"]);
</script>

<template>
    <div class="bg-cyan-50 rounded-lg shadow-md overflow-hidden m-4 px-2">
        <div class="p-1 py-4">
            <h3 class="font-semibold text-lg mb-2 text-center">Title :{{ title }}</h3>
            <p class="text-gray-500 text-sm mb-2 px-2">Description: {{ description }}</p>
            <!-- <p class="text-gray-500 text-sm mb-2 px-2">Slug: {{ slug }}</p> -->

            <div class="mt-4 p-2 text-right">
                <NuxtLink :to="{
                    name: 'posts-slug', params: { slug: slug }
                }" class="bg-rose-500 hover:bg-rose-600 text-white font-medium
                     py-2 px-4 rounded">
                    Get Details
                </NuxtLink>
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
