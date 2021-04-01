<template>
  <div>
    <b-img :src="img" fluid alt="Responsive image"></b-img>
  </div>
</template>
<script>
export default {
  name: 'contents',
  data () {
    return {
      img: require('@/assets/contentsheader.png')
    }
  }
}
</script>