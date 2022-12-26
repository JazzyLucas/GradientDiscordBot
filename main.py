import os
import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

# Create a Bot instance and set the command prefix
bot = commands.Bot(command_prefix='!')
BOT_TOKEN = os.environ['BOT_TOKEN']

# Function to generate the gradient image
def generate_gradient(width, height, start_color, end_color):
  image = Image.new('RGB', (width, height))
  draw = ImageDraw.Draw(image)
  for x in range(width):
      color = tuple(int(start_color[i] + (end_color[i] - start_color[i]) * x / width) for i in range(3))
      draw.line((x, 0, x, height), fill=color)
  return image

# Command to generate and send the gradient image
@bot.command()
async def gradient(ctx, start_color: str, end_color: str):
  # Parse the start and end colors
  start_color = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
  end_color = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))

  # Generate the gradient image
  image = generate_gradient(200, 100, start_color, end_color)

  # Save the image to a file
  image.save('gradient.png')

  # Send the image file to the channel
  await ctx.send(file=discord.File('gradient.png'))

# Run the bot
bot.run('TOKEN')