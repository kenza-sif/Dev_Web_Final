<template>
  <div id="body-home">
    <div id="questionpage">
      <h4> {{ question.questionTitle }} </h4>
      <br>
      <h4> " {{ question.questionText }} " </h4>
      <div id="questionimage">
        <img v-if="question.image" :src="question.image" alt="" height="200" width="200" />
      </div>
      <div>
        <button class="answer_button" type="button" @click="$emit('answer-question', 1)">{{
            question.possibleAnswers[0].text
        }}</button>
        <button class="answer_button" type="button" @click="$emit('answer-question', 2)">{{
            question.possibleAnswers[1].text
        }}</button>
        <br>
        <button class="answer_button" type="button" @click="$emit('answer-question', 3)">{{
            question.possibleAnswers[2].text
        }}</button>
        <button class="answer_button" type="button" @click="$emit('answer-question', 4)">{{
            question.possibleAnswers[3].text
        }}</button>
      </div>
    </div>
  </div>
</template>


<script>
//import QuestionManagerVue from './QuestionManager.vue'
export default {
  props: {
    question: {
      type: Object
    }
  },
  emits: ['answer-question']
}
</script>


<style>
#questionpage {
  height: 100%;
  width: 100%;
  margin: 0;

  text-align: center;
}

.answer_button {
  margin: 0.8rem 0.8rem 0.8rem 0.8rem;
  font-size: 1.5rem;
}

#questionimage {
  height: 100%;
  width: 100%;
  margin: 1.5rem 0.8rem 0.8rem 0.8rem;
  text-align: center;
}
</style>


