webpackHotUpdate(0,{9:function(t,e,i){"use strict";var s={data:()=>({topmenus:[],activeMenuId:0}),asyncComputed:{async sideMenus(){if(0!=this.activeMenuId){return(await this.Axios.get(`/api/common/side_menus/${this.activeMenuId}`)).data}}},mounted(){this.Axios.get("/api/common/top_menus").then(t=>{this.topmenus=t.data,this.activeMenuId=this.topmenus[0].id})}};e.a=s}});