# Brief
A text based old-school adventure game, with the addition of ollama AI model
NPCS. 

## Features
* Use the model to parse the users input and map it to one of the predefined options. (FUTURE)
* NPCs whose dialogue is entirely AI based, I will provide a starting context, then the message context
  for each AI will be saved.

## Structure
Rooms - Each room will be a class that references it's neighbours, contains items + NPCs.
NPCs - Each will be a class with a background + what they know and past message context.
Player - Class instance with an inventory.