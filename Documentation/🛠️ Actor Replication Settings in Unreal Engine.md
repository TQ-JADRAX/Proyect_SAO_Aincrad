## 🛠️ Actor Replication Settings in Unreal Engine

### 1. `Replicates`

Enables replication of the entire actor.

* ✅ Without this, the actor will not exist on clients.
* Required for any property, event, or movement replication.

### 2. `Replicate Movement`

Automatically replicates location, rotation, and scale.

* Includes interpolation for smooth visuals.
* Does not replicate physics simulation.

### 3. `Net Load on Client`

Ensures the actor placed in the level is loaded on clients upon connection.

* ✅ Useful for static, manually placed actors.
* ❌ Does not apply to dynamically spawned actors.

### 4. `Replicate Physics to Autonomous Proxy`

Replicates physics state from the server to the owning client.

* ✅ Useful for vehicle-like actors controlled by a player.
* Can cause jitter if not handled correctly.

---

## 🔍 Actor Type Configuration Example

| Actor              | Replicates | Replicate Movement | Net Load on Client | Replicate Physics to AP |
| ------------------ | ---------- | ------------------ | ------------------ | ----------------------- |
| Player             | ✅          | ✅                  | ❌                  | ✅                       |
| Placed Enemy       | ✅          | ✅                  | ✅                  | ❌                       |
| Map Pickup         | ✅          | ❌                  | ✅                  | ❌                       |
| Spawned Projectile | ✅          | ✅                  | ❌                  | ❌                       |
