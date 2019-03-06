<template>
  <div id="app">

    <Row class="timelog-header">
      <Col span=4 class="timelog-header-btn" >
        <Button size="large" long type="info"  @click="onPrevDay()"> Prev </Button>
      </Col>
      <Col span=12 class="timelog-header-btn" >
        <Button  size="large" long> {{date}} </Button>
      </Col>
      <Col span=4 class="timelog-header-btn" >
        <Button size="large" long type="primary" @click="onToday()"> Today </Button>
      </Col>
      <Col span=4 class="timelog-header-btn" >
        <Button  size="large" long type="info"  @click="onNextDay()"> Next </Button>
      </Col>
    </Row>

    <Row class="timelog-item" >
      <event-item v-for="v in events" :item=v />
    </Row>

    <Row class="timelog-new">
      <Button type="success" size="large" long @click="onNew()">New...</Button>
    </Row>

    <Modal
        v-model="showEditModal"
        title="Edit"
        @on-ok="onSubmit()"
        @on-cancel="onCancel()">

          <Select v-model="item.proj" filterable>
              <Option v-for="v in projListMock" :value="v">{{ v }}</Option>
          </Select>
          <InputNumber v-model="item.hours" size="large"></InputNumber>
          <Input v-model="item.desc" type="textarea" placeholder="Enter something..." />
    </Modal>
  </div>
</template>

<script>
import moment from "moment"
import EditModal from "./components/EditModal.vue"
import EventItem from "./components/EventItem.vue"

export default {
  name: 'app',
  components: {
    // HelloWorld
  },
  data() {
    return {
      date: '',
      offset: 0,
      showEditModal: false,
      events: [
          {
            id: "xx1",
            project: "proj1",
            desc: "some work",
            hours: 2,
          },
          {
            id: "xx2",
            project: "proj2",
            desc: "some work",
            hours: 2,
          },
      ],

      item: {},

      projListMock: [
        "111",
        "111a",
        "1112",
        "111d",
        "111v",
        "111r",
      ],
    }
  },
components: {
  EditModal,
  EventItem,
},
  mounted() {
    this.onToday()
  },

  methods: {
    onClose(item){
      alert(item)
    },

    onEdit(idx){
      console.log("onEdit")
      this.item = this.events[idx]
      this.showEditModal = true
    },

    onNew() {
      this.newEvent = {
        id: "xxy",
        project: "",
        desc: "",
        hours: Math.random(),

      }
      this.onEdit()
      this.events.push(event)
    },

    onCancel(){
      console.log("on cancel")
      this.showEditModal = false
    },
    onSubmit(){
      alert(2)
      console.log("on submit")
      this.showEditModal = false
    },

    onNextDay(){
      this.offset = this.offset + 1
      var moment = require('moment');
      this.date = moment().add(this.offset, 'days').format("YYYY-MM-DD dddd")

    },

    onPrevDay(){
      this.offset = this.offset - 1
      var moment = require('moment');
      this.date = moment().add(this.offset, 'days').format("YYYY-MM-DD dddd")
    },

    onToday(){
      // this.day = Date.now()
      var moment = require('moment');
      this.date = moment().format("YYYY-MM-DD dddd")
    }


  }
}
</script>

<style>
.timelog-header{
  margin: 10px;
  padding: 5px;
}

.timelog-header-btn{
  padding-left: 5px;
  padding-right: 5px;

}

.timelog-item{
  margin: 10px;
  padding: 5px;

}

.timelog-new{
  margin: 10px;
  padding: 5px;

}
</style>
