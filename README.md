EduPlatform MVP
This is a minimal full-stack MVP (Minimum Viable Product) for an educational platform. The goal is to provide a complete, working example of a front-end and a back-end that communicate to handle user authentication, a quiz, and a personalized user dashboard.
Features
User Authentication: Signup and Login with client-side validation and a secure back-end using bcrypt for password hashing.
Interests Quiz: A multi-question quiz that captures user learning preferences.
Learning Profile: The back-end processes quiz results to generate a personalized learning profile.
Personalized Dashboard: A home page with a dynamic navbar and sections for a Student Dashboard, Learning Roadmap, Career Opportunities, and an AI Mentor Chat.
AI Mentor Chat (Mock): A simple chat interface that provides mock responses and saves conversation history, ready for a real LLM integration.
Responsive Design: The front-end is built with a mobile-first approach using plain CSS.
Tech Stack
Frontend: Plain HTML, CSS, and Vanilla JavaScript.
Backend: Streamlit (Python) for the server.
Database: SQLite (built-in Python library).
How to Run Locally
Follow these steps to get the application running on your machine.
1. Backend Setup
The backend is a Streamlit application that handles the API endpoints and serves the AI Mentor Chat page.
Navigate to the backend directory:
cd backend


Create and activate a Python virtual environment (recommended):
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate


Install the required Python packages:
pip install -r requirements.txt


Initialize the SQLite database: This script creates the users and quiz_results tables and seeds the database with a single demo user.
python init_db.py


Run the Streamlit application:
streamlit run app.py

This will start the backend server and open a new tab in your browser, typically at http://localhost:8501. Keep this terminal window open.
2. Frontend Setup
The frontend is a set of static HTML, CSS, and JS files. They will communicate with the running Streamlit backend.
Navigate to the frontend directory in a new terminal window:
cd frontend


Serve the files using a simple HTTP server. This is crucial for the JavaScript fetch API calls to work correctly.
# For Python 3
python -m http.server 8000

This will serve the files at http://localhost:8000.
3. Connecting and Testing
Open your browser and navigate to http://localhost:8000/index.html. You should see the login/signup page.
Use the demo user (testuser@example.com, password password123) or create a new account to log in.
Upon successful login, you'll be redirected to the quiz page.
Complete the quiz and click "Submit." The results will be stored, and you'll be redirected to the home page.
On the home page, you can click the navigation links in the top-right corner to see the different sections (Dashboard, Roadmap, etc.).
The "AI Mentor Chat" link will open the Streamlit chat page at http://localhost:8501.
How to Extend
This MVP is designed for easy extension. Here are a few next steps:
Real LLM Integration: The app.py has a dedicated TODO section in the AI Mentor Chat page. Simply replace the mock logic with a call to an LLM API (e.g., OpenAI, Gemini, etc.) using your API key.
Production Authentication: The current system uses a basic session state. For a production environment, you would use a proper token-based authentication system like JWTs to secure API endpoints.
Persistent Hosting: The front-end can be hosted on a service like Vercel or Cloudflare Pages, and the Streamlit backend can be deployed on a platform like Render or Heroku.