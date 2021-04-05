<template>
  <b-card class="shadow-sm" style="width: 20rem; height: 20rem">
    <b-card-title>{{title}}</b-card-title>
    <b-card-text>
      <h4><b-icon :icon="icon"></b-icon></h4>
    </b-card-text>
    <b-card-text>
      {{description.substr(0, 120)}}
    </b-card-text>
    <b-card-text class="small text-muted">{{subtitle}}</b-card-text>
    <template #footer>
      <b-nav fill>
        <b-nav-item @click="show_overlay">
          <b-icon icon="trash-fill" class="ml-auto" variant="danger" v-b-popover.hover.top="'Delete'"></b-icon>
        </b-nav-item>
        <b-nav-item @click="editfunc">
          <b-icon icon="pencil-square" v-b-popover.hover.top="'Edit'">Edit</b-icon>
        </b-nav-item>
      </b-nav>
    </template>
    <b-overlay :show="overlay" no-wrap>
      <template #overlay>
        <div
            ref="dialog"
            tabindex="-1"
            role="dialog"
            aria-modal="false"
            aria-labelledby="form-confirm-label"
            class="text-center p-3"
          >
            <h3><strong id="form-confirm-label">Delete?</strong></h3>
            <div class="d-flex">
              <b-button variant="outline-danger" class="mr-3" @click="Cancel">
                Cancel
              </b-button>
              <b-button variant="outline-success" @click="OK">OK</b-button>
            </div>
          </div>
        </template>
      </b-overlay>
  </b-card>
</template>

<script>
export default {
  name: 'cardforedit',
  props: {
    object: Object,
    title: String,
    icon: String,
    description: String,
    subtitle: String,
    editfunc: Function,
    overlayOKfunc: Function
  },
  data () {
    return {
      overlay: false
    }
  },
  methods: {
    show_overlay () {
      this.overlay = true
    },
    Cancel () {
      this.overlay = false
    },
    OK () {
      this.overlayOKfunc(this.object)
      this.overlay = false
    }
  }
}
</script>