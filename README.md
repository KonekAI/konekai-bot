# konekai-bot
Python Slack bot 


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



### Current Bot Commands
```/ai-qna``` Ask KONEK-AI bot a question. Any question! And behold! Witness the power of OpenAI first hand.

```/game-recommendation``` A hidden feature, suggests a social game for you and your coworkers to play!

```/wiki-read``` Give a wiki article title to the bot; the bot will read it and learn it using AI (command can be used via dm or in a channel).

```/wiki-qna``` Ask wiki any question about the article it is currently reading (see /wiki-read).

```/wiki-article``` Shows and DM you the current wiki article bot is reading.

```/wiki-forget``` Remove the wiki article stored in the bot's memory.

