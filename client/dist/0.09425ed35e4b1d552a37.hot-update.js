webpackHotUpdate(0,{9:function(t,e,s){"use strict";var a={data:()=>({topmenus:[],activeMenuId:0}),asyncComputed:{async sideMenus(){return(await this.Axios.get(`/api/common/side_menus/${this.activeMenuId}`)).data}},mounted(){this.Axios.get("/api/common/top_menus").then(t=>{this.topmenus=t.data,this.activeMenuId=this.topmenus[0].id})}};e.a=a}});