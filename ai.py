import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request
import googlesearch
import openai
import os
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env file
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


# 1. Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# 2. Expanded Knowledge Base with common problems and solutions
knowledge_base = {
    "printer not printing": "Check the power cable, look for paper jams, and verify ink or toner levels. Try restarting the printer.",
    "computer slow": "Restart your computer, close unnecessary programs, run a virus scan, and consider upgrading your RAM.",
    "network connection issues": "Check your router and cables, restart your modem/router, and contact your ISP if necessary.",
    "computer won't turn on": "Ensure the power cable is securely connected, check the outlet, and inspect the power button. It may be a hardware failure.",
    "forgot password": "Use the password recovery options provided by the service. For computer logins, try password hints or contact IT support.",
    "virus infection": "Run a full antivirus scan, disconnect from the internet to prevent further damage, and consider professional help if needed.",
    "blue screen error": "Check for hardware issues, update your drivers, and monitor your system for overheating.",
    "overheating": "Clean dust from cooling fans, ensure proper ventilation, and consider using a cooling pad.",
    "wifi not connecting": "Restart your router, check your network settings, update your Wi-Fi driver, or reset your network configurations.",
    "application crashing": "Update or reinstall the application, check error logs, and verify that your system meets the software requirements.",
    "error code 404": "Verify the URL, clear your browser's cache, and ensure the resource exists on the server.",
    "slow internet": "Restart your router, check for interference, update your firmware, or contact your ISP.",
    "battery draining fast": "Reduce screen brightness, close background apps, disable unnecessary features, and consider calibrating your battery."
}

# 3. Train the model (using the keys as problem statements)
problems = list(knowledge_base.keys())
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(problems)
model = MultinomialNB()
model.fit(X, problems)

# 4. Diagnose function that predicts the issue and returns the solution if available
def diagnose_problem(user_input):
    input_features = vectorizer.transform([user_input])
    predicted_problem = model.predict(input_features)[0]
    return knowledge_base.get(predicted_problem, "No solution found. Please provide more details.")

# 5. AI solution fallback using the OpenAI API
def get_ai_solution(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User reported the following problem: {user_input}\nProvide a detailed troubleshooting solution in a concise manner:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        ai_solution = response.choices[0].text.strip()
        return ai_solution
    except Exception as e:
        return f"Error fetching AI solution: {e}"

# 6. Flask web app with fallback logic
@app.route("/", methods=["GET", "POST"])
def index():
    solution = None
    web_search_link = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        solution = diagnose_problem(user_input)

        # If no matching solution is found in the knowledge base
        if solution == "No solution found. Please provide more details.":
            try:
                search_query = user_input + " troubleshooting"
                search_results = list(googlesearch.search(search_query, tld="co.in", num=1, stop=1, pause=2))
                if search_results:
                    web_search_link = search_results[0]
                    solution = f"No specific solution found. Here is a web search result for you: {web_search_link}"
                else:
                    # Fallback to AI-generated solution if web search yields nothing
                    solution = get_ai_solution(user_input)
            except Exception as e:
                # If the web search fails, try the AI fallback
                solution = f"Error performing web search: {e}. Attempting AI solution: {get_ai_solution(user_input)}"

    return render_template("index.html", solution=solution, web_search_link=web_search_link)

if __name__ == "__main__":
    app.run(debug=True)
