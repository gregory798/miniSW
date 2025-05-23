export default defineEventHandler(async () => {
    const res = await fetch('http://127.0.0.1:8000/random')
    const json = await res.json()
    return json
})