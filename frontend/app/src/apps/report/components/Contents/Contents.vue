<template>
  <div>
    <div>
      <b-img :src="img" fluid alt="Responsive image"></b-img>
    </div>
    <b-card-group deck class="mt-2">
      <div v-for="(content, i) in contents" :key="content.contentid">
        <CardforEdit
          :object="content"
          :title="'Content '+i"
          :icon="'box'"
          :description="content.content"
          :subtitle="''"
          :editfunc="test"
          :overlayOKfunc="overlaydeleteok"
        />
      </div>
    </b-card-group>
  </div>
</template>

<script>
import CardforEdit from '@/apps/report/components/objects/CardForEdit'
export default {
  name: 'contents',
  components: {
    CardforEdit
  },
  inject: [
    'get_contents',
    'create_headers',
    'delete_from_contents'
  ],
  data () {
    return {
      img: require('@/assets/report/contentsheader.png')
    }
  },
  computed: {
    contents () {
      return this.get_contents()
    }
  },
  methods: {
    test () {
      alert('test')
    },
    async overlaydeleteok (content) {
      try {
        const headers = this.create_headers()
        const url = 'http://localhost:8080/reportapp/contents/' + String(content.localcontentid)
        await this.$axios.delete(url, headers)
        this.delete_from_contents(content)
      } catch (e) {
        alert('the content is used in some report. cant delete this.')
      }
    }
  } 
}
</script>