<template>
  <div id="app" class="w-full h-screen bg-gray-800 overflow-auto">
    <div id="nav" class="flex justify-start bg-gray-700 items-center hidden md:flex">
      <div class="flex-grow ml-2 font-bold text-xl">CoinRoutes</div>
      <router-link to="/portfolio" class="mx-2">Portfolio</router-link> |
      <router-link to="/explore" class="mx-2">Explore</router-link> |
      <router-link to="/strategy" class="mx-2">Strategy</router-link> 
    </div>
    <router-view />
    <div class="absolute bottom-0 w-full sm:invisible">
    <div id="footer" class="md:invisible">
      <div id="nav" class="w-full flex flex-grow justify-center bg-gray-700 p-2">
      <router-link to="/portfolio" class="mx-4">Portfolio</router-link> |
      <router-link to="/explore" class="mx-4">Explore</router-link> |
      <router-link to="/strategy" class="mx-4">Strategy</router-link>
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
  /* text-align: center; */
  /* color: #df9816; */
  color: #bacad4;
}


#nav a {
  font-weight: bold;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
