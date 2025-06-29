In multiplayer game sessions, game state information is communicated between multiple machines over a network connection. In contrast, single-player, local games store all game state information on a single machine. Communication over a network connection makes creating multiplayer experiences inherently more complex than single-player experiences. The process of sharing information between players involves a different approach than a single-player game. Unreal Engine (UE) features a robust networking framework that powers some of the world's most popular online multiplayer games to help you streamline this process. This page provides an overview of the concepts that drive multiplayer programming and guides you to additional documentation about UE's tools for building multiplayer experiences.


Plan Early for Multiplayer
If there is any possibility that your project might need multiplayer features at any time, you should build all of your gameplay with multiplayer in mind from the start of your project. If your team consistently implements the extra steps for creating multiplayer, the process of building gameplay will not consume much more time compared to a single-player game. In the long run, your project will be easier for your team to debug and service. Meanwhile, any gameplay programmed for multiplayer in UE will still work as expected in single-player, non-networked play.

If you do not design your project with multiplayer in mind from the beginning, refactoring a codebase that you have already built without networking will require you to comb through your entire project and rewrite large sections of gameplay functionality. You also might need to reconsider your design since technical obstacles in networking such as network speed and stability may force you to change your existing design.


Unreal Engine Networking Architecture
UE uses the client-server architecture for networked multiplayer games. There are two types of multiplayer games: local multiplayer and networked multiplayer. In a single-player or local multiplayer game, your game runs locally on a single machine as a standalone game. In this instance, all players, assets, and functionality exists and all input is processed on a single machine. Players connect input to this machine and control everything directly in the game. There is no potential issue with communicating input from a player to the game because the player is connected directly to the game instance and the game instance can promptly process all input.



In a networked multiplayer game, many players on distinct machines connect to a central machine across a network. The central machine, known as the server, hosts the multiplayer game while all the other players on different machines connect to the server as clients. The server shares game state information with each connected client and provides the means for all the players on different machines to communicate with one another.(In networked multiplayer, the game takes place between a server and several connected clients. The server processes gameplay and the clients render the game to users.)

As opposed to local multiplayer, this presents additional challenges. Different clients might have different network connection speeds and information must be communicated across a potentially unstable network where input might get lost. As a result, at any given time, the state of the game on one client machine is likely to be different than every other client machine. The server, as the host of the game, holds the one, true, authoritative game state. In other words, the server is where the multiplayer game is actually played. The clients each control remote Pawns that they own on the server. Clients send remote procedure calls from their local pawn to their server pawn to perform in game actions. The server then replicates information about the game state to each client such as where Actors are located, how these actors should behave, and what values different variables should have. Each client then uses this information to simulate a close approximation of what is actually happening on the server.

By default, the server does not stream visuals directly to client monitors to display, the server sends state information to client game instances so the client machines can re-create the visuals inside their own game instances. Unreal Engine provides the Pixel Streaming system to pre-render frames and audio for display on mobile and web browsers. For more information, see the Pixel Streaming documentation.

#### Client-Server Gameplay-Example:

This section provides a side-by-side comparison of two players in a multiplayer game to illustrate the differences between local and networked multiplayer. On the left, the two players are playing local multiplayer. On the right, the two players are playing networked multiplayer.

##### Local Multiplayer:

.- Player 1 presses an input to fire a weapon.

    Player 1's Pawn responds to this by firing its current weapon.
    Player 1's weapon spawns a projectile and plays any accompanying sound or visual effects.

Player 1's projectile moves forward from the weapon.

.- Player 1's projectile collides with Player 2's pawn.

    The collision triggers a function that destroys Player 1's projectile, causes damage to Player 2's pawn, and plays any accompanying sound and visual effects.
    Player 2 plays an on-screen effect as a response to being damaged.

##### Networked Multiplayer:

.- Player 1 presses an input on their local machine to fire a weapon.

    Player 1's local Pawn relays the command to fire the weapon to its connected Pawn on the server.
    Player 1's weapon on the server spawns a projectile.
    The server notifies each connected client to create its own copy of Player 1's projectile.
    Player 1's weapon on the server notifies each client to play the sound and visual effects associated with firing the weapon.

.-Player 1's projectile on the server moves forward from the weapon.

    The server notifies each client to replicate the movement of Player 1's projectile as it happens, so each client's version of Player 1's    projectile also moves.


| Network Mode        | `ENetMode`           | Description                                                                                                                                  |
|----------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Standalone**       | `NM_Standalone`      | A game without networking with one or more local players. Acts as a server but doesn't accept remote connections. Used for single-player or local multiplayer. |
| **Dedicated Server** | `NM_DedicatedServer` | A server with no local players. Accepts only remote clients. Discards graphics, audio, and input. Used for persistent, secure, or large-scale multiplayer games. |
| **Listen Server**    | `NM_ListenServer`    | A server with a local player hosting the game. Accessible to other players. Often used for casual coop or competitive multiplayer.              |
| **Client**           | `NM_Client`          | A client connected to a remote server (dedicated or listen). It does not execute server-side logic.                                            |
