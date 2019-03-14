<template>
    <Card>
        <Row>
            <Col class="search-bar-button" span=3>
                <Button type="dashed" long > Prev</Button>
            </Col>
            <Col class="search-bar-button" span=6>
                <Button type="primary" long >Today</Button>
            </Col>
            <Col class="search-bar-button" span=3>
                <Button type="dashed" long > Next </Button>
            </Col>
            <Col class="search-bar-button" span=5>
                <Select v-model="project">
                    <Option value="beijing">New York</Option>
                    <Option value="shanghai" disabled>London</Option>
                    <Option value="shenzhen">Sydney</Option>
                </Select>
            </Col>
            <Col class="search-bar-button" span=5>
                <Select v-model="user">
                    <Option value="beijing">New York</Option>
                    <Option value="shanghai" disabled>London</Option>
                    <Option value="shenzhen">Sydney</Option>
                </Select>
            </Col>

        </Row>
    </Card>

</template>
<script>
export default {
    data(){
        return {
            project: "",
            user: "",
        }
    }
}
</script>
<style>
.search-bar-button{
    padding-left: 10px;
    padding-right: 10px;
}
</style>
