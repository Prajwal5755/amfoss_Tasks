```
WRITEUP FOR BOT
```

```
First I visited discords developers site their i have created application and follwed by i created a bot. After that i have given certain permissions to bot
```


I have created separate environment for bot known as bot-env using 
```
python3 -m venv bot-env
```
and I have installed discord.py library there

```
Here I have initialised intents regarding message reading and handling funtions regarding members for example( intents.message_content=TRUE)  it works only when i have given permission to bot in developers website. Intents refers to defining events like kind of defining intents
```

```
And for confidentiality of my token I have stored my bot token in separate .env file which i cannot share here. .env file allows key value format from dotenv library i am importing load_dotenv() funtion used to read token.env file. And os is used to access environment variable, getenv() used to retrieve the value fof key
```

```
asyncio is a library where we can use async for functions which we want to multitasking and await inside function for functionalities inside function. This allows multitasing of bot for example if new member is joining and also someone put offensive message it handle both asyncronisely like not blocking 2 functions.
```

```
@bot.event is a  event listner and guild is a server object utils have all list of members as an example
```

```
Command line here i have used ! as prefix it can be anything ! initiate command ctx is current context and * is used to get full message as a single string 
```
Refferances
```
discord.py
youtube
Stack Overflow
```




