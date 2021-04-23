import 'mdb-vue-ui-kit/css/mdb.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import 'mdb-vue-ui-kit/css/mdb.min.css'

createApp(App)
    .use(router)
    .mount('#app')
