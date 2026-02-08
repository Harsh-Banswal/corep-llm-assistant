import os
from dotenv import load_dotenv
load_dotenv()

import google.genai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/text-bison-001")
response = model.generate_content("Say hello in one short sentence.")

print(response.text)
