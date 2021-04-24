<template>
    <p v-if="textData" class="styled-text-border">
        <span
            v-for="glyph in textData"
            :key="glyph"
            v-text="glyph.character"
            class="styled-text"
            v-bind:style="{
                color: glyph.color ? glyph.color : 'grey',
                fontSize: '30px'
            }"
        ></span>
    </p>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'StyledText',
    props: {
        textData: {
            type: Array[Object],
        },
    },
    data() {
        return {
            styleObject: {
                color: 'grey',
                fontSize: '25px',
            }
        }
    },
})
</script>


<style>
.styled-text {
    white-space: pre;
}
.styled-text-border {
    padding-left: 20px;
    border-left: 2px rgba(0,0,0,.7) solid;
}
</style>