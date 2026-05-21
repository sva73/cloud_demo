<template>
  <div class="topbar">

    <div class="left">
      <h1 class="title">PrimeVue Dashboard SVA</h1>
    </div>

    <div class="right">
      <Button
        label="Logout"
        icon="pi pi-sign-out"
        severity="danger"
        @click="logout"
      />
    </div>

  </div>
</template>

<script setup lang="ts">
import Button from 'primevue/button'

const logout = () => {
  // später: API Call / Auth Store / Router Redirect
  console.log('Logout clicked')
}
</script>

<style scoped>
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 1rem;
  margin-bottom: 1rem;

  background: white;
  border-radius: 10px;
}

.title {
  font-size: 1.2rem;
  font-weight: 600;
}

.right {
  display: flex;
  gap: 0.5rem;
}
</style>
