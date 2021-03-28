<template>
  <b-nav>
    <b-nav-item :to="url">
      <b-card
      no-body
      style="width: 15rem; height: 15rem;"
      header-bg-variant="transparent"
      class="shadow-sm"
      >
        <b-card-header><b-icon :icon="icon" role="img" alt="icon" font-scale="4"></b-icon></b-card-header>
        <b-card-body :title="name">
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
  name: 'homenavcard',
  props: {
    icon: String,
    name: String,
    description: String,
    url: String
  }
}
</script>
<style scoped>
#cardtext {
  text-align: left;
}
</style>