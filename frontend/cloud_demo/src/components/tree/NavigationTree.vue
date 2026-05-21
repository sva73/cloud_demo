<template>
  <MyTree
    :value="nodes"
    selectionMode="single"
    @nodeSelect="onSelect"
  />
</template>

<script setup lang="ts">
import { ref } from 'vue'

type Node = {
  key: string
  label: string
  data: string
}

const emit = defineEmits<{
  (e: 'selected', value: string): void
}>()

const nodes = ref<Node[]>([
  { key: '1', label: 'Dashboard', data: 'dashboard' },
  { key: '2', label: 'Users', data: 'users' },
  { key: '3', label: 'Settings', data: 'settings' }
])

const onSelect = (event: any) => {
  emit('selected', event.node.data)
}
</script>
