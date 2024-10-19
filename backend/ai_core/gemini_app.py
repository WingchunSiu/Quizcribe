import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present
if not api_key:
    raise ValueError("API Key not found in .env file")

# Configure the API key for the model
genai.configure(api_key=api_key)

# Function to call the Gemini API
def call_gemini(prompt, system_instruction):
    """
    Function to make a structured API call to the Gemini model.
    
    Args:
    - prompt (str): The user prompt for generating content.
    - system_instruction (str): The system instruction to guide the model.

    Returns:
    - str: The content generated by the model.
    """
    full_prompt = f"{system_instruction}\n\n{prompt}"
    
    # Use the 'generate_content' method for generating text
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(full_prompt)
   
    return response.text.strip()
    

# Function to summarize text
def summarize_text(input):
    summary_prompt = f"Summarize the following text:\n\n{input}"
    system_instruction = "You are an expert at summarizing transcripts."
    return call_gemini(summary_prompt, system_instruction)

# Function to generate quiz questions based on summary
 #output question in a list of python dictionary
def generate_quiz_questions(summary):
    question_prompt = f"Generate three quiz questions based on the following summary:\n\n{summary}"
    system_instruction = "You are an expert in generating quiz questions from summarized content."
    return call_gemini(question_prompt, system_instruction)


def api_summarize(text_input):
    """
    API call to get the summary of the input text.
    """
    print("Summarizing the text...")
    summary = summarize_text(text_input)
    print(f"Summary:\n{summary}\n")
    return summary

# API 2: Quiz Generation API Call
def api_generate_quiz(summary):
    """
    API call to generate quiz questions based on the provided summary.
    """
    print("Generating quiz questions...")
    raw_quiz_questions = generate_quiz_questions(summary)
    quiz_questions = []
    questions = raw_quiz_questions.strip().split('\n\n')  # Split by double newlines to separate questions

    for question_block in questions:
        lines = question_block.strip().split('\n')
        
        # Extract the question text (first line of the block)
        question_text = lines[0].strip()
        # Extract the choices (subsequent lines in the block)
        choices = []
        for line in lines[1:]:
            choice_text = line.strip()
            correct = '(correct)' in choice_text  # Mark the answer as correct if "(correct)" is found
             # Add the choice to the list
            choices.append({
                'text': choice_text.replace(' (correct)', '').split(') ')[1].strip(),  # Strip "a)", "b)", etc.
                'correct': correct
            })

         # Append the structured question with its choices to the quiz_questions list
        quiz_questions.append({
            'question': question_text,
            'choices': choices
        })

    print(f"Quiz Questions (parsed):\n{quiz_questions}\n")
    return quiz_questions



    
    return quiz_questions



# Example usage
if __name__ == '__main__':
    # Example text input (replace this with your own text)
    text_input = "The 1950s was a decade marked by the post-World War II boom, the dawn of the Cold War and the civil rights movement in the United States. “America at this moment,” said the former British Prime Minister Winston Churchill in 1945, “stands at the summit of the world.” During the 1950s, it was easy to see what Churchill meant. The United States was the world’s strongest military power. Its economy was booming, and the fruits of this prosperity–new cars, suburban houses and other consumer goods–were available to more people than ever before. However, the 1950s were also an era of great conflict. For example, the nascent civil rights movement and the crusade against communism at home and abroad in the Korean War exposed underlying divisions in American society."
    summary = api_summarize(text_input)
    quiz_questions = api_generate_quiz(summary)


    #output question in a list of python dictionary