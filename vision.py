import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyD5EsYS77CIaJ__P_xZZVAoI3lbYtFiyv8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

vision_model = genai.GenerativeModel('gemini-pro-vision')

import PIL.Image
image = PIL.Image.open('test2.jpeg')

response = vision_model.generate_content(["write a python program to change the format of the date to dd/mm/yy", image])
print(response.text)