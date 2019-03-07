<template>
    <Tabs value="name1" type="card">
        <TabPane label="标签一" name="name1">
          <v-chart :options="test"/>
        </TabPane>
        <TabPane label="标签二" name="name2">标签二的内容</TabPane>
        <TabPane label="标签三" name="name3">标签三的内容</TabPane>
    </Tabs>
</template>

<script>
import 'echarts/lib/chart/heatmap'
import 'echarts/lib/component/calendar'

export default {
  data() {
    return {
      dataMock: [ // event list
        {id: "", proj: "proj1", desc:"some work", hours: 4, date:'2019-3-1', user: "Mike" },
      ],

      stat1Mock: [
        {user: "Alice", hours: 8, date: '2019-3-1'},
        {user: "Alice", hours: 8, date: '2019-3-2'},
        {user: "Alice", hours: 8, date: '2019-3-3'},
        {user: "Alice", hours: 8, date: '2019-3-4'},
        {user: "Alice", hours: 8, date: '2019-3-5'},
      ],

      test:  {
          tooltip: {
              position: 'top'
          },

          visualMap: [{
              min: 0,
              max: 1000,
              calculable: true,
              seriesIndex: [2, 3, 4],
              orient: 'horizontal',
              left: '55%',
              bottom: 20
          }, {
              min: 0,
              max: 1000,
              inRange: {
                  color: ['grey'],
                  opacity: [0, 0.3]
              },
              controller: {
                  inRange: {
                      opacity: [0.3, 0.6]
                  },
                  outOfRange: {
                      color: '#ccc'
                  }
              },
              calculable: true,
              // seriesIndex: [1],
              orient: 'horizontal',
              left: '10%',
              bottom: 20
          }],

          calendar: [
          {
              orient: 'vertical',
              yearLabel: {
                  margin: 40
              },
              dayLabel: {
                  firstDay: 1,
                  nameMap: ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
              },
              monthLabel: {
                  nameMap: 'cn',
                  margin: 20
              },
              cellSize: 40,
              top: 0,
              left: 0,
              range: '2019-03'
          }],

          series: [{
              type: 'heatmap',
              coordinateSystem: 'calendar',
              calendarIndex: 0,
              data: [
                ["2019-03-01", 8],
                ["2019-03-03", 8],
              ]
          }]
      }      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
