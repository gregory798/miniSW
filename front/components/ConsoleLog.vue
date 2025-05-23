<template>
    <pre
        style="position: fixed; bottom: 0; width: 100%; height: 200px; overflow: auto; background: #000; color: #0f0; font-size: 12px; padding: 10px;">
      <div v-for="line in logs" :key="line">{{ line }}</div>
    </pre>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const logs = ref([])

onMounted(() => {
    const original = console.log
    console.log = (...args) => {
        logs.value.push(args.map(a => String(a)).join(' '))
        original(...args)
    }
})
</script>