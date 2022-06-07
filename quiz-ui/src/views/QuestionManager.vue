<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from "./QuestionDisplay.vue";
var answers_list;
export default {
  data() {
    return {
      currentQuestion: {
        questionTitle: '',
        questionText: '',
        possibleAnswers: [{text:''},{text:''},{text:''},{text:''}],
        image: ''
      },
      currentQuestionPosition: 0
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    answers_list = [];
    await this.loadQuestionByPosition();

  },
  methods: {
    async loadQuestionByPosition() {
      this.currentQuestionPosition++;
      const q1 = await quizApiService.getQuestion(this.currentQuestionPosition );
      this.currentQuestion.questionTitle = q1.data.title,
        this.currentQuestion.questionText = q1.data.text,
        this.currentQuestion.possibleAnswers = q1.data.possibleAnswers,
        this.currentQuestion.currentQuestionPosition = q1.data.position
      this.currentQuestion.image = q1.data.image
    },
    async answerClickHandler(number) {
      answers_list.push(number);
      if (this.currentQuestionPosition <10) {
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
      const resultquizz = await quizApiService.AddParticipation(dictjs);
      participationStorageService.saveParticipationScore(resultquizz.data.score);
      participationStorageService.saveParticipationRank(resultquizz.data.ranking);
      this.$router.push('/Score');
    }
  }

}
</script>
 

<template>
  <br><br><br>
  <h2 class="question_number">Question {{ this.currentQuestionPosition }} / 10</h2>
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