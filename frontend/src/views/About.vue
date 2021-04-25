<template>
    <link href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
    <div
        class="card"
        v-for="author in thisAuthors"
        :key="author"
        v-bind:style="[author.name == 'Александр Васильев' ? 'margin-top: 0em;' : 'margin-top: 5em;']"
    >
    <div class="card-content">
        <h4 class="subtitle">
        <strong>{{ author.name }}</strong>
        </h4>
        <p class="subtitle">{{ author.jobType }}</p>
        <p v-if="author.sourceCode">
            <span>
                Исходный код <a href="{{ author.sourceCode }}">GitHub</a>
            </span>
        </p>
    </div>
    <footer class="card-footer">
        <p class="card-footer-item">
            <span>
                Посмотреть в <a href="{{ author.link }}">Вконтакте</a>
            </span>
        </p>
    </footer>
    </div>
</template>


<script>
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'AboutCard',
    props: {
        authors: {
            type: Array[String],
        }
    },
    data() {
        return {
            thisAuthors: [
                {
                    name: 'Александр Васильев',
                    jobType: 'Разработчик',
                    link: 'https://vk.com/walther_syndicates',
                    sourceCode: 'https://github.com/ObsidianDestroyer/chinese_glyph_colorifier',
                },
                {
                    name: 'Кристина Железняк',
                    jobType: 'Консультант разработки, автор идеи',
                    link: 'https://vk.com/liang_wanting'
                },
            ],
        }
    },
})
</script>
