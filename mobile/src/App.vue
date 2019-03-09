<template>
  <div id="app">
    <!-- <router-view/> -->
    <div v-if="showCon" class="login">
      <Form ref="formCustom" :model="formCustom" :rules="ruleValidate" :label-width="80">
        <FormItem label="username" prop="username">
            <Input type="text" v-model="formCustom.username"/>
        </FormItem>
        <FormItem label="passwd" prop="passwd">
            <Input type="password" v-model="formCustom.passwd"/>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formCustom')">Submit</Button>
            <Button @click="handleReset('formCustom')" style="margin-left: 8px">Reset</Button>
        </FormItem>
      </Form>
    </div>
    <div v-else>
      <Row type="flex" class="timelog-header" justify="space-around">
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
        <event-item  v-for="v in events" :item=v  @onItemEdit="onEdit" @onItemDelete="onDelete"/>
      </Row>

      <Row class="timelog-new">
        <Button type="success" size="large" long @click="onNew()">New...</Button>
      </Row>

      <Modal
          v-model="showEditModal"
          title="Edit"
          @on-ok="onSubmit(item)"
          @on-cancel="onCancel()">

            <Select class="mb-10" v-model="item.project" filterable :placeholder="item.project">
                <Option v-for="v in projListMock" :value="v">{{ v }}</Option>
            </Select>
            <InputNumber class="mb-10" v-model="item.hours" size="large"></InputNumber>
            <Input v-model="item.desc" type="textarea" placeholder="Enter something..." />
      </Modal>
    </div>
    
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
      formCustom: {
        passwd: '',
        username: '',
        age: ''
      },
      ruleValidate: {
        username: [
            { required: true, message: 'The username cannot be empty', trigger: 'blur' }
        ],
        passwd: [
            { required: true, message: 'The password cannot be empty', trigger: 'blur' }
        ]
      },
      showCon: false,
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
  created(){
    if(!localStorage.getItem("token")){
      this.showCon = true;
      return;
    }
    this.showCon = false;
  },
  methods: {
    handleSubmit (name) {
      console.log(name)
        this.$refs[name].validate((valid) => {
            if (valid) {
                this.$Message.success('Success!');
                this.showCon = false;
            } else {
                // this.$Message.error('Fail!');
                this.showCon = true;
            }
        })
    },
    handleReset (name) {
        this.$refs[name].resetFields();
    },
    onDelete(idx) {
      let index = this.events.findIndex((e)=>{
        return e.id == idx;
      })
      this.events.splice(index,1);
      this.item = this.events;
    },
    onClose(item){
      alert(item)
    },

    onEdit(idx){
      // this.item = this.events[idx]
      console.log(this.events,">...");
      let index = this.events.findIndex((e)=>{
        return e.id == idx;
      })
      this.item = this.events[index];
      this.showEditModal = true
    },

    onNew() {
      this.newEvent = {
        id: "xxy",
        project: "pro",
        desc: "content",
        hours: parseInt(Math.random()+1),

      }
      // this.showEditModal = true;
      this.item = this.newEvent;
      // this.onEdit(this.newEvent.id)
      this.events.push(this.item)
      // this.events.push(event)
    },

    onCancel(){
      console.log("on cancel")
      this.showEditModal = false
    },
    onSubmit(item){
      this.item = item;
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
.login {
  width:80%; 
  margin:100px auto 0;
}

.timelog-header{
  margin: 10px;
}
.timelog-header button {
  padding-left:0px!important;
  padding-right:0px!important;
}
.timelog-header-btn {
  box-sizing: border-box!important;
  padding:0 3px 0 0;
}

textarea{
  resize: none!important;
}
.mb-10 {
  margin-bottom: 10px !important;
  display: block!important;
  width: 100%!important;

}
.timelog-header-btn{
  
  /* padding-left: 5px; */
  /* padding-right: 5px; */

}

.timelog-item{
  margin: 10px;
  /* padding: 5px; */

}

.timelog-new{
  margin: 10px;
  padding: 5px;

}
</style>
