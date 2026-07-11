# Chat Log & Keep History
from openai import OpenAI
client = OpenAI(
     api_key = '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'
)

chatlogs = []
while True:
     userinput = input("Enter your idea: ")

     if userinput.lower() == 'exit':
          break

     chatlogs.append({"role": "user","content":userinput})

     completion = client.chat.completions.create(
     model="gpt-3.5-turbo",
     store=False,
     messages= chatlogs,
     temperature= 1 # .5 (0 to 2)
     )

     botresponse = completion.choices[0].message.content
     chatlogs.append({"role": "assistant","content":botresponse})
     print(f"ChatAI: {botresponse}")


# Enter your idea: How to install git on ubuntu?
# ChatAI: To install Git on Ubuntu, you can follow these steps:

# 1. Open a terminal window by pressing Ctrl+Alt+T.

# 2. Update the package lists for upgrades and new package installations by running the following command:

# ```
# sudo apt update
# ```

# 3. Install Git by running the following command:

# ```
# sudo apt install git
# ```

# 4. Verify the installation by checking the Git version:

# ```
# git --version
# ```

# You should see the installed Git version displayed in the terminal.

# Git is now successfully installed on your Ubuntu system.
# Enter your idea: How to check version?
# ChatAI: To check the version of Git that is installed on your Ubuntu system, you can run the following command in the terminal:

# ```
# git --version
# ```

# After running this command, you will see the installed Git version displayed in the terminal. This command will output the Git version number, indicating that Git is installed on your system and which version is currently being used.
# Enter your idea: How to install python on window?
# ChatAI: To install Python on a Windows operating system, you can follow these steps:

# 1. Download the Python installer:
#    - Go to the official Python website: https://www.python.org/downloads/
#    - Click on the "Download" button for the latest version of Python. You can choose between Python 3.x and Python 2.x, with Python 3.x being the recommended version.
#    - Scroll down and select the Windows installer that matches your system architecture (32-bit or 64-bit).

# 2. Run the Python installer:
#    - Once the installer file is downloaded, double-click on it to run the installer.
#    - Check the box that says "Add Python x.x to PATH" during the installation process. This will automatically set up the PATH environment variable so that you can run Python from the command line.
#    - Click "Install Now" to start the installation process.

# 3. Verify the installation:
#    - Open the Command Prompt by pressing Win + R, typing "cmd" and hitting Enter.
#    - Type the following command in the Command Prompt to check if Python is installed:
#      ```
#      python --version
#      ```
#    - If Python is installed correctly, the command will display the installed Python version.

# Python is now successfully installed on your Windows system. You can start writing and running Python scripts on your computer.
# Enter your idea: How to check version?
# ChatAI: To check the version of Python that is installed on your Windows system, you can follow these steps:

# 1. Open the Command Prompt by pressing Win + R, typing "cmd" and hitting Enter.

# 2. Type the following command in the Command Prompt to check the installed Python version:
# ```
# python --version
# ```

# Or, you can also use the following command to check the Python version:
# ```
# python -V
# ```

# 3. If Python is installed correctly, the command will display the installed Python version.

# This way you can easily check the version of Python installed on your Windows system using the Command Prompt.
# Enter your idea: exist










# What is the system role?
# The system message is a special instruction that you give to the AI before the conversation starts. It sets the tone, personality, and behavior of the assistant.

# You only use it once, usually as the first message in the messages list.

#  Summary of Roles in Human Context

# Marketing Manager = system
# Gives clear instructions to employees on how to talk to customers, what to promote, and how to behave.

# Customer Service Representative = assistant
# The person who directly talks to customers, answers questions, and follows the manager’s instructions.

# Customer = user
# The person who walks into the store and asks questions, gives feedback, or complains.



#  What the system role does:
# ✅ 1. Sets the Assistant's Behavior
# The system tells the assistant how to act, what tone to use, and what rules to follow.

# Think of it as giving the assistant a job description or code of conduct before it starts talking.

# ✅ 2. Defines the Assistant's Personality or Role
# For example:

# Be a polite customer service agent

# Be a strict grammar teacher

# Be a funny pirate

# Only speak in French

# ➡️ Whatever you write in the system message becomes the mindset of the assistant.

# ✅ 3. Guides Conversation Style or Language
# It can define:

# Formal or casual tone

# How long or short the answers should be

# Whether to include emojis, markdown, or technical terms

# ✅ 4. Controls the Assistant's Knowledge or Limits
# You can instruct it to:

# Avoid certain topics

# Not give legal or medical advice

# Say “I don’t know” if unsure