<template>
	<div class="manager-page">
		<div class="manager-page-header">
			<Menu mode="horizontal" :theme="'dark'" active-name="1">
				<MenuItem v-for="menu in topmenus" :name="menu.display_name" :key="menu.id">
					<Icon type="ios-paper"></Icon>
					{{menu.display_name}}
				</MenuItem>
			</Menu>
		</div>
		<div class="manager-page-body">
			<Menu :theme="'dark'">
                <Submenu v-for="menu in sideMenus" :key="menu.id" :name="menu.display_name">
                    <template slot="title">
                        <Icon type="ios-paper"></Icon>
                        {{menu.display_name}}
                    </template>
                    <MenuItem v-for="sub in menu.sub_menus" :key="sub.id" :name="sub.display_name">{{sub.display_name}}</MenuItem>
                </Submenu>
            </Menu>
			<div class="manager-content">
				<lookat-images></lookat-images>
			</div>
		</div>
	</div>
</template>

<script>
import Images from "./Images.vue"

export default {
	data(){
		return {
			topmenus:[],
			activeMenuId:0
		}
	},
	asyncComputed:{
		async sideMenus(){
			if(this.activeMenuId != 0){
				let response = await this.Axios.get(`/api/common/side_menus/${this.activeMenuId}`);
				return response.data
			}
		}
	},
	mounted(){
		this.Axios.get("/api/common/top_menus").then(response=>{
			this.topmenus = response.data
			this.activeMenuId = this.topmenus[0].id
		})
	},
	components:{
		"lookat-images" : Images
	}
}
</script>


<style>
.manager-page{
	margin: 0px;
	padding: 0px;
	width:100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	overflow: hidden;
}

.manager-page-header{
	width: 100%;
	flex-grow: 0;
	height: 60px;
}

.manager-page-body{
	flex-grow: 1;
	flex-shrink: 1;
	height: calc(100% - 60px);
	display: flex;
}

.manager-page-body > ul{
	height: 100%;
	flex-shrink: 0;
}

.manager-content{
	flex-grow: 1;
	padding: 10px;
	flex-shrink: 1;
	width:100px;
}
</style>