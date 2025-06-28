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

def obtener_commits(n=1):
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


def filtrar_features_changelog(commits_c):
    return [c for c in commits_c if c.lower().startswith("changelog:")]



def generar_anuncio(commits_filtrados):
    if not commits_filtrados:
        return "No se encontraron nuevas funcionalidades en los últimos commits."

    prompt = (
        "Solo responde con el texto del anuncio, sin ningún saludo, introducción ni explicación, crea un anuncio de feature para mi juego el cual es una recreacion de el juego sword art online (Aincrad) en el cual se describa de una manera amplia,ilustrativa y congruente para los usuarios acerca de lo que se esta trabajando, hazlos llamativos y llamativos para los usuarios al español e ingles"
        "Basado en los siguientes commits de nuevas funcionalidades:\n\n"
        + "\n".join(commits_filtrados)
    )

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",  # Modelo gratuito de OpenRouter
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature= 0.7,
            max_tokens= 900
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error al generar con OpenRouter: {e}"
    
def generar_changelog(commits_filtrados_c):
    if not commits_filtrados_c:
        return "No se encontraron cambios para generar un changelog en los ultimos commits"
    
    prompt_c = (
        "Solo responde con el texto del anuncio, sin ningún saludo, introducción ni explicación, crea un anuncio de cahngelog para mi juego el cual es una recreacion de el juego sword art online (Aincrad) en el cual se describa de una manera amplia,ilustrativa y congruente para el equipo de programacion acerca de lo que se esta trabajando, hazlos llamativos y tecnicos para mi equipo de trabajo en mi repositorio de github al español e ingles"
        "Basado en los siguientes commits de nuevos changes:\n\n"
        + "\n".join(commits_filtrados_c)
    )

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",  # Modelo gratuito de OpenRouter
            messages=[
                {"role": "user", "content": prompt_c}
            ],
            temperature=0.7,
            max_tokens=900
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error al generar con OpenRouter: {e}"
    

def enviar_a_discord_changelog(mensaje):
    if mensaje == "No se encontraron cambios para generar un changelog en los ultimos commits":
        print('No se envio nada a Discord en el canal CHANGELOG')
        return
    
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL_CHANGELOG_CHAT")  # La URL la tomamos desde .env
    
    if not webhook_url:
        print("❌ Webhook de Discord no configurado.")
        return
    
    # Divide el mensaje en bloques de 2000 caracteres
    partes = [mensaje[i:i+2000] for i in range(0, len(mensaje), 2000)]

    for parte in partes:
        response = requests.post(webhook_url, json={"content": parte})
        if response.status_code == 204:
            print("✅ Parte enviada a Discord.")
        else:
            print(f"❌ Error al enviar a Discord: {response.status_code} - {response.text}")



def enviar_a_discord(mensaje):
    if mensaje == "No se encontraron nuevas funcionalidades en los últimos commits.":
        print('No se envio nada a discord en el canal FEATURES')
        return
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")  # La URL la tomamos desde .env
    if not webhook_url:
        print("❌ Webhook de Discord no configurado.")
        return

    # Divide el mensaje en bloques de 2000 caracteres
    partes = [mensaje[i:i+2000] for i in range(0, len(mensaje), 2000)]

    for parte in partes:
        response = requests.post(webhook_url, json={"content": parte})
        if response.status_code == 204:
            print("✅ Parte enviada a Discord.")
        else:
            print(f"❌ Error al enviar a Discord: {response.status_code} - {response.text}")

    
def main():
    commits = obtener_commits()
    commits_c = obtener_commits()
    features = filtrar_features(commits)
    anuncio = generar_anuncio(features)
    changelog = filtrar_features_changelog(commits_c)
    anuncio_changelog = generar_changelog(changelog)
    print("\n📢 Anuncio generado:\n")
    print(anuncio)
    enviar_a_discord(anuncio)
    print("\n📢 Changelog generado:\n")
    print(anuncio_changelog)
    enviar_a_discord_changelog(anuncio_changelog)
    
if __name__ == "__main__":
       print("🚀 Ejecutando GPT Commit Announcer...")
       main() 