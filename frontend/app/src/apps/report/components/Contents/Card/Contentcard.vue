<template>
  <div>
    <CardforEdit
      :object="content"
      :title="title"
      :icon="icon"
      :description="description"
      :subtitle="subtitle"
      :editfunc="editfunc"
      :overlayOKfunc="overlayOKfunc"
    />
  </div>
</template>
<script>
import CardforEdit from '@/apps/report/components/objects/CardforEdit'
export default {
  name: 'contentcard',
  components: {
    CardforEdit
  },
  props: {
    content: Object,
    title: String,
    icon: String,
    description: String,
    subtitle: String,
    overlayOKfunc: Function,
    contentgetter: Function,
    contentsetter: Function,
    savefunc: Function,
    selectedcontentsetter: Function
  },
  methods: {
    editfunc () {
      this.selectedcontentsetter(this.content)
      this.$router.push({name: 'createcontentsviewer', params: {contentgetter: this.contentgetter, contentsetter: this.contentsetter, savefunc: this.savefunc, itemclickactivate: false}})
    }
  }
}
</script>