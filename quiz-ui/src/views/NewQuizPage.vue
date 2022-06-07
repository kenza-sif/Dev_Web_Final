<template>
  <div id="startquizpage">
    <p for="name" class="saisir_nom">Saisissez votre nom: </p>
    <input required v-model="username" class="inputbox">
    <br>
    <br>
    <button class="go_button" type="button" @click="launchNewQuiz">GO!</button>
  </div>
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

      this.$router.push('/questions');
    },
  }

}
</script>


<style>
.saisir_nom{
  font-size : 1.8rem;
}
.inputbox,.go_button{
  font-size : 1.5rem;
}
#startquizpage{
  height: 100%;
  width: 100%;
  margin: 0;
  text-align: center;
}
</style>
