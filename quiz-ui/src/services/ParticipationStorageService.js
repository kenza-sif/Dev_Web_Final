export default {
  clear() {
    window.localStorage.clear()

  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    window.localStorage.getItem("playerName", playerName);
    return;
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    window.localStorage.getItem("participationScore", participationScore);
    return;
  }
};