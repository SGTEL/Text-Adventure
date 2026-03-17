from ollama import chat, generate

MODEL = "llama3.2:latest"

class NPC:
    def __init__(self, name:str, backstory: str):
        self.name = name
        self.messages: list[dict] = [
            {
                "role": "system",
                "content": f"""
                Your name is {self.name}. You are an NPC in a text adventure
                game with the following backstory: {backstory}. 
                Keep your answers to one or two sentences.
                """,
            }
        ]

    def talk(self, msg):
        self.messages.append(
            {
                "role": "user",
                "content": msg,
            }
        )

        response = chat(model=MODEL, messages=self.messages)
        self.messages.append(
            {
                "role": "assistant",
                "content": response.message.content,
            }
        )

        print(f"\n{self.name}: {response.message.content}")



fred: NPC = NPC("Fred", """
                        Your job is to insult the player and also 
                        pick them up specifically on any grammar mistakes.
                        The room you are in is the bathroom.
                        """)

mary: NPC = NPC("Mary", """
                        You are a priest whose job it is to convert the player
                        to you religion of goat worship. You are in the reception
                        area.
                        """)