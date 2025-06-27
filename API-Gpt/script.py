import subprocess
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

# Cargar .env desde ruta absoluta
dotenv_path = Path(__file__).resolve().parent / "Api_Key.env"
load_dotenv(dotenv_path)

# Leer API Key
api_key = os.getenv("OPENROUTER_API_KEY")

# Crear cliente apuntando a OpenRouter
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def obtener_commits(n=10):
    try:
        output = subprocess.check_output(
            ["git", "log", f"-n{n}", "--pretty=format:%s"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return output.strip().split("\n")
    except subprocess.CalledProcessError:
        print("❌ Error al ejecutar git log. ¿Estás en un repositorio Git?")
        return []

def filtrar_features(commits):
    return [c for c in commits if c.lower().startswith("feat:")]

def generar_anuncio(commits_filtrados):
    if not commits_filtrados:
        return "No se encontraron nuevas funcionalidades en los últimos commits."

    prompt = (
        "Genera un anuncio llamativo y breve en estilo de redes sociales al español y ingles "
        "basado en los siguientes commits de nuevas funcionalidades:\n\n"
        + "\n".join(commits_filtrados)
    )

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",  # Modelo gratuito de OpenRouter
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error al generar con OpenRouter: {e}"

def main():
    commits = obtener_commits()
    features = filtrar_features(commits)
    anuncio = generar_anuncio(features)
    print("\n📢 Anuncio generado:\n")
    print(anuncio)

if __name__ == "__main__":
    main() 