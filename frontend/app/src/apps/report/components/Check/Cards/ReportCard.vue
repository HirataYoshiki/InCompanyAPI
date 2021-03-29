<template>
  <div>
    <b-card
      border-variant="primary"
      v-bind:header="headertime"
      header-bg-variant="primary"
      header-text-variant="white"
      header-border-variant="primary"
      align="center"
      class="mb-2"
      v-bind:title="report.title">
        <b-card-text>Some descriptions.</b-card-text>
        <b-button @click="go_to_detail" variant="primary">Edit</b-button>
        <template #footer>
          <b-nav vertical>
            <b-nav-item @click="show_overlay">
              <b-icon icon="trash-fill" class="ml-auto" variant="danger"></b-icon>
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
    </div>
</template>

<script>
export default {
  name: 'reportcard',
  props: {
    report: Object
  },
  inject: [
    'create_headers',
    'get_groups',
    'get_contents',
    'delete_from_reports',
    'set_orderedcontents'
  ],
  data () {
    return {
      overlay: false
    }
  },
  methods: {
    go_to_detail () {
      this._orderedcontents()
      this.$router.push({path: 'detail'})
    },
    show_overlay () {
      this.overlay = true
    },
    Cancel () {
      this.overlay = false
    },
    async OK () {
      let url = 'http://localhost:8080/reportapp/reports/' + String(this.report.localreportid)
      const headers = this.create_headers()
      await this.$axios.delete(url, headers)
      this.overlay = false
      this.delete_from_reports(this.report)
    },
    _orderedcontents () {
      let groups = this.get_groups().filter(n => n.localgroupid === this.report.contentgroupid)
      groups.sort(function (a, b) {
        return a.order - b.order
      })
      const contents = this.get_contents()
      let orderedcontents = []
      groups.forEach(function (item) {
        let push = contents.concat()
        push.filter(n => n.contentid === item.contentid)
        orderedcontents.push(push[0])
      })
      this.set_orderedcontents(orderedcontents)
    }
  },
  computed: {
    headertime () {
      return 'Created at ' + this.report.timestamp
    }
  },
  watch: {
    report: function () {
      this.report = this.report
    }
  }
}
</script>