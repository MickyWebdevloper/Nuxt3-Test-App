<script setup>
defineProps(['id', "title", "description", "slug"]);
</script>

<template>
    <div class="grid sm:grid-cols-3 gap-7 justify-items-center m-10">
        <!-- Column 1: Image -->
        <!-- <div class="bg-white rounded-lg shadow-md overflow-hidden">
            <img class="h-400 w-full object-cover" :src="image" alt="Placeholder Image" />
        </div> -->

        <!-- Column 2: Title, Overview, revenue, Buy Button -->
        <div class="sm:col-span-2 mx-6">
            <h1 class="font-bold text-2xl mb-5">Title -> {{ title }}</h1>
            <h3 class="font-semibold text-lg mb-5">ID:-> {{ id }}</h3>
            <p class="text-gray-500 text-md mb-8">
                description -> {{ description }}
            </p>

            <p class="text-gray-500 text-md">Slug -> {{ slug }}</p>
        </div>
    </div>
</template>
 