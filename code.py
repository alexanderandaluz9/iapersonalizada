import google.generativeai as genai

import os


# Configuración de tu API Key

API_KEY = "API"

genai.configure(api_key=API_KEY)



# Prompt

PROMPT_SISTEMA = """

Eres una IA

"""



# Configuración del modelo

generation_config = {

  "temperature": 0.7,

  "top_p": 0.95,

  "top_k": 64,

  "max_output_tokens": 8192,

}



model = genai.GenerativeModel(

  model_name="gemini-2.5-flash",

  generation_config=generation_config,

  system_instruction=PROMPT_SISTEMA,

)


chat_session = model.start_chat(history=[])

print("--- Mi IA (escribe 'salir' o 'adios' para terminar) ---")



while True:

  user_input = input("Tú: ")


  if user_input.lower() in ["salir", "exit", "quit", "adios"]:

    print("¡Adiós!")

    break


  try:

    response = chat_session.send_message(user_input)

    print(f"\nGemini: {response.text}\n")

  except Exception as e:

    print(f"Hubo un error: {e}")