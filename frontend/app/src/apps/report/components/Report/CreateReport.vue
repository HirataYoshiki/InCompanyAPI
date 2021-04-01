<template>
  <div>
    <b-img :src="img" fluid alt="Responsive image"></b-img>
    <b-container fluid>
      <b-row>
        <b-col>
          <ContentPool :getter="get_contents" :setter="return_true" :group="group"/>
        </b-col>
        <b-col>
          <b-icon icon="layers" font-scale="4"></b-icon>
          <b-form-group
            label="Build up report!"
            label-for="content_order"
          >
            <b-list-group id="content_order">
              <draggable v-model="order" :group="group" draggable=".item">
                <b-list-group-item
                  id="contentorder"
                  v-for="(content, i) in order" :key="i"
                >
                  <strong>{{i+1}}.</strong>
                  <b-icon icon="box"></b-icon>
                  {{content.content.substr( 0, 21)}}
                </b-list-group-item>
              </draggable>
              <b-list-group-item slot="footer" variant="light" id="contentorderfooter">Drag and Drop Content</b-list-group-item>
            </b-list-group>
          </b-form-group>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ContentPool from '@/apps/report/components/objects/ContentPool'
import draggable from 'vuedraggable'
export default {
  name: 'createreport',
  components: {
    ContentPool,
    draggable
  },
  inject: [
    'get_contents'
  ],
  data () {
    return {
      img: require('@/assets/buildreportheader.png'),
      group: 'createreport',
      order: []
    }
  },
  methods: {
    return_true () {
      return true
    }
  }
}
</script>
<style scoped>
#contentorder {
  text-align: left;
}
</style>