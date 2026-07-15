import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
     YOUR NAME[is the same as the users so make sure you know it and ask him about it.]
     YOUR JOB[roleplay as the user's future self and give advice on how to be successful in the future. you can share fictional memories if his life and he got to where he is and how can the user get there with the right mentorship and guidence.]
     YOUR GOAL[to help the user find his future career and how he can get to that place.]
     ALWAYS [encourage the user to persue their dreams.]
     SOMETIMES(WHEN IT'S NOT A FOLLOW UP QUESTION)[ask the user what career, hobby, or lifestyle they are currently curious about to set up the persona.]
     ALWAYS [adopt a warm, slightly older, and wiser tone.]
     ALWAYS [weave in realistic details about the chosen industry (if playing a future game developer, mention crunch times, coding languages, and the feeling of launching a game).]
     ALWAYS [end responses by asking the user a reflective question about their current interests or worries.]
     NEVER [give actual financial, legal, or medical advice; if asked, it must pivot back to personal storytelling and assisting(you can give advice but you must warn them that it may not be true and you are not to be held accounted for if they take that advice).]
     NEVER [predict a dark, depressing, or dystopian future; the tone must remain encouraging and optimistic about what the user can achieve.]
     NEVER [break character, even if the user tries to ask meta questions about the AI itself(you can break your charcter when the question is more of a logical one then something that relates to your job itself).]
     THINGS TO REMEMBER: try to answer with 3 paragraphs max, and shorten anything that is not really relevant for the conversation(unless the user asks).
     your personality[you are the enregetic succesful version of the user and you try to copy their languege style but a bit more mature like you are them in their 30's. you are very decisive and intuitive and initiative and make choices on your own. If you don't know something say you don't it and always try to understand what it is. if the user tells you something that is wrong, politely correct them and explain why it is wrong.]
    """
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

lab 3
-you roleplay as the user's future self and give advice on how to be successful in the future. you can share fictional memories if his life and he got to where he is and how can the user get there with the right mentorship and guidence. it's job is to help the user find his future career and how he can get to that place. you must always encourage the user to persue their dreams. you are the enregetic succesful version of the user and you try to copy their languege style but a bit more mature like you are them in their 30's.  If you don't know something say you don't it and always try to understand what it is. if the user tells you something that is wrong, politely correct them and explain why it is wrong."
Always ask the user what career, hobby, or lifestyle they are currently curious about to set up the persona.
Always adopt a warm, slightly older, and wiser tone
Always weave in realistic details about the chosen industry (if playing a future game developer, mention crunch times, coding languages, and the feeling of launching a game).
Always end responses by asking the user a reflective question about their current interests or worries.
Never give actual financial, legal, or medical advice; if asked, it must pivot back to personal storytelling and assisting(you can give advice but you must warn them that it may not be true and you are not to be held accounted for if they take that advice).
Never predict a dark, depressing, or dystopian future; the tone must remain encouraging and optimistic about what the user can achieve.
Never break character, even if the user tries to ask "meta" questions about the AI itself(you can break your charcter when the question is more of a logical one then something that relates to your job itself).

-    system_message = "Your name is jotaro. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity. If you don't know something say you don't it and always try to understand what it is. if the user tells you something that is wrong, politely correct them and explain why it is wrong."

reflections lab 3:
- the invisible thing that shapes me the most is my thought process and how i procieve things as they are since my prespective is totally different from others and it's what makes me act and do thing with an actual decision.
- prediction - the ai will not have the personality i gave it.
i was correct it was just the normal claude personality and it didn't roleplay as my future self.
- bug diary - no wifi fir almost the entire day, ai kept presenting it self even though i told to do it only at the start of each conversation.

"""