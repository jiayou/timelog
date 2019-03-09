<template>
    <Row class="eventBtn" type="flex" justify="space-around">
        <Col span=16>
            <Row>
                <Col span=4 >{{item.hours}}h</Col>
                <Col span=20>{{item.project}}</Col>
            </Row>
            <Row>
                {{item.desc}}
            </Row>
        </Col>
        <Col span=3>
            <Button type="primary"  @click="onItemEdit()">Edit</Button>
        </Col>
        <Col span=3>
            <Button type="error" @click="onItemDelete()">Delete</Button>
        </Col>
    </Row>
</template>
<script>
export default {
    props: ['item','showEditModel'],

    methods: {
        onItemEdit() {
            console.log(this.item,"...")
            this.$emit("onItemEdit", this.item.id)
        },

        onItemDelete() {
            this.$emit("onItemDelete", this.item.id)
        },

    }

}
</script>
<style>
.eventBtn button {
    width: 100%;
    padding-left: 0px!important;
    padding-right: 0px!important;
}
</style>
