
class AnswerSynthesisAgent:
    def synthesize(self, query, analysis_result, retrieved_data):
        answer = f"Question: {query}\n"
        answer += f"Intent: {analysis_result['intent']}\n"
        answer += f"Keywords: {', '.join(analysis_result['keywords'])}\n"
        answer += "\nRetrieved Information:\n"
        for item in retrieved_data:
            answer += f"- {item['title']}: {item['snippet']} (Link: {item['link']})\n"
        return answer
