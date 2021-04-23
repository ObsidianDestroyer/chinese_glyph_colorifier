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
        <StyledText
            id="styled"
            :textData="appliedText"
        />
    </div>
</template>

<script>
import { MDBTextarea } from 'mdb-vue-ui-kit';

import Header from '@/components/Header.vue';
import StyledText from '@/components/StyledText.vue';
import { $api } from '@/api/mainApi.js';


export default {
    components:  {
        Header,
        MDBTextarea,
        StyledText,
    },
    data() {
        return {
            appliedText: '',
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
                    for (let data of response) {
                        console.log(data.color)
                        validatedText.push(data)
                    }
                    this.appliedText = validatedText;
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
    width: 40vw;
    height: 10vh;
    margin-left: auto;
    margin-right: auto;
}

</style>

