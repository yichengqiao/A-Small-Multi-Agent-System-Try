
from flask import Flask, render_template, request
from task_manager_agent import TaskManagerAgent
from question_understanding_agent import QuestionUnderstandingAgent
from information_retrieval_agent import InformationRetrievalAgent
from answer_synthesis_agent import AnswerSynthesisAgent

# Initialize Flask app and agents
app = Flask(__name__)
task_manager = TaskManagerAgent()
question_agent = QuestionUnderstandingAgent()
retrieval_agent = InformationRetrievalAgent()
synthesis_agent = AnswerSynthesisAgent()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user query from form
        user_query = request.form["query"]

        # Step 1: Question Understanding
        analysis_result = question_agent.analyze_query(user_query)

        # Step 2: Information Retrieval
        retrieved_data = retrieval_agent.fetch_information(analysis_result["keywords"])

        # Step 3: Answer Synthesis
        final_answer = synthesis_agent.synthesize(user_query, analysis_result, retrieved_data)

        # Render result
        return render_template("index.html", query=user_query, analysis=analysis_result, result=retrieved_data, final_answer=final_answer)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
