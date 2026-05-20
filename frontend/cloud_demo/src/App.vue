<script setup lang="ts">
import { onMounted, ref } from 'vue'
import axios from 'axios'

const items = ref<string[]>([])
const status = ref('Lade Daten...')

const apiUrl = import.meta.env.VITE_API_URL

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/api/data`)

    items.value = response.data.items
    status.value = 'Backend verbunden'
  } catch (error) {
    status.value = 'Backend nicht erreichbar'
    console.error(error)
  }
})
</script>

<template>
  <div class="container">
    <h1>Cloud Platform</h1>

    <p>{{ status }}</p>

    <ul>
      <li v-for="item in items" :key="item">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<style>
.container {
  padding: 40px;
  font-family: Arial, sans-serif;
}
</style>
