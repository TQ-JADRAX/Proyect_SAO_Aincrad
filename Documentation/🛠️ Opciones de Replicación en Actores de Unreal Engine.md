## 🛠️ Opciones de Replicación en Actores de Unreal Engine

### 1. `Replicates`

Activa la replicación del actor completo.

* ✅ Sin esto, el actor no existirá en otros clientes.
* Requerido para cualquier replicación de propiedades, eventos o movimiento.

### 2. `Replicate Movement`

Replica automáticamente la ubicación, rotación y escala del actor.

* Incluye interpolación.
* No replica simulación física, solo transformaciones.

### 3. `Net Load on Client`

Hace que el actor colocado en el mapa se cargue automáticamente en los clientes.

* ✅ Útile para objetos estáticos colocados manualmente.
* ❌ No aplica a actores generados en tiempo de ejecución.

### 4. `Replicate Physics to Autonomous Proxy`

Replica la física desde el servidor hacia el cliente que controla el actor.

* ✅ Útile en juegos de vehículos con simulación física.
* Puede causar jitter si no se maneja correctamente.

---

## 🔍 Ejemplo de configuración según tipo de actor

| Actor            | Replicates | Replicate Movement | Net Load on Client | Replicate Physics to AP |
| ---------------- | ---------- | ------------------ | ------------------ | ----------------------- |
| Jugador          | ✅          | ✅                  | ❌                  | ✅                       |
| Enemigo colocado | ✅          | ✅                  | ✅                  | ❌                       |
| Pickup en mapa   | ✅          | ❌                  | ✅                  | ❌                       |
| Proyectil spawn  | ✅          | ✅                  | ❌                  | ❌                       |
