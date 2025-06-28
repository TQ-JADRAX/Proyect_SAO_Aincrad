import subprocess
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import requests
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
        "crea un anuncio de feature para mi juego el cual es una recreacion de el juego sword art online (Aincrad) en el cual se describa de una manera ilustrativa y congruente para los usuarios acerca de lo que se esta trabajando, y de manera separada un changelog para el repositorio de github, hazlos llamativos y llamativos para los usuarios"
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

def enviar_a_discord(mensaje):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")  # La URL la tomamos desde .env
    if not webhook_url:
        print("❌ Webhook de Discord no configurado.")
        return

    data = {
        "content": mensaje
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("✅ Anuncio enviado a Discord.")
    else:
        print(f"❌ Error al enviar a Discord: {response.status_code} - {response.text}")

def main():
    commits = obtener_commits()
    features = filtrar_features(commits)
    anuncio = generar_anuncio(features)
    print("\n📢 Anuncio generado:\n")
    print(anuncio)

if __name__ == "__main__":
       print("🚀 Ejecutando GPT Commit Announcer...")
       commits = obtener_commits()
       features = filtrar_features(commits)
       anuncio = generar_anuncio(features)
       print("\n📢 Anuncio generado:\n")
       print(anuncio)
       enviar_a_discord(anuncio)
       main() 