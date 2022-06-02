<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from "./QuestionDisplay.vue";
var currentQuestionPosition;
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
    await this.loadQuestionByPosition();

  },
  methods: {
    async loadQuestionByPosition() {
      const q1 = await quizApiService.getQuestion(currentQuestionPosition + 1);
      this.currentQuestion.questionTitle = q1.data.title,
        this.currentQuestion.questionText = q1.data.text,
        this.currentQuestion.possibleAnswers = q1.data.possibleAnswers,
        this.currentQuestion.currentQuestionPosition = q1.data.position
      this.currentQuestion.image = q1.data.image
    },
    async answerClickHandler() {
      loadQuestionByPosition();
      if (this.currentQuestionPosition == 10) {
        endQuiz();
      }
    },
    async endQuiz() {
      this.$router.push('/Score');
    }
  }

}
</script>
 

 <template>
  <h1>Question {{ currentQuestionPosition }} / {{ 10 }}</h1>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>
 
 <style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>