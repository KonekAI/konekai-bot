# Inspiration

Our team wanted to build a bot that connected people working from home through a responsive collaborative measure. Working in group settings can be difficult, especially given a lack of information on a given topic and deficiencies in the research process among team members. To resolve this issue, our team created Konek AI. 

Konek AI is a performative educational slack bot that was designed to enhance user collaboration and minimize research lag with a more streamlined approach.

---
# What it does

When the Konek AI bot is downloaded into a Slack channel, users are able to leverage the power of Open AI to refine team research. Users can activate and interact with the bot in channels and group chats in Slack via the slash command.

### **The ```/ai-qna``` command**
When the user types in ```/ai-qna <question>``` into the text box, they can ask our bot ANYTHING. Our bot will utilize the Ada engine from OpenAI and rapidly formulate an answer. Then the slack bot will print the response to the current user channel in the following format:
```
/ai-qna who is the prime minister of Canada
```
Slack bot will respond:
```
Q: who is the prime minister of Canada
A: Justin Trudeau.
```



###  **The ```/wiki-``` command series**
With this series of commands, the user can ask Konek AI to learn a specific Wikipedia article and directly ask Konek AI questions related to the topics within the article. To achieve this, the bot utilizes both the OpenAI and the Wikipedia python API. There are four /wiki commands in total, here is how to use them:



**The /wiki-read command**

The ```/wiki-read <article_title>``` command tells the bot to read a specific Wikipedia article and stores that article as baseline information for future queries.
```
/wiki-read Javascript
```
```
I have read the wiki article Javascript, feel free to ask me anything via /wiki-qna! (use /wiki-forget once you are done with this article)
```
(The bot will only remember one article at a time, so every time ```/wiki-read <a_different_article>``` is used, the bot will automatically forget the previous article)

- If users use this command in a slack channel the bot is invited in, the bot will display the responses in that channel for everyone to view. Otherwise, the bot will display the response in the user's direct message.
- If the user did not give any article name, the bot will remind the user through direct message:
```
	Sorry, you did not give me an article name. You can write the name after the command, for example: /wiki-article Java(programming language)
```
- If the user did not give a valid article name (Yes, the bot can check whether or not the article exists in the Wikipedia database or not!), the bot will remind the user through direct message:
```
		The article you gave me does not exist on Wikipedia, please enter a valid article title
```



**The /wiki-qna command**

The ```/wiki-qna <question>``` command allows users to ask specific questions about the Wikipedia article the bot is currently reading. It works similarly with ```/ai-qna <question>```.

Example (assuming user already told the bot ```/wiki-read Ruby programming language``` ):
``` 
/wiki-qna who created Ruby
```
```
Q: who created Ruby
A: According to this article about Ruby programming language... Yukihiro Matsumoto.
```



 **The /wiki-article command**

The ```/wiki-article``` command shows the user the current article the bot is reading via direct message.



**The /wiki-forget command**

The ```/wiki-forget``` command tells the bot to forget the article it is currently reading. Simply giving slack bot another article to read (via /wiki-read) will achieve the same effect. But it is best practice to /wiki-forget at the end of one session to clear the bot's memory.



**A hidden feature ;)** 
 ```/game-recommendation``` This command was a fun addition to the project. It randomly suggest a free online game for you and your co-worker to play and socialize.   

---
# How we built it

We built our slack bot with python, using the web client function within the slack API and its python-SDK. The web server was built in Flask, we connected local hosts to ngrok to create a public server which allowed us to connect to the slack API during development. When the project is finalized, we used Heroku to host our bot.

We developed modulated functionalities that connect and send requests to OpenAI and Wikipedia python API. These modules utilize external API to format Wikipedia texts, validate articles, and ask Ada Engin questions. Due to this modular layout, the bot can easily call on these functionalities when needed.  

Our front end was built with a Javascript framework (ReactJS), designed with Figma and Canva, integrated and styled with CSS, React-Bootstrap/React-Bootstrap icons and HTML and finally, hosted on Heroku. 

---

# Challenges we ran into

The collaborative measures given the time constraints are always difficult to manage. Every person on our team had a different vision coming into this hackathon for a project they wanted to create. Throughout designing our app, we would have frequent meetings to ensure we were not only collectively aligned, but that our end goals were mutual; we had a challenging time solidifying a concept that represented the nature of our mutual interests. However, we were able to finalize an idea and work towards engineering a viable product. Our team sourced and ultimately decided that we would split our team in half to divide and conquer our tasks (Frontend and Backend). 

For our Backend tasks, the most challenging pieces were connecting all the moving parts: integrating the bot with Slack, incorporating Open AI and Wikipedia into a cohesive, responsive product for users to actively utilize in their group messages or channels. 

For our Frontend tasks, we struggled to convert our Figma design into usable code. We designed our final product only to realize that we not only designed it incorrectly, but  we also weren't able to copy and paste our CSS code into our components. Causing us to use alternative resources such as Canva to make our CSS features from scratch, save those features as png/jpeg file(s), and, crop and tailor it to our web pages' needs. To achieve the design and style we were envisioning, we predicted it would take us four hours to complete the front end, when in actuality, it took us the entire duration of the competition. 

---
# Accomplishments that we're proud of

Despite the challenges that we faced during this competition, we were able to create a product that not only works, but also tailors itself to the users' needs. Even though we all had and continue to envision different end products, we finished this hackathon achieving some of our stretch goals in both the front end and backend.

Our team successfully created a gorgeous design and implemented a challenging AI that was new to all of us. Additionally, our team organized, documented, regularly and clearly communicated our needs and collaborated on a mutual vision that was best for the theme of this hackathon. We utilized tools (e.g., frameworks, third party API's, design tools, Agile, etc. ) that were new to all of us. While exposure to different coding styles, personalities, and methods of collaboration were hurdles we overcame, we created a product we're all proud of. 

---
# What we learned

As a group, we learned that building for an MVP rather than ambitiously trying to create a more complex application makes the development process easier.  Given so many different opportunities to incorporate various features, sticking to a relatively simple idea and building off of it to reach stretch goals for our team allowed us to finish a product from scratch within 24 hours. The phrase, "keep it simple" holds true for our team, and allowed us to supplement our idea further by dividing our product into digestible pieces.

By sizing smaller tasks throughout the day, we were able to learn in more manageable chunks of time. Given the amount of tasks we assigned the frontend and backend, we absorbed so much during this hackathon.  

---
# What's next for Konek|AI

Konek|AI can have purposeful usage in higher-level scanning, reporting, and interactive/collaborative means. From enhancing the academic research process ( Konek|AI could aid multiple medical researchers at once by scanning literature and responding accurately in group settings) to creating an interactive study session for a user to digest exhausting dense material. 

Our immediate next step is to gain slack's approval so we can publically distribute our app to remote slack workspaces. With that, Konek|AI will become more accessible and versatile. It also allows us to gather information regarding the app's performance in a wide range of environments which will help future modifications and improvements. Given the current state of the world, Konek|AI can help bridge the digital divide and elevate productivity with a focus on teamwork.

### File Management
- README.md 
- .gitignore 
- Procfile (Heroku setup)
- runtime.txt (Heroku setup)
- requirements.txt (Dependencies - Heroku setup)
- wiki_article.txt (Temperary file to store wiki article title) 
- slackBot.py (Slack bot logic)
- openAI.py (Heroku setup)
- wsgi.py (Heroku setup)
