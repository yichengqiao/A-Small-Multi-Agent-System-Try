
class TaskManagerAgent:
    def __init__(self):
        self.tasks = []
        self.agent_responses = {}

    def receive_query(self, query):
        print(f"Received query: {query}")
        self.assign_tasks(query)

    def assign_tasks(self, query):
        question_agent_task = {"task_id": "1", "agent": "QuestionUnderstandingAgent", "query": query}
        self.tasks.append(question_agent_task)

        retrieval_agent_task = {"task_id": "2", "agent": "InformationRetrievalAgent", "query": query}
        self.tasks.append(retrieval_agent_task)

    def collect_response(self, task_id, agent_name, response):
        print(f"Received response from {agent_name}: {response}")
        self.agent_responses[task_id] = response

    def compile_responses(self):
        return {
            "query": self.agent_responses.get("1", {}).get("query", ""),
            "analysis": self.agent_responses.get("1", {}).get("analysis", ""),
            "information": self.agent_responses.get("2", {}).get("information", []),
        }

    def deliver_response(self):
        result = self.compile_responses()
        print("\n=== Final Response ===")
        print(result)
