---
### 🛠️ Fix Weapon Colliders for VR Character in Unreal Engine

#### 📋 Description
    
    There is an issue with the current collision system for melee weapons in the VR project. The weapons are not properly   interacting with the VR character. This ticket aims to implement a clean and functional collision setup.
---

#### ✅ Tasks

1. 🔧 **Disable static mesh colliders**

   * Ensure all default static mesh collisions are turned off to avoid unwanted overlap or interference.

2. 🟥 **Create custom hitboxes for each weapon**

   * Add a `Box Collision` or `Capsule Collision` component to each weapon blueprint for accurate collision detection.

3. ✋ **(Optional - for testing) Add grip points**

   * Implement a grip socket or a scene component that represents the holding point of each weapon.

4. 🔍 **Verify correct hit detection and behavior**

   * Test the collision responses in VR (overlap events, blocking, etc.).

5. ⚙️ **Adjust player character collision behavior**

   * Modify how the character handles incoming collisions from weapons (e.g., overlap vs. block, custom responses).

---

#### 📌 Notes

* Make sure the new hitboxes do **not** interfere with hand tracking or grabbing mechanics.
* Consider using custom collision channels if needed for better control.

---
