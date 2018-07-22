import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    try:
        # user = await client.get_user_info('446237795342745600')
        # channel = await  client.start_private_message(user)
        ura_channel = client.get_channel('465840548842831874')
        tip_channel = client.get_channel('446588000462438402')
        tmp = await client.send_message(tip_channel, './mining 10')
        # hogemi = await client.get_user_info('446234539681906689')
        # hogemi_ch = await  client.start_private_message(hogemi)
        # client.g
        tmp = await client.send_message(ura_channel, './tip random 10')
    finally:
        tmp = await client.logout()


client.run("")