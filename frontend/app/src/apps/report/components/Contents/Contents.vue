<template>
  <div>
    <div>
      <b-img :src="img" fluid alt="Responsive image"></b-img>
    </div>
    <b-card-group>
      <div v-for="(content, i) in contents" :key="content.contentid">
        <CardforEdit
          :object="content"
          :title="'Content '+i"
          :icon="'box'"
          :description="content.content"
          :subtitle="''"
          :editfunc="test"
          :overlayOKfunc="test"
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
    'delete_from_contents'
  ],
  data () {
    return {
      img: require('@/assets/contentsheader.png')
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
    }
  } 
}
</script>