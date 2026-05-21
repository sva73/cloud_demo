<template>
  <NavigationTree @selected="emitSelect" />
</template>

<script setup lang="ts">
import NavigationTree from '../tree/NavigationTree.vue'

const emit = defineEmits<{
  (e: 'node-selected', value: string): void
}>()

const emitSelect = (val: string) => {
  emit('node-selected', val)
}
</script>
