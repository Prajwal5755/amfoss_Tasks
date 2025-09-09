import discord
from discord.ext import commands
import asyncio
import re
import os
from dotenv import load_dotenv

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    orientation_channel = discord.utils.get(guild.text_channels, name="orientation")
    if orientation_channel:
        await orientation_channel.send(f"Welcome to the server, {member.mention}! Please check out the #rules channel and introduce yourself.")
    role = discord.utils.get(guild.roles, name="Aspiring Hero")
    if role:
        await member.add_roles(role)
        await member.send(f"Hi {member.name}, you've been given the 'Aspiring Hero' role! Feel free to ask if you have any questions.")

def contains_harmful_content(content):
    harmful_keywords = ["menacing threats"]
    return any(keyword in content.lower() for keyword in harmful_keywords)

def contains_url(content):
    url_pattern = re.compile(r'(https?://\S+|www\.\S+)')
    return bool(url_pattern.search(content) or "suspicious link" in content.lower())

def contains_spam(content):
    spam_keywords = ["villainous spam"]
    return any(keyword in content.lower() for keyword in spam_keywords)

def contains_offtopic_content(content):
    offtopic_keywords = ["off-topic disruption"]
    return any(keyword in content.lower() for keyword in offtopic_keywords)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if contains_harmful_content(message.content):
        await message.delete()
        await message.author.send(f"{message.author.mention}, your message was removed due to harmful content. Please adhere to the community guidelines.")
    elif contains_url(message.content):
        await message.delete()
        await message.author.send(f"{message.author.mention}, posting links is not allowed in this server.")
    elif contains_spam(message.content):
        await message.delete()
        await message.author.send(f"{message.author.mention}, your message was removed due to spam content. Please avoid spamming.")
    elif contains_offtopic_content(message.content):
        await message.delete()
        await message.author.send(f"{message.author.mention}, your message was removed for being off-topic. Please stay on topic.")
    
    await bot.process_commands(message)
@bot.command()
@commands.has_any_role("Admin","Faculty")
async def bugle(ctx,*,announcement):
    channel = discord.utils.get(ctx.guild.text_channels, name="announcement")
    if channel:
        msg = await channel.send(announcement)
        async def delayed_delete(message):
            await asyncio.sleep(86400)
            pins = await channel.pins()
            if message.id not in [pin_msg.id for pin_msg in pins]:
                await msg.delete()
        bot.loop.create_task(delayed_delete(msg))
    else:
        await ctx.send("Announcements channel not found.")

@bot.command()
@commands.has_any_role("Admin","Aspiring Hero")
async def wisdom(ctx,topics,member:discord.Member=None):
    responses={
        "rules":"1. Be respectful to all members.\n2. No spamming or advertising.\n3. Keep content relevant to the channel topics.\n4. Follow Discord's community guidelines.",
        "resources":"1. Discord's Official Guide: https://discordpy.readthedocs.io/en/stable/#manuals\n2. Bot craetion: https://discord.com/developers/applications\n3. YouTube Tutorials: Search for 'Discord Server Management'.",# resources that i have used to learn discord bot includes command line asyncio etc
        "contact":"For any issues, please contact the server admin or moderators via direct message or email at prajwalgn614@gmail.com."
    }
    response = responses.get(topics.lower(), "Sorry, I don't have information on that topic. Please choose from 'rules', 'resources', or 'contact'.")
    if member is None:
        member = ctx.author
    channel = discord.utils.get(ctx.guild.text_channels,name="queries")
    if channel:
       if topics.lower() in responses:
           await channel.send(f"{member.mention},Your query:{topics}\n{response}")
    else:
        await ctx.send("Queries channel not found.")

    


bot.run(TOKEN)
