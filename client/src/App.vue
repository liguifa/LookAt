<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      username:"",
      password:"",
      remember:false
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
#app{
  width:100%;
  height:100%;
  margin: 0px;
  padding: 0px;
}
</style>