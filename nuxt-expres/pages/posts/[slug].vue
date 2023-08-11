<template>
    <div>
        <h1>Hello iam single post here.</h1>
        <div class="grid md:grid-cols-4 sm:grid-cols-1 justify-items-center bg-cyan-50">
            <div>
                <PostDetail :id="id" :title="title" :content="content" :image="image" />
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
const content = ref("Hello i am do here");
const image = ref('Image is here')
</script>
