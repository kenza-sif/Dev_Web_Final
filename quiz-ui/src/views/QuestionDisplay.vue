<template>
  <p> {{ question.questionTitle }} <br>
    {{ question.questionText }}
    <img v-if="question.image" :src="question.image" />
    <br>

  <div id="components-demo">
    <button type="button" @click="launchNewQuiz">{{ question.possibleAnswers[0].text }}</button>
    <button type="button" @click="launchNewQuiz">{{ question.possibleAnswers[1].text }}</button>
    <br>
    <button type="button" @click="launchNewQuiz">{{ question.possibleAnswers[2].text }}</button>
    <button type="button" @click="launchNewQuiz">{{ question.possibleAnswers[3].text }}</button>
  </div>

  <br>
  <br>
  <br>
  <br>
  <br>
  </p>

</template>
<script>
//import QuestionManagerVue from './QuestionManager.vue'
export default {
  props: {
    question: {
      type: Object
    }
  }
}
</script>

