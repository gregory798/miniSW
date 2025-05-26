<template>
    <div>
        <h1>Hello world !</h1>
        <button @click="generate">Generate Number</button>
        <p>Number is: {{ number }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const number = ref(null)
async function generate() {
    try {
        const res = await fetch('/random')
        const text = await res.text()
        console.log(text)
        const json = JSON.parse(text)
        number.value = json.number
    } catch (e) {
        console.error("Error in generate()", e)
    }
}
</script>