import ollama

first_message = True

conversation = [
    {
        "role": "system",
        "content": """
You are Ragnar, a highly intelligent AI assistant.

Rules:
- Never say you are Gemma or an AI model.
- Address the user as "Sir" naturally.
- Greet only once at the beginning of the session.
- Speak professionally.
- Keep responses concise unless asked for details.
"""
    }
]

def ask_ragnar(user_input):
    global first_message, conversation

    # Greet only once
    if first_message:
        conversation.append({
            "role": "system",
            "content": "This is the first interaction of this session. Greet the user once."
        })
        first_message = False

    # Add user message
    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="gemma3:4b",
        messages=conversation
    )

    assistant_reply = response["message"]["content"]

    # Save assistant reply
    conversation.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply