import time
import random

#create the Shop class
class Shop:
    def __init__(self, name):
        self.name = name

#welcome flag and shop name input
print("Welcome to the ttrpg shop generator!")
time.sleep(1)
input_name = input("Enter a name for this shop: ")
shop = Shop(input_name)

#shop_type definition
print(f"Let's make {shop.name}. What do they sell or offer?")

# Create a dictionary of shop types and their descriptions
shop_types = {
    "weapon": "A shop selling various types of weapons",
    "armor": "A shop selling various types of armor",
    "clothing": "A shop selling various types of clothing",
    "potion": "A shop selling magical potions and elixirs",
    "healer": "A shop offering medical services and healing items",
    "magic items": "A shop selling magical items and artifacts",
    "animal tack": "A shop selling equipment for animals and mounts",
    "guild hall": "A meeting place for a guild or organization",
    "general store": "A shop selling a variety of everyday items",
    "smith": "A shop specializing in metalworking and blacksmithing",
    "bookseller": "A shop that sells books, scrolls, and other written materials.",
    "artisan shop": "A shop that specializes in handmade goods, such as jewelry, pottery, or woodworking.",
    "Curiosity Shop": "A shop that sells odd and unusual items, such as exotic animals, strange artifacts, and rare magical items.",
    "Pawn Shop": "A shop where adventurers can sell or trade their old items for new ones.",
    "Hireling Agency": "A place where adventurers can hire NPCs to accompany them on their quests."
}

# Show the options to the user
print("Select a shop type:")
for i, shop_type in enumerate(shop_types):
    print(f"{i + 1}. {shop_type.capitalize()} - {shop_types[shop_type]}")
time.sleep(1)

# Ask the user to input a number
while True:
    selection = input("Enter the number of the shop type you want to visit: ")
    
    # Check if the input is valid
    if selection.isdigit() and int(selection) in range(1, len(shop_types) + 1):
        # Print the selected shop type's description
        selected_shop_type = list(shop_types.keys())[int(selection) - 1]
        print(f"You have selected {selected_shop_type.capitalize()} - {shop_types[selected_shop_type]}")
        break
    else:
        print("Invalid selection. Please enter a valid number.")
shop_type = shop_types[selected_shop_type]
time.sleep(1)    

# Create a dictionary of neighborhoods and their descriptions
neighborhoods = {
    "ghost town": "an abandoned town with a few remaining buildings",
    "village": "a small community with a central gathering place",
    "bustling town market": "a crowded marketplace with vendors selling various goods",
    "city bazaar": "a large marketplace with vendors selling exotic goods",
    "own building (bougie)": "a fancy building owned by the shopkeeper",
    "own building (municipal)": "a building owned by the local government",
    "outdoor area": "a stall or stand set up in a public space",
    "Market square": "a bustling marketplace in the heart of a city where merchants and vendors come to sell their wares.",
    "Dockside": "a waterfront area where ships come to port and sailors and merchants come to trade goods.",
    "Red light district": "a seedy part of town where illegal activities and vices are rampant.",
    "Temple district": "an area where religious buildings and organizations are located.",
    "Noble quarter": "a high-end neighborhood where the wealthy and influential reside.",
    "Rural village": "a small community located outside of a city.",
    "Black market": "an underground network of illegal shops and merchants that sell prohibited or hard-to-find items.",
    "Artisan district": "an area where skilled craftsmen and artisans create and sell their handmade wares.",
    "University district": "an area surrounding a center of learning.",
    "Industrial park": "a part of town where factories and manufacturing plants are located."
}

#neighborhood 
print("Now we have to get an idea of where the shop is located.")
time.sleep(1)
print("Please choose a neighborhood:")

# Print out the options for the user to choose from
for i, neighborhood in enumerate(neighborhoods):
    print(f"{i + 1}. {neighborhood}")

# Prompt the user to choose a neighborhood
while True:
    try:
        choice = int(input("Enter a number: "))
        if 1 <= choice <= len(neighborhoods):
            neighborhood = list(neighborhoods.keys())[choice - 1]
            print(f"You have chosen a {selected_shop_type} in a {neighborhood}: {neighborhoods[neighborhood]}")
            break
        else:
            print(f"Please enter a number between 1 and {len(neighborhoods)}")
    except ValueError:
        print("Please enter a valid number")
        continue
neighborhood = neighborhoods[neighborhood]
neighborhood_desc = neighborhoods.get(neighborhood, "Unknown neighborhood")
time.sleep(1)

#Shopkeeper generator
print(f"Now, let's make an NPC shopkeeper to work at {shop.name}.")
time.sleep(1)

#Dictionary of NPCs and their descriptions
shopkeepers = {
    "Craftsman": "Skilled in creating handmade goods",
    "Merchant": "Trades in various goods",
    "Haggler": "Expert in bargaining and negotiating prices",
    "Collector": "Acquires and sells rare or unique items",
    "Artisan": "Specializes in creating artistic and decorative items",
    "Curator": "Collects and sells valuable or historic items",
    "Entrepreneur": "Innovative and resourceful in starting and running a business",
    "Dealer": "Buys and sells specific types of goods, such as antiques or weapons",
    "Peddler": "Travels from place to place selling various goods",
    "Apothecary": "Expert in creating and selling medicinal remedies",
    "Alchemist": "Uses magic and science to create and sell potions and other magical items",
    "Herbalist": "Uses natural remedies and herbs to create and sell medicines",
    "Smith": "Skilled in metalworking and creating weapons and armor",
    "Tailor": "Creates and sells clothing and accessories",
    "Baker": "Creates and sells baked goods and confections",
    "Brewer": "Creates and sells alcoholic beverages",
    "Barber": "Provides haircuts and grooming services",
    "Bookseller": "Sells books, scrolls, and other written works",
    "Gardener": "Specializes in plants and gardening supplies",
    "Musician": "Creates and sells musical instruments and sheet music"
}

# Print out the options for the user to choose from
for i, shopkeeper in enumerate(shopkeepers):
    print(f"{i + 1}. {shopkeeper}")

# Prompt the user to choose a shopkeeper
while True:
    try:
        choice = int(input("Enter a number: "))
        if 1 <= choice <= len(shopkeepers):
            selected_shopkeeper = list(shopkeepers.keys())[choice - 1]
            print(f"You have chosen a {selected_shopkeeper}: {shopkeepers[selected_shopkeeper]}")
            shopkeeper = selected_shopkeeper
            break
        else:
            print(f"Please enter a number between 1 and {len(shopkeepers)}")
    except ValueError:
        print("Please enter a valid number")
time.sleep(1)

#fantasy name generator found at https://python-forum.io/thread-18779.html with minor additions
FIRST = ['A', 'Ag', 'Aga' 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
    'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has', 
    'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo', 
    'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Phra', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel', 'Sher', 
    'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Wy' 'Ya', 'Yo', 'Yyr', 'Zu']
 
SECOND = ['ate', 'ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra', 
    'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku', 
    'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak', 'ri',
    'ric', 'rin', 'rum', 'rus', 'rut', 'sax' 'sek', 'ser', 'sha', 'te' 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'tt', 'varl',
    'wain', 'wan', 'win', 'wise', 'wood', 'ya']

#roll a shopkeeper name
def shopkeeper_name():
    return random.choice(FIRST) + random.choice(SECOND)
shopkeeper_name = shopkeeper_name()

#tell the user the shopkeeper name
print(f"The Shopkeeper's name is: {shopkeeper_name}")
time.sleep(1)

# Open the file containing the roleplay devices
with open("rpd.txt", "r") as f:
    devices = f.readlines()

# Strip newline characters from the devices
devices = [d.strip() for d in devices]

# Choose a random device from the list
device = random.choice(devices)

# Print the device and ask the user if they want to roll again
print(f"Your roleplay device is: {device}")
while True:
    roll_again = input("Roll again? (y/n) ")
    if roll_again.lower() == "n":
        break
    device = random.choice(devices)
    print(f"Your new roleplay device is: {device}")

print(f"The {shopkeeper_name} is {device}!")
time.sleep(1)

print("Generating prompts...")
time.sleep(1)

class Shop_Information:
    def __init__(self, name, shop_type, neighborhood, shopkeeper, device):
        self.name = name
        self.type = self.shop_types[shop_type]
        self.description = shop_descriptions[shop_type]
        self.neighborhood = neighborhoods[neighborhood]
        self.shopkeeper = shopkeepers[shopkeeper]
        self.shopkeeper_name = shopkeep.name[shopkeeper_name()]
        self.device = device[device]
  
    def display_info(self):
        print(f"Shop Name: {self.name}")
        print(f"Shop Type: {self.shop_type}")
        print(f"Shop Type Description: {self.shop_type.description}")
        print(f"Neighborhood: {self.neighborhood}")
        print(f"Shopkeeper: {self.shopkeeper}")
        print(f"Fantasy Name: {self.shopkeeper_name}")
        print(f"Device: {self.device}")

#output for chatbot
print("prompt for chatbot:")
print(f"Write an introduction for ttrpg players that introduces them to a shop called {shop.name} located in the {neighborhood} neighborhood, {neighborhood_desc}.")
print(f"The shop is a {selected_shop_type.capitalize()} which has wares including- {shop_types[selected_shop_type]}.")
print(f"The shopkeeper is a {shopkeeper} name {shopkeeper_name} who is {device}.")
time.sleep(2)

#output for img generation
print("prompt for map img gen:")
print("ttrpg illustration player handbook fantasy rpg, topdown arial map indoor grid shop interior location")
print(f"{shop.name} is {selected_shop_type.capitalize()} - {shop_types[selected_shop_type]} located in a {neighborhood}: {neighborhood_desc}.")
time.sleep(1)
print("prompt illustration of shop img gen:")
print(f"{shop.name} is {selected_shop_type.capitalize()} - {shop_types[selected_shop_type]} located in a {neighborhood}: {neighborhood_desc} run by a {selected_shopkeeper}: {shopkeepers[selected_shopkeeper]} named {shopkeeper_name}.")
print("ttrpg illustration player handbook fantasy rpg game location shop")
time.sleep(1)
print("prompt for shopkeeper npc art img gen:")
print(f"The {selected_shopkeeper}: {shopkeepers[selected_shopkeeper]}'s name is {shopkeeper_name} who is {device}.")
print("ttrpg illustration player handbook fantasy rpg game NPC shopkeeper fantasy character art")
time.sleep(3)

#the closer
close = input("Want to exit? (y/n) ")