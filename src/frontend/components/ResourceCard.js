// components/ResourceCard.js

<template>
    <div class="resource-card">
        <h3>{{ resource.name }}</h3>
        <p>Amount: {{ resource.amount }}</p>
    </div>
</template>

<script>
export default {
    name: 'ResourceCard',
    props: {
        resource: {
            type: Object,
            required: true
        }
    }
};
</script>

<style scoped>
.resource-card {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}
</style>
