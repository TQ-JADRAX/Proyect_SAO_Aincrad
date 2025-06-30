## 🚀 Eventos Replicados en Unreal Engine (RPCs)

Los Remote Procedure Calls (RPCs) permiten ejecutar lógica en otras máquinas de la red: servidor o clientes.

---

### 1. 🤖 `Run on Server` (Ejecutar en el servidor)

* ✅ Se llama desde el cliente.
* ⚖️ Se ejecuta **solo en el servidor**.
* 🤔 Requiere que el actor sea **replicado** y **controlado por el cliente**.

**Ejemplo:** disparar un arma, lanzar un hechizo.

**Uso:** Validación de acciones y ejecución autoritaria.

---

### 2. 🌌 `Multicast`

* ✅ Se llama desde el servidor.
* 🚀 Se ejecuta **en todos los clientes y el servidor**.
* ⚖️ Ideal para **mostrar efectos visuales** globales.

**Ejemplo:** explosiones, sonidos, VFX compartidos.

**Uso:** Reproducción de eventos visuales para todos los jugadores.

---

### 3. 👤 `Run on Owning Client` (Ejecutar en cliente propietario)

* ✅ Se llama desde el servidor.
* 🤝 Se ejecuta **solo en el cliente que controla ese actor**.
* ⚖️ Ideal para **UI, efectos o mensajes privados**.

**Ejemplo:** mostrar "Has subido de nivel", abrir HUD.

**Uso:** Información personalizada para un solo jugador.

---

## 📊 Comparativa

| Tipo de Evento  | Quién lo llama | Dónde se ejecuta              | Cuándo usarlo                                   |
| --------------- | -------------- | ----------------------------- | ----------------------------------------------- |
| `Run on Server` | Cliente        | Solo en servidor              | Validar acciones o generar eventos globales     |
| `Multicast`     | Servidor       | Todos los clientes + servidor | Mostrar efectos o sonidos para todos            |
| `Run on Client` | Servidor       | Solo cliente propietario      | Mostrar mensajes, UI o animaciones individuales |

---

**Nota:** Los eventos replicados solo funcionan en actores replicados (`bReplicates = true`) y bajo condiciones reales de red.
