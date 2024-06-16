# imported the necessary libraries
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyD5EsYS77CIaJ__P_xZZVAoI3lbYtFiyv8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# for models in genai.list_models():
#     if 'generateContent' in models.supported_generation_methods:
#         print(models.name)

model = genai.GenerativeModel('gemini-pro')

print("================")
question = input("Ask me a question\n")
print("================")
response = model.generate_content(question)

print(response.text)
feedbacks = response.prompt_feedback.safety_ratings
for feedback in feedbacks:
    if feedback.category.HARM_CATEGORY_VIOLENCE == feedback.HarmProbability.HIGH or feedback.category.HARM_CATEGORY_VIOLENCE == feedback.HarmProbability.MEDIUM or feedback.category.HARM_CATEGORY_DANGEROUS_CONTENT == feedback.HarmProbability.HIGH or feedback.category.HARM_CATEGORY_DANGEROUS_CONTENT == feedback.HarmProbability.MEDIUM:
        print("This content is too dangerous")
        break