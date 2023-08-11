<script setup>
defineProps(["title", "date", "poster", "revenue", "overview"]);
</script>

<template>
    <div class="grid sm:grid-cols-3 gap-7 justify-items-center m-10">
        <!-- Column 1: Image -->
        <div class="bg-white rounded-lg shadow-md overflow-hidden">
            <img class="h-400 w-full object-cover" :src="poster" alt="Placeholder Image" />
        </div>

        <!-- Column 2: Title, Overview, revenue, Buy Button -->
        <div class="sm:col-span-2 mx-6">
            <h1 class="font-bold text-2xl mb-5">{{ title }}</h1>
            <h3 class="font-semibold text-lg mb-5">Release Date: {{ date }}</h3>
            <p class="text-gray-500 text-md mb-8">
                {{ overview }}
            </p>

            <p class="text-gray-500 text-md">Revenue: $ {{ revenue }}</p>
        </div>
    </div>
</div></template>
 