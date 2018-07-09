import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    try:
        user = await client.get_user_info('446237795342745600')
        channel = await  client.start_private_message(user)
        # tip_channel = client.get_channel('446587631749562388')
        # tmp = await client.send_message(tip_channel, './mining 10')
        hogemi = await client.get_user_info('446234539681906689')
        hogemi_ch = await  client.start_private_message(hogemi)
        # client.g
        tmp = await client.send_message(hogemi_ch, './tip random 10')
        tmp = await client.send_message(channel, './tip random 10')
    finally:
        client.logout()
        exit(0)

client.run("")