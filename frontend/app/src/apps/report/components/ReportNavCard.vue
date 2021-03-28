<template>
  <b-nav>
    <b-nav-item @click="set_page_number(pagenumber)">
      <b-card
      no-body
      style="width: 15rem; height: 20rem;"
      header-bg-variant="transparent"
      class="shadow-sm"
      >
        <b-card-header><b-icon :icon="img" role="img" alt="icon" font-scale="4"></b-icon></b-card-header>
        <b-card-body :title="title">
          <b-card-text id="cardtext">
            {{description}}
          </b-card-text>
        </b-card-body>
      </b-card>
    </b-nav-item>
  </b-nav>
</template>

<script>
export default {
  name: 'reportnavcard',
  inject: [
    'set_page_number'
  ],
  props: {
    img: String,
    title: String,
    description: String,
    pagenumber: Number
  }
}
</script>
<style scoped>
#cardtext {
  text-align: left;
}
</style>