<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        possibleAnswers: []
      },
      currentQuestionPosition: 1
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    loadQuestionByPosition();

  },
  methods: {
    async loadQuestionByPosition() {
      const q1 = await quizApiService.GetQuestion(1);
      this.questionTitle = q1.data.title,
        this.questionText = q1.data.text,
        this.possibleAnswers = q1.data.possibleAnswers,
        this.currentQuestionPosition = q1.data.position
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
 