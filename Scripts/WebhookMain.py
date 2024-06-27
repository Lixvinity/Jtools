import os
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = input('Enter webhook URL: ')

ateveryone = input('Do you want to @everyone?. 0 = yes, 1 = no')

if ateveryone == '0':
  ateveryone = ('@everyone')
else:
  if ateveryone == '1':
    ateveryone = ('')

embed_title = input('Enter a Title: ')
embed_color = int(input('Enter a color code: '))
thumb_image_url = input('Enter Thumbnail image URL: ')
image_url = input('Enter Image URL: ')
description = input('Please enter a description: ')
set_curl = input('Do you want to set a clickable URL? (0 = yes, 1 = no) ')

if set_curl == '0':
    set_curl = True
    curl = input('What URL do you want? ')
else:
    if set_curl == '1':
        set_curl = False
        curl = ''

webhook = DiscordWebhook(url=webhook_url)

embed = DiscordEmbed(title=embed_title, color=embed_color, content=ateveryone)
embed.set_image(url=image_url)
embed.set_thumbnail(url=thumb_image_url)
embed.set_description(description)
if set_curl:
    embed.set_url(url=curl)

webhook.add_embed(embed)
webhook.content = ateveryone
response = webhook.execute()
