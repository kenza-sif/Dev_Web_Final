<template>
  <p for="name">Saisissez votre nom: </p>

  <input required v-model="username">
  <br>
  <br>
  <button type="button" @click="launchNewQuiz">GO!</button>


</template>
<script>

import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);

      this.$router.push('/questions/1');
    },
  }

}
</script>
  <style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
