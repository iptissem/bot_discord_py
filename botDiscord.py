import discord 
from discord.ext import commands
from datetime import datetime, timezone
import asyncio
from class_.historique import historique_commandes
from class_.file import queue
from hashmap_data import Hashmap
import tree

intents = discord.Intents.all()
History = historique_commandes()
History_queue = queue("Start")
historique_utilisateurs = Hashmap(100)
client = commands.Bot(command_prefix="!", intents = intents)

@client.event
async def on_ready():
    print(f'Bot connecté en tant que {client.user.name}')


#Création question QUIZ
questions = [
    {
        'question': 'Quelle anime est le plus regardé au monde en 2022 ?',
        'options': ['Attaque des Titans', 'Naruto', 'Dragon Ball Z', 'Kimestu No Yaiba'],
        'answer': 'Kimestu No Yaiba'
    },
    {
        'question': '"Attrapez-les tous" est le slogan de : ',
        'options': ['Naruto', 'Pokemon', 'One piece', 'Bleach'],
        'answer': 'Pokemon'
    },
     {
        'question': 'Je souhaite créer un monstre ancestrale : Jûbi, qui-suis-je ?',
        'options': ['San Goku', 'Obito Uchiwa', 'Madara Uchiwa', 'L'],
        'answer': 'Madara Uchiwa'
    },
     {
        'question': 'A qui devais appartenir le "One for all" de base ?',
        'options': ['Shoto', 'Deku', 'Mirio', 'Redriot'],
        'answer': 'Mirio'
    },
   {
    'question': 'Qui est le bras droit de Naruto 7ème du nom ?',
    'options': ['Hinata', 'Il l a perdu contre Sasuke !', 'Shikamaru', 'Gaara'],
    'answer': 'Shikamaru'
   },
     {
        'question': 'Quelle Lune démoniaque Tanjiro s"est battu en premier ?',
        'options': ['Akaza', 'Gon', 'Rui', 'Muzan'],
        'answer': 'Rui'
    },
]
intro_message = " ❀ \n\n**Bienvenue au quiz {username} !** \n\n Ce quiz va permettre de savoir si tu es un vrai passioné d'animé ou non ! \n\n➣ ɪɴғᴏʀᴍᴀᴛɪᴏɴs ᴅᴇ ʙᴀsᴇ\n     - **6 questions** il y aura.\n     - Tu as **30 secondes** pour répondre.\n     - ***!exit*** : quitter la partie en cours.\n\n ➣Tu es prêts ? **!ok** pour commencer ! \n\n Bon courage :D !\n\n ❀"
quiz_started = False


@client.command()
async def quiz(ctx):
    global quiz_started
    global quiz_starter_id
    

    if not quiz_started:
        await ctx.send(intro_message.format(username=ctx.author.name))
        quiz_started = True
        quiz_starter_id = ctx.author.id
        
    else:
        await ctx.send("Le quiz est déjà en cours. Répondez aux questions en cours.")


@client.command()
async def ok(ctx):
    global quiz_started
    global quiz_starter_id 

    if quiz_started:
        correct_answers = 0
        incorrect_answers = 0
        if ctx.author.id != quiz_starter_id:
           await ctx.send("Tu n'as pas à répondre au quiz des autres !")
           return

        for question in questions:
            if ctx.prefix + 'exit' in question['options']:
                await ctx.send("Vous avez quitté le quiz.")
                quiz_started = False
                return

            # Envoie la question
            question_message = f"{question['question']}\n\n"
            for i, option in enumerate(question['options']):
                question_message += f"{i+1}. {option}\n"
            await ctx.send(question_message)

            # Fonction pour vérifier la réponse
            def check_answer(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                # Attends la réponse de l'utilisateur pendant 30 secondes
                user_answer = await client.wait_for('message', check=check_answer, timeout=30.0)

                # Vérifie si l'utilisateur a tapé !exit
                if user_answer.content.lower() == ctx.prefix + 'exit':
                    await ctx.send("**Vous avez quitté le quiz :cry: **\n\n")
                    result_message = f"Voici vos résultats :\nBonnes réponses : {correct_answers}\nMauvaises réponses : {incorrect_answers}\n\n"
                    await ctx.send(result_message)   
                    quiz_started = False
                    return

                # Vérifie si la réponse est correcte
                if int(user_answer.content) == question['options'].index(question['answer']) + 1:
                    await ctx.send("**Bonne réponse ! :man_dancing: ** ❀ \n\n")
                    correct_answers += 1
                else:
                    await ctx.send(f"**Raté ! :cry:** C'était : {question['answer']} ❀  \n\n ")
                    incorrect_answers += 1
            except asyncio.TimeoutError:
               
                await ctx.send("** Trop tard :stuck_out_tongue: !**❀ \n\n")


        # Affiche les résultats
        
        await ctx.send("** ❀ \n\nQuiz terminé :star2: !**\n\n")
        if correct_answers > 3:
         result_message = f"**VICTOIRE**  Vous avez {correct_answers} bonnes réponses, bravo champion !\n\n ❀"
        else:
         result_message = f"**DEFAITE** ! Vous avez {correct_answers} bonnes réponses, reviens quand tu seras plus fort ! \n\n ❀"
        await ctx.send(result_message)

        quiz_started = False

    else:
        await ctx.send("Le quiz est déjà en cours. Répondez aux questions en cours.")


#Création CALCULETTE

@client.command()
async def calcul(ctx):
    await ctx.send("❀ \n\nCoucou !\n\nJe suis **tellement intelligent** que je pourrais résoudre tous vos calculs :smile:")
    await ctx.send("Entrez donc une expression mathématique ! : ")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        expression = await client.wait_for('message', check=check, timeout=30.0)
        expression = expression.content

        try:
            resultat = eval(expression)
            await ctx.send("Trop facile ! C'est : **{}** :yum:".format(resultat))
        except (SyntaxError, NameError):
            await ctx.send("Expression invalide :cry:  Veuillez réessayer.")

    except asyncio.TimeoutError:
        await ctx.send("Temps écoulé... Veuillez réessayer.")

#Création INFO USER 
user_info = [
    "Ton temps sur le serveur",
    "Ton compte à été créer le :",
    "Ton rôle",
    "Tu es en mode : ",
    "Ton surnom est : ",
    "Liste des serveurs communs"
]

@client.command()
async def info(ctx, *, arg=""):
    if not arg:
        await ctx.send("**Bienvenue, bienvenue !**\n\n Je connais pleins de choses sur toi ! *Même des choses que tu ne sais probalement pas :smiling_imp:*\n\n || Tapes`!info plus` pour voir par toi même ! Ne t'arrêtes pas jusqu'à ce que je déclare forfait ||")
    elif arg.lower().startswith("plus"):
        if len(user_info) > 0:
            next_info = user_info.pop(0)
            await ctx.send(f"{next_info} : {await get_user_info(ctx.author, next_info, ctx)}")
        else:
            await ctx.send("*Oups* Je suis à cours...\n\n ||Plus pour longtemps !||")


async def get_user_info(user, info):
    if info == "Ton temps sur le serveur":
        now = datetime.now(timezone.utc)
        joined_at = user.joined_at.astimezone(timezone.utc)
        return str(now - joined_at)
    elif info == "Ton compte à été créer le :":
        return user.created_at.strftime("%d/%m/%Y")
    elif info == "Ton rôle":
        roles = [role.name for role in user.roles]
        return ', '.join(roles)
    elif info == "Tu es en mode : ":
        return str(user.status)
    elif info == "Ton surnom est : ":
        return str(user.nick)
    elif info == "Liste des serveurs communs":
        shared_servers = [guild.name for guild in client.guilds if user in guild.members]
        return '\n'.join(shared_servers)
    else:
        return "Information inconnue"

async def do_history(ctx):
   while History_queue.first_node != None:
      rep = History_queue.pop()
      await ctx.channel.send(rep)

#Supression commande avec !del    
@client.command(name="del")
async def delete(ctx):
    await ctx.channel.purge(limit=10)
    History_queue.append("!del")

#Affichage de l'historique
@client.command(name="full_history")
async def full_history(ctx):
   all_commands = History.get_all_commands()
   await ctx.channel.send(all_commands)
   History_queue.append("full_history")

#Affichage dernière commande
@client.command(name="last_command")
async def last_command(ctx):
   last_cmd = History.get_last_command()
   await ctx.channel.send(last_cmd)
   History_queue.append("!last_command")

#Message bienvenue 
@client.event
async def on_member_join(member):
    general_channel = client.get_channel(977137496720826368)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)


@client.event
async def on_message(message):
  if message.author == client.user:
    return   

  if message.content.startswith("hello"):
    await message.channel.send("hello")

  await client.process_commands(message)

# Commande clear
@client.command(name="clear_command")
async def clear_command(ctx):
    History.clear()
    History.add_command("!clear_command")
    add_history_user(ctx.author.id, "!clear_command")

# ajout de la commande à l'user
def add_history_user(id_utilisateur, commande):
    if historique_utilisateurs.get(id_utilisateur) is None:
        historique_utilisateurs.append(id_utilisateur, [commande])
    else:
        historique_utilisateurs.append(id_utilisateur, historique_utilisateurs.get(id_utilisateur) + [commande])

# Sauvegarde les données dans un fichier json
@client.event
async def on_disconnect():
    await data_save(historique_utilisateurs)  # Sauvegarder les données dans le fichier historique.json avant la déconnexion

async def data_load(historique_utilisateurs):
    try:
        
        historique_utilisateurs.charger_donnees('historique.json')  # Appeler la fonction de chargement de la classe Hashmap

    except Exception as e:
        print(f"Une erreur s'est produite lors du chargement des données : {e}")

async def data_save(historique_utilisateurs):
    try:
        
        historique_utilisateurs.sauvegarder_donnees('historique.json')  # Appeler la fonction de sauvegarde de la classe Hashmap

    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde des données : {e}")

async def save_per():
    try:
        while True:
            await data_save(historique_utilisateurs)  # Appeler la fonction de sauvegarde périodiquement

            # Attendre 1 heure avant la prochaine sauvegarde
            await asyncio.sleep(5)
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde périodique des données : {e}")


# Commande historique
@client.command()
async def historique(ctx):
    historique = historique_utilisateurs.get(ctx.author.id)
    if historique is None:
        await ctx.send("Cette commande n'a pas été utilisé !")
    else:
        message = "Voici votre historique de commandes : \n\n"
        for commande in historique:
            message += str(commande) + "\n"
        await ctx.send(message)

#tree
client.discussion = tree.DiscussionSystem()

@client.command()
async def discussion(ctx):
    client.discussion.reset_discussion()
    await ctx.send(client.discussion.get_response())

@client.command()
async def rep(ctx, response):
    client.discussion.process_answer(response)
    await ctx.send(client.discussion.get_response())

# Commande "reset"
@client.command()
async def reset(ctx):
    client.discussion.reset_discussion()
    await ctx.send("J'ai tout oublié !")

# Commande "speak_about"
@client.command()
async def speak_about(ctx, topic):
    response = client.discussion.speak_about(topic)
    await ctx.send(response)


client.run("TOKEN")

