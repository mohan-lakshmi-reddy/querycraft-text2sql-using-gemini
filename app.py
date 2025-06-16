import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space as avs

# Load environment variables
load_dotenv()

# --- Check for Google API Key ---
#google_api_key = os.getenv("GOOGLE_API_KEY")
#if not google_api_key:
 #   st.error("Google API Key not found. Please set it in your .env file.")
  #  st.stop() # Stop the app if the key is missing

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")



# Gemini API response function
def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

# Prompt template
input_prompt_template = """
You are an AI language model that can convert plain English descriptions of database queries into valid SQL statements. Your task is to read an English description of a query and output the corresponding SQL query.
Follow these guidelines:
Identify the table(s) involved.
Determine the specific columns needed.
Recognize any conditions or filters that should be applied.
Include any sorting, grouping, or aggregation if specified.
Format the SQL query properly.
Here are some examples:
Example 1:
Input: "Retrieve the names and ages of all employees who are older than 30 years."
Output: SELECT name, age FROM employees
WHERE age > 30;
Example 2:
Input: "Get the total sales amount from the orders table."
Output: SELECT SUM(amount) FROM orders;
Example 3:
Input: "Find the list of customers who made purchases in the last month, sorted by the date of purchase in descending order."
Output: SELECT customer_name FROM purchases
WHERE purchase_date > DATE_SUB(CURDATE(), INTERVAL 1 MONTH) ORDER BY purchase_date DESC;
Example 4:
Input: "Show the average salary of employees grouped by department."
Output: SELECT department, AVG(salary) FROM employees
GROUP BY department;
Your tasks Convert the following English descriptions into SQL queries.
Input: {sql_text}
Things you need to remember everytime-
-50 Query:
And from the next line write the sql query snippet
Present the results following the same format as the examples provided above.
Break the query snippet as shown in examples
"""


# Streamlit UI configuration
st.set_page_config(page_title="Text to SQL Query", layout="wide") # Corrected: page_title

avs(4) # Corrected: call avs directly without .add_vertical_space

col1, col2 = st.columns([3, 2])

with col1:
    st.title("QueryCraft")
    st.header("Making Database queries as Easy as Conversation!")
    st.markdown(
        """<p style='text-align: justify;'>
        Introducing QueryCraft, your revolutionary solution for simplifying database 
        interactions through natural language queries. Powered by a cutting-edge Large 
        Language Model (LLM), Querycraft seamlessly converts everyday language into accurate
        SQL queries, eliminating the need for SQL expertise, whether you're a business analyst 
        seeking quick insights, a customer support representative streamlining data retrieval, 
        or an educator enhancing student learning experiences, Querycraft offers versatile solutions
        tailored to your needs. Say goodbye to complex database interactions and hello to effortless 
        data access with QueryCraft. Unlock the
        power of natural language querying today! </p>""", unsafe_allow_html=True
    )

with col2:
    img = Image.open("images/icon.png") # Make sure "images/icon.png" exists
    st.image(img, use_container_width=True)
avs(2)
# ───── Offering Section ─────
col1, col2 = st.columns([3, 2]) # You might want to swap this to have image on left, text on right for this section

with col2: # This means text is on the right
    st.header("Wide Range of Offerings")
    st.write("- Seamless Natural Language to SQL Conversion: Effortlessly convert natural language questions into SQL queries.")
    st.write("- Business Analytics: Enable business analysts to quickly access and analyze data without needing SQL expertise.")
    st.write("- Customer Support: Streamline data retrieval for customer support representatives, reducing response times and enhancing customer satisfaction.")
    st.write("- Educational Tools: Assist students in learning SQL by allowing them to input queries in plain English.")
    st.write("- Increased Productivity: Improve decision-making and productivity by simplifying database interactions.")
    st.write("- Intuitive User Experience: Provide an intuitive and engaging experience for users across various scenarios.")
    st.write("- Versatile Solutions: Cater to the needs of business analysts, customer support representatives, and educators.")

with col1: # This means image is on the left
    img1 = Image.open("images/icon1.png") # Make sure "images/icon1.png" exists
    st.image(img1, use_container_width=True)
avs(2)
# ───── Query Conversion Section ─────
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='text-align: center;'>Start Your Query Conversion</h1>", unsafe_allow_html=True)
    sql_text = st.text_area("Provide the text")
    submit = st.button("Submit")

    if submit:
        # Insert the user input into the input prompt template
        input_prompt = input_prompt_template.format(sql_text=sql_text)
        response = get_gemini_response(input_prompt)
        st.subheader(response) # Corrected: removed extra space

with col2:
    img2 = Image.open("images/icon2.png") # Make sure "images/icon2.png" exists
    st.image(img2, use_container_width=True)
avs(2)
# ───── FAQ Section ─────
col1, col2 = st.columns([2, 3])

with col2:
    st.write("Question: What is QueryCraft?")
    st.write("""Answer: QueryCraft is an advanced project powered by a Large Language Model (LLM) that converts natural language questions into SQL queries, simplifying database interactions for users without SQL expertise.""")
    avs(2) # Corrected: call avs directly
    st.write("Question: How can QueryCraft help business analysts?")
    st.write("""Answer: QueryCraft allows business analysts to ask questions in natural language and converts these questions into accurate SQL queries. This enables analysts to quickly access and analyze data, improving productivity and decision-making.""")
    avs(2) # Corrected: call avs directly
    st.write("Question: Can QueryCraft be used in customer support?")
    st.write("""Answer: Yes, customer support representatives can use QueryCraft to input questions like 'Show the recent orders placed by user ID 12345, which the LLM converts into SQL queries. This helps in quick and efficient data retrieval, reducing response times and enhancing customer satisfaction.""")

with col1:
    avs(3) # Corrected: call avs directly
    img3 = Image.open("images/icon3.png") # Make sure "images/icon3.png" exists
    st.image(img3, use_container_width=True)