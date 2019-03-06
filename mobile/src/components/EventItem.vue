<template>
    <Row>
        <Col span=18>
            <Row>
                <Col span=4 >{{item.hours}}h</Col>
                <Col span=20>{{item.project}}</Col>
            </Row>
            <Row>
                {{item.desc}}
            </Row>
        </Col>
        <Col span=3>
            <Button type="primary" @click="onItemEdit()">Edit</Button>
        </Col>
        <Col span=3>
            <Button type="error" @click="onItemDelete()">Delete</Button>
        </Col>
    </Row>
</template>
<script>
export default {
    props: ['item'],

    methods: {
        onItemEdit() {
            this.$emit("onItemEdit", this.item.id)
        },

        onItemDelete() {
            this.$emit("onItemDelete", this.item.id)
        },

    }

}
</script>
