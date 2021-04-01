<template>
  <b-nav>
    <b-nav-item :to="link" append>
      <b-card
        :title="title"
        :img-src="img"
        img-alt="Image"
        img-top
        tag="article"
        style="width: 20rem; height: 25rem;"
        class="mb-2"
      >
        <b-card-text id="cardtext">
          {{description}}
        </b-card-text>
      </b-card>
    </b-nav-item>
  </b-nav>
</template>

<script>
export default {
  name: 'reportnavcard',
  props: {
    img: String,
    title: String,
    description: String,
    link: String
  }
}
</script>
<style scoped>
#cardtext {
  text-align: left;
}
</style>