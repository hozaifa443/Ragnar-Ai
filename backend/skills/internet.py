from ddgs import DDGS

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return "Sorry Sir, I couldn't find any results."

        answer = ""

        for result in results:
            answer += f"{result['title']}\n"
            answer += f"{result['body']}\n\n"

        return answer

    except Exception as e:
        print("Search Error:", e)
        return "Sorry Sir, I couldn't connect to the internet."