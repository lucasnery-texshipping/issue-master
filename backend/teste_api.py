import google.generativeai as genai

# COLE SUA CHAVE AQUI DENTRO
API_KEY = "AIzaSyAqUvlt9IYQ1E3blfKW8A7O7vIGoD6c-T4"

genai.configure(api_key=API_KEY)

print("--- Buscando modelos disponíveis para sua chave ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Nome: {m.name}")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")