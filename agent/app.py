import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is jotaro. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity. If you don't know something say you don't it and always try to understand what it is. if the user tells you something that is wrong, politely correct them and explain why it is wrong."
    history = []
    count = 0

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        count += 1
        if count >= 3:
            print('History:', history)

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')


run_chat()
"""
1
-input tokens are the amount of tokens used in your message to the AI.
2
- output tokens are the amount of tokens used in the AI's response.
- the output of the AI shortend
- yes they're identical
- hi answer is really different every time and the AI is not consistent is it's answers
-tempature controls the AI's randomness and creativity. A higher temperature (1.0) makes the AI more random and creative, while a lower tempature(0.0) makes it more focused and deterministic.
3
- because the AI doesn't have a memory so every time it is asked a question a past converstion or even in genearl it has to read the entire chat from the start just to get context and answer the user.

reflections: 
- in my world usually it would be fragrances since the more i collect the more expansive ones i buy or it can also be vinyl collecting since i always need more music to listen to so it just racks up.
- there will be an error or the ai won't understand the question or anything. nothing changed and nothing happend to input tokens from my understanding
- he didn't forget anything idk why naybe because i didn't try for that long or i didn't save so the code with the message ran.
the tokens actually disappeared like they didn't show up in the history output.
- no the AI is not different we just don't see the history of our conversation.
"""