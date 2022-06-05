<script setup>
import { RouterLink, RouterView } from 'vue-router'
import image from  "../assets/homepage-img.png"
</script>


<template>
  <div id="body-home">
    <div id="homepage">
      <h2>Bienvenue à notre quiz !</h2>
      <br>
      <RouterLink class="RouterLink-home" to="/start-new-quiz-page">Démarrer le quiz !</RouterLink>
      <RouterLink class="RouterLink-home" to="/Score">Score</RouterLink>
      <div v-for="scoreEntry in registeredScores.slice(0,3)" v-bind:key="scoreEntry.score" class="tableau" >
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </div>
    </div>
    <div id="image">
      <img v-bind:src="image">
    </div>
  </div>
</template>


<style>
  .tableau{
    border : 0.1rem solid black;
    padding : 0.8rem 1rem 1rem 1rem  ;
    width : 50%;
    margin-top : 0.5rem;
    font-size : 1.5rem;
  }
  #homepage,#image{
    height: auto;
    width: auto;
    margin: auto;
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
    font: normal 100% Helvetica, Arial, sans-serif;
    display: flex;
    line-height: 2rem;
  }
  .RouterLink-home{
    margin: 0rem 0rem 1rem 0rem;
    font-size : 1.8rem;
  }
</style>


<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    const test = await quizApiService.getQuizInfo();
    this.registeredScores = test.data.scores;
    console.log(this.registeredScores);
  }
};
</script>


