import streamlit as st
import os
import io
import contextlib

# Function to load questions and hints from the 45_phython_questions folder
def load_questions():
    questions = {}
    hints = {}
    folder_path = "45_phython_questions"  # Path to the folder containing questions

    # Check if the folder exists
    if not os.path.exists(folder_path):
        st.error(f"Error: Folder '{folder_path}' not found. Please make sure the folder exists.")
        return questions, hints

    # Load questions and hints from Python files
    for file in os.listdir(folder_path):
        if file.endswith(".py"):  # Only process Python files
            try:
                with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    # Extract hint from the file (if any)
                    hint = "Hint: Use the `print()` function for basic output."  # Default hint
                    if "# Hint:" in content:
                        hint = content.split("# Hint:")[1].split("\n")[0].strip()
                    questions[file] = content
                    hints[file] = hint
            except Exception as e:
                st.error(f"Error loading file '{file}': {e}")

    # Check if any questions were loaded
    if not questions:
        st.error("No questions found in the folder. Please check the files.")

    return questions, hints

# Function to capture output from user's code
def capture_output(code):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code)
        except Exception as e:
            return f"Error: {e}"
    return output.getvalue()

# Main Streamlit app
def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
            /* Main background color */
            .stApp {
                background-color: #1e1e1e;  /* Dark background like VS Code */
            }
            /* Headers and text */
            h1, h2, h3, h4, h5, h6, p, div, span, label {
                color: #ffffff !important;  /* White text for dark background */
            }
            /* Dropdown menu (Select a question) */
            .stSelectbox > div > div > div > input {
                background-color: #333333;  /* Dark gray background */
                color: #ffffff !important;  /* White text */
                border-radius: 5px;
            }
            /* Code blocks (Python code preview) */
            .stCodeBlock {
                background-color: #1e1e1e;  /* Dark background like VS Code */
                color: #d4d4d4;  /* Light gray text */
                border-radius: 5px;
                padding: 10px;
                font-family: 'Consolas', monospace;
            }
            /* Syntax highlighting for Python code */
            .stCodeBlock .keyword {
                color: #569cd6;  /* Blue for keywords */
            }
            .stCodeBlock .string {
                color: #ce9178;  /* Orange for strings */
            }
            .stCodeBlock .comment {
                color: #6a9955;  /* Green for comments */
            }
            .stCodeBlock .function {
                color: #dcdcaa;  /* Yellow for functions */
            }
            .stCodeBlock .number {
                color: #b5cea8;  /* Light green for numbers */
            }
            /* Text area (Code editor) */
            .stTextArea textarea {
                background-color: #333333;  /* Dark gray background */
                color: #d4d4d4;  /* Light gray text */
                border-radius: 5px;
                font-family: 'Consolas', monospace;
            }
            /* Buttons */
            .stButton button {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
            /* Progress bar */
            .stProgress > div > div {
                background-color: #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎯 Python Practice App")
    st.write("Welcome to the Python Practice App! Select a question from the list below to get started.")

    # Load questions and hints
    questions, hints = load_questions()

    # Check if questions were loaded
    if not questions:
        st.warning("No questions available. Please check the repository and try again.")
        return

    # Sort questions by file name
    sorted_questions = sorted(questions.items(), key=lambda x: x[0])

    # Display list of questions with icons and numbering
    st.markdown("### 📚 Questions")
    selected_question = st.selectbox(
        "Select a question",
        [f"📝 {i+1}. {file}" for i, (file, _) in enumerate(sorted_questions)]
    )

    # Extract the selected file name
    selected_file = selected_question.split(". ")[1]

    # Display the selected question
    st.markdown(f"### 🚀 {selected_file}")
    st.code(questions[selected_file], language="python")  # Display the Python code

    # Code editor for users to write their solution
    user_code = st.text_area("✍️ Write your code here", height=200)

    # Run code button
    if st.button("▶️ Run Code"):
        if user_code.strip():  # Check if the user has entered code
            output = capture_output(user_code)
            st.write("**Output:**")
            st.code(output)
        else:
            st.warning("Please write some code before running.")

    # Display unique hint for the selected question
    if st.checkbox("💡 Show Hint"):
        st.write(hints[selected_file])

    # Python libraries information
    st.markdown("---")
    st.markdown("### 📚 Python Libraries Information")
    st.write("Here are some major Python libraries and their uses:")
    st.write("- **NumPy**: For numerical computations.")
    st.write("- **Pandas**: For data manipulation and analysis.")
    st.write("- **Matplotlib**: For data visualization.")
    st.write("- **Seaborn**: For statistical data visualization.")
    st.write("- **Scikit-learn**: For machine learning.")
    st.write("- **TensorFlow**: For deep learning.")
    st.write("- **PyTorch**: For deep learning and neural networks.")
    st.write("- **Flask**: For building web applications.")
    st.write("- **Django**: For building robust web applications.")
    st.write("- **Requests**: For making HTTP requests.")
    st.write("- **BeautifulSoup**: For web scraping.")
    st.write("- **OpenCV**: For computer vision tasks.")
    st.write("- **Pillow**: For image processing.")
    st.write("- **SQLAlchemy**: For database interactions.")
    st.write("- **Streamlit**: For building web apps with Python.")

    # Progress tracker
    st.markdown("---")
    st.markdown("### 📊 Progress Tracker")
    total_questions = len(sorted_questions)
    completed_questions = st.slider("Completed Questions", 0, total_questions, 0)
    st.write(f"**Progress:** {completed_questions}/{total_questions}")

# Run the app
if __name__ == "__main__":
    main()
