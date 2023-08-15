
<template>
    <div>
        <div v-if="pending">
            <h1>Pending ......</h1>
        </div>
        <div v-if="error">
            <h1>Error is {{ error }} ......</h1>
        </div>
        <div class="grid md:grid-cols-4 sm:grid-cols-1 justify-items-center bg-cyan-50">
            <div v-for="post in posts" :key="post.id">
                <PostCard :id="post.id" :title="post.title" :description="post.description" :slug="post.slug" />
            </div>
        </div>

    </div>
</template>


<script setup>
// This will work in both `<script setup>` and `<script>`
definePageMeta({
    layout: "custom",
});

const id = ref(12);
const title = ref("Batman Brown City");
const description = ref("Hello i am do here");
const slug = ref('Slug is here')

const { pending, data: posts, error } =
    await useLazyFetch('http://localhost:8000/api/posts/')

</script>