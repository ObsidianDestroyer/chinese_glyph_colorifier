<template>
    <p
        v-if="glyphStats"
    >
        <span
            v-for="glyph in glyphStats"
            :key="glyph"
            class="counter"
        >
            <span class="radical-style">
                Radical: <strong>{{glyph.radical}}</strong>;
            </span>
            <span class="count-style">
                Count: <strong>{{glyph.count}}</strong>;
            </span>
            <span class="percentage-style">
                Percentage: <strong>{{Math.round(glyph.count / totalGlyphs * 100)}}</strong>%
            </span>
        </span>
    </p>
</template>

<script>
import { defineComponent } from 'vue';


export default defineComponent({
    name: 'Counter',
    props: {
        glyphStats: {
            type: Array[Object],
        },
        totalGlyphs: {
            type: Number,
        },
    }
})

</script>

<style>
.counter {
    display: flex;
    justify-content: space-between;
    justify-items: center;
}
.radical-style {
    padding-left: 20px;
    padding-right: 20px;
}

.count-style {
    padding-left: 20px;
    padding-right: 20px;
}

.percentage-style {
    padding-left: 20px;
    padding-right: 20px;
}
</style>