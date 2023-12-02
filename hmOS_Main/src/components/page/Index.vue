<template>
    <div style="width: 100%; height: 100%;">
        <iframe
            :src="src"
            allowfullscreen="true"
            webkitallowfullscreen="true"
            mozallowfullscreen="true"
            oallowfullscreen="true"
            msallowfullscreen="true"
            name="mapFrame"
            frameborder="0"
            style="width: 100%; height: 100%;"
        >
        </iframe>
    </div>
</template>

<script>
export default {
    data() {
        return {
            src: 'static/index.html'
        };
    }
};
</script>

<style scoped>
</style>