# Non-Euclidean Environment With Ray Casting (Python)

## Topics:

- [General Description](https://github.com/LuanSFMarques/non-euclidean_raycast#general-description)
- [Ray Casting (How it Works?)](https://github.com/LuanSFMarques/non-euclidean_raycast#ray-casting-how-it-works)
- [Ray Casting with PyGame](https://github.com/LuanSFMarques/non-euclidean_raycast#ray-casting-with-pygame)
- [Config](https://github.com/LuanSFMarques/non-euclidean_raycast#settings)
- [Non-Euclidean "Magic"](https://github.com/LuanSFMarques/non-euclidean_raycast#non-euclidean-magic)
- [How to execute](https://github.com/LuanSFMarques/non-euclidean_raycast#how-to-execute)
- [Motivation & Inspiration](https://github.com/LuanSFMarques/non-euclidean_raycast#motivation--inspiration)
- [Credits](https://github.com/LuanSFMarques/non-euclidean_raycast#credits)

## General Description
"Non-Euclidean Environment with Ray Casting" is my individual project, developed as a part of my final exam for the "CS50x" course at Harvard. As the project's name suggests, it involves the creation of a compact non-Euclidean space using the "Ray Casting" technique. This technique, initially employed in the iconic game Wolfenstein 3D in 1992, has the remarkable ability to craft a 3D world using only a Cartesian plane, straightforward map design, and some mathematical principles. If you're curious to learn more, let's delve into the next topic!

## Ray Casting (How it Works?)
Ray Casting is a method in which a ray is projected from a specific vantage point, following a defined path and translating the gathered data into visual information. In this project, we harnessed this technique to generate multiple rays emanating from the player's perspective until they intersect with a wall. Subsequently, the distance between the player and the wall, as determined by these cast rays, serves as critical data for computing the dimensions of virtual walls in a pseudo-3D environment. Each ray essentially represents a segment of the 3D world view, and when combined (across the field of view), they craft an 
illusion of depth, resulting in a convincing simulation of the 3D realm famously seen in "Wolfenstein 3D".

## Ray Casting with PyGame
PyGame is an immensely valuable library for developing games with the Python programming language. While it may not be the optimal choice for playing high-performance games due to Python's performance characteristics, it was employed for a specific purpose in this project: to facilitate the training of algorithms in Python. As indicated in the project files, there are a total of 5 .py files, and each one, with the exception of the configuration file, incorporates PyGame for various 
functionalities.
The "Draw" function played a pivotal role in all graphic design aspects of the project, eliminating the need for external images or alternative tools to shape the project's visual elements. It's crucial to note that the raycasting calculation algorithm is independent of PyGame; PyGame's role primarily lies in displaying the outcomes of this algorithm on the screen.

## Settings
Within the "settings.py" file, you'll discover numerous constants thoughtfully defined to enhance code clarity and maintainability during development. These constants encompass crucial data, such as "screen height," "screen width," "field of view (FOV)," and the "number of rays within the FOV." These values were centralized in this file to serve as references for other .py files in the project, streamlining the coding process and ensuring consistency.

## Non-Euclidean "Magic"
Here lies the most captivating aspect of this endeavor. Non-Euclidean geometry, as you may be aware, diverges from the principles of Euclidean geometry in an axiomatic system. What does this signify? It implies that space behaves in a decidedly unorthodox manner, defying our conventional understanding. Picture this: you step into your house and unexpectedly find yourself amidst a sprawling football field. How is such a perplexing space woven into a pseudo-3D world, you wonder? The answer lies in the art of illusion.

In due course, you'll notice a smaller corridor leading to a passage seemingly larger than it should logically be. This apparent anomaly is achieved through the clever use of what we'll call a "portal." When you approach the entrance to this diminutive corridor, the portal seamlessly ushers you into a view that mirrors what you'd see if you were peering into another hallway. Upon entering it, you experience a fluid transition to the other corridor, creating the illusion of continuous movement without teleportation.

In practice, whenever your character gazes at the smaller hallway, a duplicate is fashioned, sharing a perspective similar to yours in relation to the smaller hallway but oriented toward the other hallway. Eventually, the perspectives of the duplicate and your playable character are seamlessly swapped, and this sleight of hand becomes apparent when you are teleported. (The code,featuring a top view of the characters, vividly illustrates this phenomenon.)

## How to execute
Execute the "non_euclidean_raycast.exe" file in the directory alongside the files "n_euclidean1_ray," "n_euclidean2_ray," and "menu.py." Upon launching the application, you will encounter two choices. The first, "First-Person only," grants you the ability to exclusively view the pseudo-3D world rendered through ray casting. The second option, "Debug View Mode," offers insight into the inner workings of the program, revealing the perspective of the generated clone and the blocks visible to the main character.

## Motivation & Inspiration
My inspiration for embarking on this project drew from the intriguing concepts presented in the book "House of Leaves" and the Doom 2 map "MyHouse.wad." Both of these sources delve into the notion of impossible spaces, piquing my curiosity and fueling my motivation to explore this theme further. For those with an interest in this captivating subject, I wholeheartedly recommend delving into the pages of the book and immersing yourself in the mod by playing it within the game.

## Credits
So many thanks to Stanislav Petrov for helping me enormously with his video teaching how to create a ray casting in pygame. 
- Stanislav youtube channel: https://www.youtube.com/@CoderSpaceChannel
- Stanislav Github: https://github.com/StanislavPetrovV/DOOM-style-Game