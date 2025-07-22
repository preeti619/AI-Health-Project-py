import google.generativeai as genai

genai.configure(api_key="AIzaSyCm3aSL69-V0vuliEEhkbyev4r39HJcqcU")

model = genai.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat()

def ask_gpt(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"


# AIzaSyCm3aSL69-V0vuliEEhkbyev4r39HJcqcU
