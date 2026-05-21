<template>
  <div class="layout">

    <aside class="sidebar">
      <SidebarMenu @node-selected="onSelect" />
    </aside>

    <main class="content">
      <Topbar />
      <MainContent :selectedMenu="selected" />
    </main>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import SidebarMenu from './SidebarMenu.vue'
import MainContent from './MainContent.vue'
import Topbar from './TopBar.vue'

const selected = ref<string>('dashboard')

const onSelect = (val: string) => {
  selected.value = val
}
</script>
