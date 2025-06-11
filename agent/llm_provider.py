import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


class LLMWrapper:
    def __init__(self):
        from groq import Groq
        import os
        from dotenv import load_dotenv

        load_dotenv()

        self.provider = os.getenv("LLM_PROVIDER")
        self.api_keys = {
            "groq": os.getenv("GROQ_API_KEY"),
            "anthropic": os.getenv("ANTHROPIC_API_KEY")
        }

        if self.provider == "groq":
            self.client = Groq(api_key=self.api_keys["groq"])
        else:
            raise ValueError("Unsupported LLM_PROVIDER")

    def summarize(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful research paper summarizer."},
                {"role": "user", "content": f"Summarize this text: {text}"}
            ]
        )
        return response.choices[0].message.content.strip()

