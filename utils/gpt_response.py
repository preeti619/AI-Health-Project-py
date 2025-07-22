import google.generativeai as genai

genai.configure(api_key="your api")

model = genai.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat()

def ask_gpt(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
