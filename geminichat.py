import google.generativeai as genai
genai.configure(api_key="AIzaSyBJWBQEmL8pNHpjwmaQpdl9HEzBV3Fyjw0")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
while True:
    message = input("You: ")
    response = chat.send_message(message)
    print("Gemini: " + response.text)