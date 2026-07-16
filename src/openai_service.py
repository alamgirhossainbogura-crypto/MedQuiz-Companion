import os
from openai import OpenAI

class OpenAIService:
    def __init__(self):
        # Replit Secret থেকে API Key লোড করা
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def get_ai_response(self, user_message, system_prompt, chat_history):
        messages = [{"role": "system", "content": system_prompt}]
        for msg in chat_history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_message})

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # বা হ্যাকার্থনের নির্দিষ্ট গাইডলাইন মডেল
                messages=messages
            )
            return {"success": True, "reply": response.choices[0].message.content}
        except Exception as e:
            return {"success": False, "error": str(e)}

# গ্লোবাল অবজেক্ট তৈরি
ai_service = OpenAIService()
