<template>
  <div>
    <b-img :src="img" fluid alt="Responsive image"></b-img>
    <b-navbar>
      <b-navbar-nav class="ml-auto">
        <b-button variant="success" @click="save">Save</b-button>
      </b-navbar-nav>
    </b-navbar>
    <b-container fluid>
      <b-row>
        <b-col>
          <div id="mde">
            <vue-simplemde v-model="text" :configs="mdeconf"/>
          </div>
        </b-col>
        <b-col v-if="itemclickactivate">
          <ContentPool
            :getter="get_contents"
            :setter="return_true"
            :itemclickevent="itemclickevent"/>
        </b-col>
      </b-row>
    </b-container>
    
  </div>
</template>

<script>
import VueSimplemde from 'vue-simplemde'
import ContentPool from '@/apps/report/components/objects/ContentPool'
export default {
  name: 'contenteditor',
  components: {
    VueSimplemde,
    ContentPool
  },
  props: {
    contentgetter: Function,
    contentsetter: Function,
    savefunc: Function,
    itemclickactivate: {
      type: Boolean,
      default: true
    }
  },
  inject: [
    'get_contents'
  ],
  data () {
    return {
      img: require('@/assets/report/contentheader.png'),
      mdeconf: {
        placeholder: 'Input Content here',
        spellChecker: false
      }
    }
  },
  computed: {
    text: {
      get () {
        return this.contentgetter()
      },
      set (value) {
        if (value > 600) {
          alert('the content is too large')
        } else {
          this.contentsetter(value)
        }
      }
    }
  },
  methods: {
    save () {
      try {
        this.savefunc()
        alert('save')
      } catch (e) {
        alert('Error')
      }
    },
    return_true () {
      return true
    },
    itemclickevent (content) {
      this.text = content.content
    }
  }
}
</script>
<style scoped>
#mde {
  text-align: left;
}
</style>