import random
import time

animals = [
    "aardvark", "albatross", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon",
    "badger", "barracuda", "bat", "bear", "beaver", "bee", "bird", "bison", "boar", "butterfly", "camel",
    "caribou", "cassowary", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee",
    "chinchilla", "chough", "coati", "cobra", "cockroach", "cod", "cormorant", "coyote", "crab", "crocodile",
    "crow", "curlew", "deer", "dinosaur", "dog", "dolphin", "donkey", "dotterel", "dove", "dragonfly", "duck",
    "dugong", "dunlin", "eagle", "echidna", "eel", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish",
    "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "goat", "goose", "gorilla",
    "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring",
    "hippopotamus", "hornet", "horse", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish",
    "kangaroo", "kinkajou", "koala", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama",
    "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mink", "mongoose",
    "monkey", "moose", "mouse", "mosquito", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "ostrich",
    "otter", "owl", "oyster", "parrot", "panda", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pork",
    "pigeon", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rat", "raven",
    "reindeer", "rhinoceros", "salamander", "salmon", "sandpiper", "sardine", "seahorse", "shark", "sheep", "shrew",
    "skunk", "sloth", "snail", "snake", "spider", "squirrel", "starling", "swan", "tapir", "tarsier", "termite",
    "tiger", "toad", "turtle", "wallaby", "walrus", "wasp", "weasel", "whale", "wolf", "wolverine", "wombat", "wren",
    "yak", "zebra"
]
adjectives = [
    "adorable", "adventurous", "aggressive", "alert", "amazing", "amusing", "ancient", "angry", "annoyed", "anxious",
    "arrogant", "ashamed", "attractive", "average", "awful", "bad", "beautiful", "better", "bewildered", "black",
    "blue", "bloody", "blue-eyed", "blushing", "bored", "brainy", "brave", "breakable", "bright", "busy", "calm",
    "careful", "cautious", "charming", "cheerful", "clean", "clear", "clever", "cloudy", "clumsy", "colorful",
    "combative", "comfortable", "concerned", "condemned", "confused", "cooperative", "courageous", "crazy", "creepy",
    "crowded", "cruel", "curious", "cute", "dangerous", "dark", "dead", "defeated", "defiant", "delightful", "depressed",
    "determined", "different", "difficult", "disgusted", "distinct", "disturbed", "dizzy", "doubtful", "drab", "dull",
    "eager", "easy", "elated", "elegant", "embarrassed", "enchanting", "encouraging", "energetic", "enthusiastic",
    "envious", "evil", "excited", "expensive", "exuberant", "fair", "faithful", "famous", "fancy", "fantastic", "fierce",
    "filthy", "fine", "foolish", "fragile", "frail", "frantic", "friendly", "frightened", "funny", "gentle", "gifted",
    "glamorous", "gleaming", "glorious", "good", "gorgeous", "graceful", "grieving", "grotesque", "grumpy", "handsome",
    "happy", "healthy", "helpful", "helpless", "hilarious", "homeless", "homely", "horrible", "hungry", "hurt", "ill",
    "important", "impossible", "inexpensive", "innocent", "inquisitive", "itchy", "jealous", "jittery", "jolly",
    "joyous", "kind", "lazy", "light", "lively", "lonely", "long", "lovely", "lucky", "magnificent", "misty", "modern",
    "motionless", "muddy", "mushy", "mysterious", "nasty", "naughty", "nervous", "nice", "nutty", "obedient", "obnoxious",
    "odd", "old-fashioned", "open", "outrageous", "outstanding", "panicky", "perfect", "plain", "pleasant", "poised",
    "poor", "powerful", "precious", "prickly", "proud", "puzzled", "quaint", "real", "relieved", "repulsive", "rich",
    "scary", "selfish", "shiny", "shy", "silly", "sleepy", "smiling", "smoggy", "sore", "sparkling", "splendid",
    "spotless", "stormy", "strange", "stupid", "successful", "super", "talented", "tame", "tasty", "tender", "tense",
    "terrible", "testy", "thankful", "thoughtful", "thoughtless", "tired", "tough", "troubled", "ugliest", "ugly",
    "uninterested", "unsightly", "unusual", "upset", "uptight", "vast", "victorious", "vivacious", "wandering",
    "weary", "wicked", "wide-eyed", "wild", "witty", "worrisome", "worried", "worrisome", "wrong", "zany", "zealous"
]
def generate_name():
    print(f"{adjectives[random.randint(0, len(adjectives) - 1)]}_{animals[random.randint(0, len(animals) - 1)]}_{random.randint(100,999)}")
generate_name()
time.sleep(60)
