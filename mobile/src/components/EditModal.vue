<template>
</template>

<script>
export default {
  props: ["item0", "projList", "show"],
  mounted() {
      
      console.log("mounted modal")
  },

  watch: {
    show(val) {
      console.log("show changed")
      this.isOpen = val
    }
  },

  data() {
    return {
      isOpen: false,
      item: {
        id: "",
        proj: "",
        desc: "",
        hour: 0,
      },
    }
  },
  methods: {
  }
}
</script>

<style scoped>
</style>
