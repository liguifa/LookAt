<template>
	<div class="images-page">
		<Table  border :columns="columns" :data="data"></Table>
	</div>
</template>

<script>
export default {
	data () {
        return {
            columns: [
                {
                    title: '序号',
                    key: 'id',
                    width: 100,
                    fixed: 'left'
                },
                {
                    title: '名称',
                    key: 'name',
                    width: 400
                },
                {
                    title: '缩略图',
                    key: 'thumbnail',
                    width: 200
                },
                {
                    title: '路径',
                    key: 'path',
                    width: 200
                },
                {
                    title: '上传时间',
                    key: 'upload_time',
                    width: 200
                },
                {
                    title: '上传者',
                    key: 'upload_user',
                    width: 100
                },
                {
                    title: 'Action',
                    key: 'action',
                    fixed: 'right',
                    width: 120,
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'text',
                                    size: 'small'
                                }
                            }, 'View'),
                            h('Button', {
                                props: {
                                    type: 'text',
                                    size: 'small'
                                }
                            }, 'Edit')
                        ]);
                    }
				}],
			data:[]
		}
	},
	mounted() {
		this.Axios.get("/api/images/").then(response=>{
			this.data = response.data
		})
	},
}
</script>