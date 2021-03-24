<template>
  <b-overlay :show="status" no-wrap>
    <template #overlay>
      <div
          ref="dialog"
          tabindex="-1"
          role="dialog"
          aria-modal="false"
          aria-labelledby="form-confirm-label"
          class="text-center p-3"
        >
          <p><strong id="form-confirm-label">Are you sure?</strong></p>
          <div class="d-flex">
            <b-button variant="outline-danger" class="mr-3" @click="Cancel">
              Cancel
            </b-button>
            <b-button variant="outline-success" @click="OK">OK</b-button>
          </div>
        </div>
    </template>
  </b-overlay>
</template>

<script>
export default {
  name: 'confirmoverlay',
  data () {
    return {
      status: true
    }
  },
  props: {
    items: Object,
    onOK: Function | Promise,
    number: Number
  },
  methods: {
    OK () {
      this.status = false
      this.onOK(this.number)
    },
    Cancel () {
      this.status = false
    }
  }
}
</script>