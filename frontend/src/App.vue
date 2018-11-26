<template>
  <div id="app">
    <div id="nav">
      <router-link to="/new-risk-model">Create your risk model</router-link> |
      <router-link to="/risks-list">Risk models list</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #061f2b;
    &.router-link-exact-active {
      color: #00a6d8;
    }
  }
}
</style>
