// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  nitro: { preset: 'static' },
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true }
})
