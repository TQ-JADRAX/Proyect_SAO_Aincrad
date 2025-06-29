## 🌟 Visión General de Redes en Unreal Engine 5.3

### 🎯 Fundamentos del Multijugador

* Arquitectura cliente-servidor.
* Modos de red (`ENetMode`): `Standalone`, `Listen Server`, `Dedicated Server`, `Client`.
* Replicación de actores (`bReplicates`), subobjetos replicados.

### 🔧 Gestión de Sesiones

* Crear, unir y gestionar sesiones multijugador.
* Integración con subsistemas online como Steam o EOS.

### 💻 Programación de Juegos Multijugador

* RPCs (Remote Procedure Calls).
* Roles de actor: Authority, Autonomous Proxy, Simulated Proxy.
* Prioridad, dormancia y relevancia.
* Replicación de propiedades y componentes.

### 🌐 Sistema de Replicación Iris

* Alta eficiencia para juegos con muchos actores replicados.
* Reemplaza o complementa el sistema tradicional de replicación.

### 🧰 Grafo de Replicación

* Sistema basado en nodos que organiza cómo y cuándo replicar.
* Permite optimizar qué datos se envían según zonas y relevancia.

### 🎥 Sistema de Repeticiones (Replay)

* Graba partidas para luego analizarlas o reproducirlas.
* Útil para QA, replays o presentaciones.

### 🚀 Despliegue de Juegos Multijugador

* Empaquetado para servidores dedicados o modo listen.
* Recomendaciones para estabilidad y escalabilidad.

### 🔎 Pruebas, Depuración y Optimización

* Herramientas: Network Profiler, Networking Insights, Unreal Insights.
* Comandos de consola: `stat net`, `netprofile`, `net pktloss`, etc.
* Emulación de condiciones de red (latencia, pérdida de paquetes).

### 📚 Tutoriales y Recursos

* Guías rápidas.
* Cursos oficiales.
* Foros de desarrolladores.

---

Fuente original: [Epic Games Documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine?application_version=5.3)
