<template>
    <Header/>
    <h1>Chinese character coloring app</h1>
    <div class="text-area-wrapper">
        <MDBTextarea
            id="mdb-textarea"
            rows="5"
            type="textarea"
            :value="appliedText"
            @input="sendText"
        />
    </div>
    <div class="styled-text-cointaner">
        <StyledText
        style="styled-text-border"
            :textData="appliedText"
        />
        <Counter
        id="counter"
        :glyphStats="counter"
        :totalGlyphs="totalGlyphs"
        />
    </div>
</template>

<script>
import { MDBTextarea } from 'mdb-vue-ui-kit';

import Header from '@/components/Header.vue';
import StyledText from '@/components/StyledText.vue';
import Counter from '@/components/Counter.vue';

import { $api } from '@/api/mainApi.js';


export default {
    components:  {
        Header,
        MDBTextarea,
        StyledText,
        Counter,
    },
    data() {
        return {
            appliedText: '',
            counter: '',
            totalGlyphs: 0,
        }
    },
    methods: {
        sendText: async function(textarea) {
            if (textarea.target != null) {
                var text = textarea.target.value
                var form = new FormData();
                form.set('text', String(text));

                await $api.postAPI.postCharacters(form)
                .then(response => {
                    var validatedText = [];
                    var counter = [];
                    for (let data of response.body) {
                        validatedText.push(data)
                    }
                    for (let [radical, count] of Object.entries(response.stats)) {
                        counter.push({radical: radical, count: count})
                    }
                    this.appliedText = validatedText;
                    this.counter = counter;
                    this.totalGlyphs = Object.keys(response.body).length;
                    console.log(this.totalGlyphs)
                })
                .catch(error => {
                    console.log(error)
                });
            }
        },
    }
}

</script>

<style>
.text-area-wrapper {
    display: inline;
    width: 40vw;
    height: 10vh;
    margin-left: auto;
    margin-right: auto;
}
.styled-text-cointaner {
    display: flex;
    justify-content: center;
    margin-top: 2em;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
    width: 100em;
}

</style>

