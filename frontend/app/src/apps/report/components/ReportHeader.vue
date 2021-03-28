<template>
  <b-navbar type="light" variant="light">
    <b-collapse id="nav-text-collapse" is-nav>
      <b-navbar-nav>
        <b-navbar-brand @click="set_page_number(0)">
          <b-icon icon="arrow-left-square" variant="dark"></b-icon>
        </b-navbar-brand>
        <b-nav-text>Report</b-nav-text>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'reportheader',
  inject: [
    'set_page_number'
  ]
}
</script>