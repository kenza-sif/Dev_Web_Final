<script setup>
import { RouterLink, RouterView } from 'vue-router'
import podium from  "../assets/podium.jpg"
</script>


<template>
  <div id="scorebody">
    <div id="scorepage">
      <h3>Bravo {{username}} !</h3>
      <h3>Vous avez gagné {{score}} points !</h3>
      <h3>Votre dernier classement était : N° {{rank}}</h3>
      <br> 
      <h3>Le Classement :</h3>
      <div v-for="scoreEntry in registeredScores.slice(0,10)" v-bind:key="scoreEntry.score" class="classement" >
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </div>
    </div>
    <div id="podium">
      <img v-bind:src="podium">
      <br><br><br><br><br>
      <RouterLink class="RouterLink_score" to="/" tag="button">return</RouterLink>
    </div>
  </div>
</template>


<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "scorepage",
  data() {
    return {
      registeredScores: [],
      username : participationStorageService.getPlayerName(),
      score : participationStorageService.getParticipationScore(),
      rank : participationStorageService.getParticipationRank(),
    };
  },
  async created() {
    const test = await quizApiService.getQuizInfo();
    this.registeredScores = test.data.scores
    console.log(this.registeredScores);
  }
};
</script>


<style>
  #scorepage{
    height: 100%;
    width: 100%;
    margin: auto;
    place-items: center;
  }
  .classement{
    border : 0.1rem solid black;
    padding : 0.5rem 0.5rem 0.5rem 0.5rem ;
    width : 50%;
    margin-top : 0.5rem;
    font-size : 1.5rem;
  }
  #podium{
    height: 100%;
    width: 100%;
    margin: 2rem -2rem 0rem 10rem;
  }
  #scorepage {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    display: flex;
    flex-direction: column;
    place-items: center;
  }
  #scorebody{
    font: normal 100% Helvetica, Arial, sans-serif;
    display: flex;
    line-height: 2rem;
    margin: 6rem 1rem 0rem 5rem ;
    place-items: center;
  }
  .RouterLink_score{
    margin: 1rem 1rem 1rem 1rem ;
    font-size : 2.5rem;
  }
</style>
