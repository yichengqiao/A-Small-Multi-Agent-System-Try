
import requests

class InformationRetrievalAgent:
    def __init__(self):
        self.api_url = "https://en.wikipedia.org/w/api.php"
        self.cache = {}

    def fetch_information(self, keywords):
        results = []
        for keyword in keywords:
            if keyword in self.cache:
                results.append(self.cache[keyword])
            else:
                params = {"action": "query", "format": "json", "list": "search", "srsearch": keyword, "utf8": 1}
                response = requests.get(self.api_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    if "query" in data and "search" in data["query"]:
                        search_results = data["query"]["search"]
                        if search_results:
                            result = {"keyword": keyword, "title": search_results[0]["title"], "snippet": search_results[0]["snippet"], "link": f"https://en.wikipedia.org/wiki/{search_results[0]['title'].replace(' ', '_')}"}
                            self.cache[keyword] = result
                            results.append(result)
        return results
