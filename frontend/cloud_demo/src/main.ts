import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from 'primevue/config'

import Tree from 'primevue/tree'
import Card from 'primevue/card'
import Button from 'primevue/button'

import 'primeicons/primeicons.css'

import './assets/styles.css'

const app = createApp(App)

app.use(PrimeVue)

// globale Komponenten
app.component('MyTree', Tree)
app.component('MyCard', Card)
app.component('MyButton', Button)

app.mount('#app')
