## 🚀 Replicated Events in Unreal Engine (RPCs)

Remote Procedure Calls (RPCs) allow logic execution across the network: on the server or specific clients.

---

### 1. 🤖 `Run on Server`

* ✅ Called by a client.
* ⚖️ Executes **only on the server**.
* 🤔 Requires the actor to be **replicated** and **owned by the calling client**.

**Example:** firing a weapon, casting a spell.

**Use case:** authoritative validation and logic.

---

### 2. 🌌 `Multicast`

* ✅ Called from the server.
* 🚀 Executes on **all clients and the server**.
* ⚖️ Ideal for **global visual/audio effects**.

**Example:** explosions, sound cues, VFX.

**Use case:** display synchronized feedback to all players.

---

### 3. 👤 `Run on Owning Client`

* ✅ Called from the server.
* 🤝 Executes **only on the client that owns the actor**.
* ⚖️ Great for **UI or local player notifications**.

**Example:** show "Level Up", open inventory UI.

**Use case:** private effects for one player.

---

## 📊 Comparison Table

| Event Type      | Who Calls It | Where It Executes     | When to Use                                 |
| --------------- | ------------ | --------------------- | ------------------------------------------- |
| `Run on Server` | Client       | Only on server        | Validate input or trigger global logic      |
| `Multicast`     | Server       | All clients + server  | Show FX/audio to everyone                   |
| `Run on Client` | Server       | Only on owning client | Display UI, animations, or private messages |

---

**Note:** RPCs only work on actors with `bReplicates = true` and require real network conditions (not in standalone mode).
