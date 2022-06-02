<template>
  <p> {{ question.currentquestion.questionTitle }}
    <br>
    <br>
    <button type="button" @click="launchNewQuiz">Suivant</button>
  </p>

</template>
<script>
import QuestionManagerVue from './QuestionManager.vue'
export default {
  props: {
    question: {
      type: Object
    }
  }
}
</script>

