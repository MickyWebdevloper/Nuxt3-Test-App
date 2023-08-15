<template>
    <div>
        <!-- <h1>Hello iam single post here.</h1>
        <h2>slug - {{ $route.params.slug }}</h2> -->
        <!-- <div v-if="pending">
            <h1>Pending ......</h1>
        </div>
        <div v-if="error">
            <h1>Error is {{ error }} ......</h1>
        </div>
        <div class="grid md:grid-cols-4 sm:grid-cols-1 justify-items-center bg-cyan-50">
            <div>
                <PostDetail 
                :id="post.id" :title="post.title" :description="post.description" 
                :slug="post.slug" />
            </div>
        </div> -->
        <h1>Detil Page</h1>
        <h1 v-if="error">Oops! Error encountered: {{ error }}</h1>
        <h1 v-if="pending">Pending ... </h1>
        <div v-if="post">
            <div class="container">
                <PostDetail :id="post.id" :title="post.title" :description="post.description" :slug="post.slug" />
            </div>
        </div>
    </div>
</template>

<script setup>
// This will work in both `<script setup>` and `<script>`
definePageMeta({
    layout: "custom",
});
const id = ref(123);
const title = ref("Batman Brown City");
const description = ref("Hello i am do here");
const slug = ref('Image is here')
const route = useRoute()

const { pending, data: post, error } =
    await useLazyFetch(`http://localhost:8000/api/posts/${route.params.slug}/`)

</script>
