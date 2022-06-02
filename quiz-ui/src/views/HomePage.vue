<script setup>
import { RouterLink, RouterView } from 'vue-router'
import image from  "../assets/hero-img.png"
</script>


<template>
  <div id="body-home">
  <div id="homepage">
  <h1>Bienvenue à notre quiz !</h1>
  
  <RouterLink class="RouterLink" to="/start-new-quiz-page">Démarrer le quiz !</RouterLink>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date" class="tableau">
  {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  </div>
  <div id="image">
  <img
  v-bind:src="image"
  class="lazy" alt="">
  </div>
  </div>

</template>

<style>
  .tableau{
    border : 1px solid black;
    padding : 20px 20px 20px 20px;
    width : 50%;
    margin-top : 10px;
    font-size : 25px;
  }
  #homepage, #image{
    height: 100%;
    width: 50%;
    margin: 0;
  }
  #homepage {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    display: flex;
    flex-direction: column;
    place-items: center;
  }
  #body-home{
    display: flex;
    line-height: 32px;
  }
  .RouterLink{
    margin: 50px 0px 5Opx 0px;
  }
</style>



<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [{playerName:"Alma",score:"6"},{playerName:"Jean",score:"8"},{playerName:"Paul",score:"2"}]
    };
  },
  async created() {
    const test = await quizApiService.getQuizInfo();
    //this.registeredScores = test.data.scores
    console.log(this.registeredScores);
  }
};
</script>


