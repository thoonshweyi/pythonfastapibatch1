# Chat Log & Keep History
from openai import OpenAI
client = OpenAI(
     api_key = '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'
)

def getuserinput():
     return input("User: ").strip()

def getbotresponse(chatlogs):
     try:
          completion = client.chat.completions.create(
               model="gpt-3.5-turbo",
               store=False,
               messages= chatlogs,
               temperature= 1 # .5 (0 to 2)
               )
          return completion.choices[0].message.content
     except Exception as e:
          print(f"Error Found : {e}")
          return "Sorry, something went wrong. Please try again."

def chat():
     chatlogs = []
     print("Start Chatting with the bot (type 'exit' to stop app!)")

     while True:
          userinput = getuserinput()

          if userinput.lower() == 'exit':
               break

          chatlogs.append({"role": "user","content":userinput})


          botresponse = getbotresponse(chatlogs)
          chatlogs.append({"role": "assistant","content":botresponse})
          print(f"ChatAI: {botresponse}")
     
chat()

# 25CB

# Start Chatting with the bot (type 'exit' to stop app!)
# User: How to learn javascript?
# ChatAI: Here are some tips for learning JavaScript:

# 1. Start by understanding the basics: Learn about variables, data types, operators, control structures, functions, and objects.

# 2. Practice coding: The best way to learn JavaScript is by practicing coding. Start with simple exercises and gradually move on to more complex tasks.

# 3. Take online courses: There are many online resources available that offer JavaScript courses for beginners. Websites like Codecademy, Udemy, and Coursera offer comprehensive courses on JavaScript.

# 4. Read books: There are many books available on JavaScript that can help you understand the language better. Some recommended books include "Eloquent JavaScript" by Marijn Haverbeke and "You Don't Know JS" series by Kyle Simpson.

# 5. Join coding communities: Join online coding communities like Stack Overflow, GitHub, and Reddit to connect with other programmers and get help with your coding questions.

# 6. Build projects: One of the best ways to learn JavaScript is by building projects. Start with simple projects like a to-do list or a weather app, and gradually work your way up to more complex projects.

# 7. Attend workshops and meetups: Attend JavaScript workshops and meetups in your area to network with other developers and learn from experts in the field.

# 8. Stay updated: JavaScript is constantly evolving, so it's important to stay updated on the latest trends and technologies in the language. Follow blogs, newsletters, and social media accounts related to JavaScript to stay informed.

# Remember that learning JavaScript takes time and practice, so be patient with yourself and keep coding!
# User: When did it developed?
# ChatAI: JavaScript was developed in 1995 by Netscape Communications Corporation. It was originally called LiveScript and later renamed to JavaScript to capitalize on the popularity of Java at the time. JavaScript quickly gained popularity as a client-side scripting language for web development due to its ability to create interactive and dynamic websites.
# User: exit
