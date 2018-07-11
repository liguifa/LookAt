<template>
	<div class="manager-page">
		<div class="manager-page-header">
			<Menu mode="horizontal" :theme="'dark'" active-name="1">
				<MenuItem name="1">
					<Icon type="ios-paper"></Icon>
					内容管理
				</MenuItem>
				<MenuItem name="2">
					<Icon type="ios-people"></Icon>
					用户管理
				</MenuItem>
				<Submenu name="3">
					<template slot="title">
						<Icon type="stats-bars"></Icon>
						统计分析
					</template>
					<MenuGroup title="使用">
						<MenuItem name="3-1">新增和启动</MenuItem>
						<MenuItem name="3-2">活跃分析</MenuItem>
						<MenuItem name="3-3">时段分析</MenuItem>
					</MenuGroup>
					<MenuGroup title="xx">
						<MenuItem name="3-4">xxxxx</MenuItem>
						<MenuItem name="3-5">xxxxxx</MenuItem>
					</MenuGroup>
				</Submenu>
				<MenuItem name="4">
					<Icon type="settings"></Icon>
					综合设置
				</MenuItem>
			</Menu>
		</div>
		<div class="manager-page-body">
			<Menu :theme="'dark'">
                <Submenu name="1">
                    <template slot="title">
                        <Icon type="ios-paper"></Icon>
                        内容管理
                    </template>
                    <MenuItem name="1-1">文章管理</MenuItem>
                    <MenuItem name="1-2">评论管理</MenuItem>
                    <MenuItem name="1-3">举报管理</MenuItem>
                </Submenu>
                <Submenu name="2">
                    <template slot="title">
                        <Icon type="ios-people"></Icon>
                        用户管理
                    </template>
                    <MenuItem name="2-1">新增用户</MenuItem>
                    <MenuItem name="2-2">活跃用户</MenuItem>
                </Submenu>
                <Submenu name="3">
                    <template slot="title">
                        <Icon type="stats-bars"></Icon>
                        统计分析
                    </template>
                    <MenuGroup title="使用">
                        <MenuItem name="3-1">新增和启动</MenuItem>
                        <MenuItem name="3-2">活跃分析</MenuItem>
                        <MenuItem name="3-3">时段分析</MenuItem>
                    </MenuGroup>
                    <MenuGroup title="留存">
                        <MenuItem name="3-4">用户留存</MenuItem>
                        <MenuItem name="3-5">流失用户</MenuItem>
                    </MenuGroup>
                </Submenu>
            </Menu>
		</div>
	</div>
</template>

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
}

.manager-page-body > ul{
	height: 100%;
}
</style>