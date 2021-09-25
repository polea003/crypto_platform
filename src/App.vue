<template>
  <div id="app" class="w-full h-screen">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/Blog">About</router-link>
    </div>
    <router-view/>
    <div class="absolute bottom-0 w-full">
      <button class="bg-blue-500 hover:bg-blue-700 text-white w-24 h-24 font-bold py-2 px-4 rounded">
  Button
</button>
    <div id="footer">
      <div>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      </div>
    </div>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #df9816;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #ce871e;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
