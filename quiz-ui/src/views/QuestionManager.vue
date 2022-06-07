<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from "./QuestionDisplay.vue";
var currentQuestionPosition;
var answers_list;
export default {
  data() {
    return {
      currentQuestion: {
        questionTitle: '',
        questionText: '',
        possibleAnswers: [],
        image: ''
      },
      currentQuestionPosition: 1
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    currentQuestionPosition = 0;
    answers_list = [];
    await this.loadQuestionByPosition();

  },
  methods: {
    async loadQuestionByPosition() {
      currentQuestionPosition++;
      const q1 = await quizApiService.getQuestion(currentQuestionPosition );
      this.currentQuestion.questionTitle = q1.data.title,
        this.currentQuestion.questionText = q1.data.text,
        this.currentQuestion.possibleAnswers = q1.data.possibleAnswers,
        this.currentQuestion.currentQuestionPosition = q1.data.position
      this.currentQuestion.image = q1.data.image
    },
    async answerClickHandler(number) {
      answers_list.push(number);
      if (currentQuestionPosition <10) {
          this.loadQuestionByPosition();}
      else{
          this.endQuiz();
      }
      
      
    },
    async endQuiz() {
      const name=participationStorageService.getPlayerName()
      var dictjs={
          "playerName": name,
          "answers": answers_list
      };
      await quizApiService.AddParticipation(dictjs);
      this.$router.push('/Score');
    }
  }

}
</script>
 

<template>
  <br><br><br>
  <h2 class="question_number">Question {{ currentQuestionPosition }} / {{ 10 }}</h2>
  <QuestionDisplay :question="currentQuestion"
  @answer-question="answerClickHandler" 
 />
</template>
 

 
<style>
.question_number{
  height: 100%;
  width: 100%;
  margin: 1rem 0rem 0rem 2rem;
}
</style>