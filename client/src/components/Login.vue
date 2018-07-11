<template>
  <div class="page">
    <div class="login">
      <h1>登录</h1>
      <Input class="login-item" v-model="username" placeholder="帐号" />
      <Input class="login-item" v-model="password" placeholder="密码" />
      <div class="login-item">
        <Checkbox v-model="remember">记住我</Checkbox>
        <a class="login-item-register" href="/register.html">没有帐号？</a>
      </div>
      <Button class="login-item" type="primary" @click="login">登录</Button>
    </div>
    <Spin fix v-if="isLoading">
      <div class="loading">
        <svg width="135" height="135" viewBox="0 0 135 135" xmlns="http://www.w3.org/2000/svg" fill="#fff">
            <path d="M67.447 58c5.523 0 10-4.477 10-10s-4.477-10-10-10-10 4.477-10 10 4.477 10 10 10zm9.448 9.447c0 5.523 4.477 10 10 10 5.522 0 10-4.477 10-10s-4.478-10-10-10c-5.523 0-10 4.477-10 10zm-9.448 9.448c-5.523 0-10 4.477-10 10 0 5.522 4.477 10 10 10s10-4.478 10-10c0-5.523-4.477-10-10-10zM58 67.447c0-5.523-4.477-10-10-10s-10 4.477-10 10 4.477 10 10 10 10-4.477 10-10z">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 67 67"
                    to="-360 67 67"
                    dur="2.5s"
                    repeatCount="indefinite"/>
            </path>
            <path d="M28.19 40.31c6.627 0 12-5.374 12-12 0-6.628-5.373-12-12-12-6.628 0-12 5.372-12 12 0 6.626 5.372 12 12 12zm30.72-19.825c4.686 4.687 12.284 4.687 16.97 0 4.686-4.686 4.686-12.284 0-16.97-4.686-4.687-12.284-4.687-16.97 0-4.687 4.686-4.687 12.284 0 16.97zm35.74 7.705c0 6.627 5.37 12 12 12 6.626 0 12-5.373 12-12 0-6.628-5.374-12-12-12-6.63 0-12 5.372-12 12zm19.822 30.72c-4.686 4.686-4.686 12.284 0 16.97 4.687 4.686 12.285 4.686 16.97 0 4.687-4.686 4.687-12.284 0-16.97-4.685-4.687-12.283-4.687-16.97 0zm-7.704 35.74c-6.627 0-12 5.37-12 12 0 6.626 5.373 12 12 12s12-5.374 12-12c0-6.63-5.373-12-12-12zm-30.72 19.822c-4.686-4.686-12.284-4.686-16.97 0-4.686 4.687-4.686 12.285 0 16.97 4.686 4.687 12.284 4.687 16.97 0 4.687-4.685 4.687-12.283 0-16.97zm-35.74-7.704c0-6.627-5.372-12-12-12-6.626 0-12 5.373-12 12s5.374 12 12 12c6.628 0 12-5.373 12-12zm-19.823-30.72c4.687-4.686 4.687-12.284 0-16.97-4.686-4.686-12.284-4.686-16.97 0-4.687 4.686-4.687 12.284 0 16.97 4.686 4.687 12.284 4.687 16.97 0z">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 67 67"
                    to="360 67 67"
                    dur="8s"
                    repeatCount="indefinite"/>
            </path>
        </svg>
      </div>
    </Spin>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      username:"",
      password:"",
      remember:false,
      isLoading:false
    }
  },
  methods:{
    login(){
      this.isLoading = true
      let formData = new FormData()
      formData.append("username",this.username)
      formData.append("password",this.password)
      this.Axios.post("/api/user/login/",formData).then(response=>{
        this.isLoading = false
        if(response.data.isSuccess){
          this.$router.push("manager")
        } else {
          this.$Message.error({
            content:"登录失败，用户名或密码错误."
          })
        }
      })
    }
  }
}
</script>

<style>
html,body{
  height: 100%;
  width: 100%;
  overflow: hidden;
  margin: 0px;
  padding: 0px;
}
.page{
  background: url('https://cn.bing.com/az/hprichbg/rb/FremontPeak_ZH-CN8041302763_1920x1080.jpg');
  background-size: cover;
  width:100%;
  height:100%;
  margin: 0px;
  padding: 0px;
}
.login{
  width: 400px;
  height: 275px;
  display: flex;
  flex-direction: column;
  align-self: center;
  justify-content: center;
  background: #ffffff;
  border: 1px solid #d1dbe5;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04);
  padding: 20px 20px 20px 20px;
  position: fixed;
  top:0px;
  left: 0px;
  bottom:0px;
  right:0px;
  margin: auto;
  border-radius: 5px;
  text-align: center;
}

.login-item{
  margin: 10px 0px;
  text-align: left;
}

.login-item-register{
  float:right;
}

.loading{
  width: 135px;
  height: 135px;
}

.loading path{
  fill: #0099FF;
}
</style>