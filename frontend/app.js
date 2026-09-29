const API_URL = "http://localhost:8000";

function addBubble(text, type) {
  const chat = document.getElementById("chat");
  const bubble = document.createElement("div");
  bubble.className = "bubble " + type;
  bubble.textContent = text;
  chat.appendChild(bubble);
  chat.scrollTop = chat.scrollHeight;
  return bubble;
}

async function askQuestion() {
  const input = document.getElementById("question");
  const button = document.getElementById("askBtn");
  const question = input.value;

  if (!question.trim()) return;

  addBubble(question, "user");
  input.value = "";
  button.disabled = true;

  const answer = addBubble("Thinking...", "bot");          // loading

  try {
    const response = await fetch(API_URL + "/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    if (!response.ok) throw new Error("HTTP " + response.status);

    const data = await response.json();
    answer.textContent = data.answer;                       // answer or fallback
  } catch (error) {
    console.error(error);
    answer.textContent = "API is unavailable. Is uvicorn running on port 8000?";
    answer.className = "bubble error";                      // API error
  } finally {
    button.disabled = false;
    input.focus();
  }
}

document.getElementById("question").addEventListener("keydown", (event) => {
  if (event.key === "Enter") askQuestion();
});