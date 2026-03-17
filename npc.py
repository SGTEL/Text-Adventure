from ollama import chat, generate

MODEL = "llama3.2:latest"

class NPC:
    def __init__(self, name:str, backstory: str):
        self.name = name
        self.messages: list[dict] = [
            {
                "role": "user",
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

        response = chat(model=MODEL, messages=self.messages, stream=True)
        print(f"\n{self.name}: ", end="")
        for chunk in response:
            print(chunk.message.content, end='', flush=True)
        print()


fred: NPC = NPC("Fred", """
                        Your job is to insult the player and also 
                        pick them up specifically on any grammar mistakes.
                        The room you are in is the bathroom.
                        """)