import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import ECharts from 'vue-echarts'
// import Routers from './router.js';
import iView from 'iview';
import 'iview/dist/styles/iview.css';

Vue.component('v-chart', ECharts);
Vue.use(VueRouter);
Vue.use(iView);
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
