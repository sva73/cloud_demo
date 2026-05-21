<template>
  <section class="main-content-wrapper">

    <DashboardView v-if="selectedMenu === 'dashboard'" />
    <UsersView v-else-if="selectedMenu === 'users'" />
    <SettingsView v-else-if="selectedMenu === 'settings'" />

    <div v-else class="fallback">
      <Card>
        <template #title>Keine Seite gewählt</template>
        <template #content>
          Bitte wähle ein Menü aus.
        </template>
      </Card>
    </div>

  </section>
</template>

<script setup lang="ts">
import Card from 'primevue/card'

import DashboardView from '../../views/DashboardView.vue'
import UsersView from '../../views/UsersView.vue'
import SettingsView from '../../views/SettingsView.vue'

defineProps<{
  selectedMenu: string
}>()
</script>

<style scoped>
.main-content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.fallback {
  padding: 1rem;
}
</style>
