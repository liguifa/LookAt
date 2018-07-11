import VueRouter from "vue-router"
import Login from "./components/Login.vue"
import Manager from "./components/Manager.vue"

const routes = [
	{ path: '/login', component: Login },
	{ path: '/manager', component: Manager}
]

const router = new VueRouter({
	routes
})

export default router