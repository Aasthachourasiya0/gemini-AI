import google.generativeai as genai
genai.configure(api_key="AIzaSyBJWBQEmL8pNHpjwmaQpdl9HEzBV3Fyjw0")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is the meaning of life?")
print(response.text)
