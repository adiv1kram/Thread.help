import os
import google.generativeai as genai
import json

# --- Configuration ---
# IMPORTANT: You must get your own API key from Google AI Studio
# and set it as an environment variable.

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# --- Prompt Engineering ---
def create_genai_prompt(parsed_data):
    """
    Constructs a detailed prompt for the GenAI model based on parsed thread data.
    """
    if not parsed_data:
        return None # Return None if there's no data to analyze

    
    total_threads = len(parsed_data)
    
    
    states = {thread.get('java_state', 'UNKNOWN') for thread in parsed_data}
    state_counts = {state: 0 for state in states}
    for thread in parsed_data:
        state_counts[thread.get('java_state', 'UNKNOWN')] += 1

    # This is a basic Prompt String I built
    prompt = f"""
    You are an expert Java performance analysis bot named "Thread.help".
    Your task is to analyze a structured JSON representation of a Java thread dump.
    Identify key performance issues like deadlocks, resource contention, and blocked threads.
    Provide a concise summary, a list of diagnosed problems with supporting evidence,
    and a list of actionable recommendations. The output must be in markdown format.

    **Analysis Request:**

    **Summary of Thread States:**
    - Total Threads: {total_threads}
    - Thread States: {json.dumps(state_counts)}

    **Full Thread Dump Data (JSON):**
    {json.dumps(parsed_data, indent=2)}

    **Your Task:**
    1.  **Summary:** Briefly describe the overall state of the application based on the data.
    2.  **Diagnosis:** Identify specific problems (e.g., Deadlock, High Contention, Blocked I/O). For each problem, reference the specific thread names and lock IDs involved. Be precise.
    3.  **Recommendations:** Suggest concrete, actionable solutions to fix the diagnosed problems. For example, "Increase the database connection pool size" or "Review the synchronized block in 'com.example.MyClass' to avoid nested locking."
    ---
    """
    return prompt

# Analysis Function 
def analyze_with_genai(parsed_data):
    """
    Sends the parsed thread dump data to the Gemini model for analysis.
    """
    prompt = create_genai_prompt(parsed_data)
    
    if not prompt:
        return "The uploaded file does not contain any valid Java thread data to analyze."

    try:
        
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # This will catch any API key errors, network issues and etc.
        return f"An error occurred while contacting the GenAI service: {str(e)}"

