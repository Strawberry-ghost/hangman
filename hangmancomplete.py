import random
print("Welcome to")
print("H A N G M A N")
print("****************************************************************")
HANGMANGRAPHICS = ['''

+_______+
 |    |
      |
      |
      |
      |
=========''','''
+_______+
 |    |
 O    |
      |
      |
      |
=========''','''

+_______+
  |   |
  O   |
  |   |
      |
      |
=========''','''

+_______+
  |   |
  O   |
 /|   |
      |
      |
=========''','''


+_______+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

+_______+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

+_______+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''

+_______+
  |   |
  O   |
 /|\  |
_/ \  |
      |
=========''','''

+_______+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''']

notRecognizedInput = False

while notRecognizedInput == False:
    category = input("Please choose a category: \n Enter \"countries\" for countries. \n Enter \"cities\" for cities. \n Enter \"animals\" for animals. \n Enter \"wildcard\" for wildcard.\n")
    if (category == 'countries' ):
        print("Category is cities.")
        notRecognizedInput = True
        words = ['united states','afghanistan','albania','algeria','andorra','angola','anguilla','antigua and barbuda','argentina',
                        'armenia','aruba','australia','austria','azerbaijan','bahamas','bahrain',
                        'bangladesh','barbados','belarus','belgium','belize','benin','bermuda','bhutan','bolivia','bosnia and herzegowina','botswana',
                        'bouvet island','brazil','brunei darussalam','bulgaria','burkina faso','burundi',
                        'cambodia','cameroon','canada','cape verde','cayman islands','central african republic',
                        'chad','chile','china','christmas island','cocos islands','colombia','comoros','congo','cook islands','costa rica','cote divoire',
                        'croatia', 'cuba','cyprus','czech republic','denmark','djibouti','dominica',
                        'dominican republic', 'east timor', 'ecuador', 'egypt','el salvador', 'equatorial guinea',
                        'eritrea','estonia','ethiopia','falkland islands','faroe islands','fiji', 'finland','france','french guiana','french polynesia',
                        'french southern territories', 'gabon', 'gambia','georgia','germany','ghana',
                        'gibraltar','greece','greenland','grenada','guadeloupe','guam','guatemala','guinea','guinea bissau','guyana','haiti','honduras',
                        'hungary','iceland','india','indonesia','iran','iraq','ireland',
                        'israel','italy','jamaica','japan','jordan','kazakhstan','kenya','kiribati','north korea','south korea'
                        'kuwait','kyrgyzstan','laos','latvia','lebanon','lesotho','liberia','libya','liechtenstein',
                        'lithuania','luxembourg','macau','macedonia','madagascar','malawi','malaysia','maldives',
                        'mali','malta','marshall islands','martinique','mauritania','mauritius','mayotte',
                        'mexico','micronesia','moldova','monaco','mongolia','montserrat','morocco','mozambique','myanmar','namibia',
                        'nauru','nepal','netherlands','netherlands antilles','new caledonia','new zealand','nicaragua',
                        'niger','nigeria', 'niue','norfolk island','northern mariana islands','norway','oman','pakistan','palau','panama',
                        'papua new guinea','paraguay','peru','philippines','pitcairn','poland','portugal','qatar','reunion','romania',
                        'russian federation','rwanda','saint kitts and nevis','saint lucia','st vincent grenadines',
                        'samoa','san marino','sao tome','saudi arabia','senegal','seychelles','sierra leone','singapore',
                        'slovakia','slovenia','solomon islands','somalia','south africa','spain','sri lanka', 'sudan','suriname',
                        'swaziland','sweden','switzerland','syrian arab republic','taiwan','tajikistan','tanzania','thailand','togo','tokelau',
                        'tonga','trinidad and tobago','tunisia','turkey','turkmenistan','tuvalu',
                        'uganda','ukraine','united arab emirates','united kingdom','uruguay',
                        'uzbekistan','vanuatu','vatican city state','venezuela', 'vietam',
                        'virgin islands','western sahara','yemen','yugoslavia', 'zaire','zambia','zimbabwe']
                
    elif (category == 'cities'):
        print("Category is cities.")
        notRecognizedInput = True
        words = ["minneapolis", "indianapolis","austin","dallas","guangzhou","rio de janeiro","manila","lagos","chonqing","istanbul","kolkata","buenos aires","karachi","dhaka","new york","cairo","osaka","beijing","mexico city","mumbai"
                         "sao paulo","shanghai","new delhi","tokyo","los angeles","moscow","st petersberg","kinshasa","tianjin","paris","shenzhen","jakarta","london","bangalore","lima","chennai","nagoya","johannesburg",
                         "bankok","hyderabad","lahore","tehran","wuhan","chengdu","dongguan","nanjing","ahmadabad","hong kong",
                         "ho chi minh city","foshan","kuala lampur","baghdad","santiago","hangzhou","rayadh","shenyang","madrid",
                         "xian","toronto","miami","pune","belo horizonte","surat","houston","singapore","philadelphia",
                         "kitakyushu","luanda","suzhou","haerbin","barcelona","atlanta","khartoum","dar es salaam",
                         "washington d c","abidjan","guadalajara","yangon","alexandria","ankara","kabul","qingdao","chittagong",
                         "monterrey","sydney","dalian","xiamen","zhengzhou","boston","melbourne","brasilia","jiddah","pheonix",
                         "jinan","montreal","shantou","medellin","fortaleza","kunming","changchun","changsha","recife",
                         "rome","zhongshan","cape town","detroit","hanoi","tel aviv","porto alegre","salvador",
                         "faisalabad","berlin","aleppo","dakar","casablanca","urumqi","taiyuan","curitiba","jaipur",
                         "shizuoka","hefei","san francisco","fuzhou","shijiazhuang","seattle","addis ababa","nanning","lucknow",
                         "busan","wenzhou","ibadan","ningbo","san diego","milan","yaounde","athens","wuxi","campinas",
                         "izmir","kanpur","mashhad","puebla","sanaa","sango domingo","douala","kiev","guatemala city","caracas","iowa city",
                         "duluth","honalulu","jerusalem","nairobi","prauge","lima","lagos","brussels","denver","nashville","monrovia"
                         "riyahdh","seoul","kuwait city","amman","benghazi","capetown","mosul","medina","beirut","stockholm",
                         "hiroshima","port au prince","volgograd","seongnam","napoli","odessa","peshawar","freetown","sendai",
                         "tripoli","tbilisi","allahabad","sofia","milan","kyoto","shiraz","rajkot","munich","gwangju","phnom penh"
                         "benin","kobe","daejon","santa cruz","barcelona","mecca","tijuana","damascus",
                         "warsaw","minsk","perth","pyongyang","omdurman","isfahen","taipei"]
	
    elif (category == 'animals'):
        print("Category is animals.")
        notRecognizedInput = True
        words = ["alpaca","albatross","alligator","anteater",
                         "aardvark","armadillo","baboon","badger","blue whale","barracuda","buffalo","bobcat","butterfly",
                         "beaver","bison","camel",
                         "caribou","capybara","chinchilla","cheetah","chameleon","caterpillar","chimpanzee",
                         "coyote","cuckoo","crocodile","dinosaur","dingo","cricket","cougar","dragonfly","elephant",
                         "falcoln","ferret","eagle","echidna","flamingo","emu","elephant seal","gnat","gazelle","gerbil",
                         "giraffe","gnu","goldfinch","goosander","giant panda","gaur","grasshopper","grouse","guinea pig",
                         "hamster","guinea fowl","hippopotamus","hedgehog","herring","hermit crab","hornet","impala","iguana"
                         "jackal","jellyfish","jerboa","kangaroo","kingfisher","kinkajou","komodo dragon","kookaburra","kouprey"
                         "lemur","lizard","llama","lobster","locust","lynx","macaque","macaw","magpie","mammoth","manatee",
                         "marmoset","marmot","meerkat","mongoose","mosquito","moose","mouse","newt","narwhal","octopus","panther",
                         "parrot","partridge","peafoul","pelican","penguin","pheasant","pidgeon","polar bear","porcupine","porpoise",
                         "prairie dog","quail","quetzal","raccoon","reindeer","raven","ram","rhinoceros","salamander","sand dollar",
                         "salmon","sardine","sea lion","shrew","sloth","squid","stegosaurus","tapir","skunk","tamarin","turkey",
                         "turtle","toucan","termite","tiger","wasp","viper","vultute","wallaby","walrus","water buffalo","waxwing",
                         "weasel","whale","wobbegong","gray wolf","wolf","wolverine","wombat","woodpecker","wren","worm","yak","zebra", "pygmy goat",
                         "rhinoceros beetle","hercules beetle","seven spotted ladybug","ultramarine flycatcher","shrimp","great white shark",
                         "sea squirt","peregrine falcon","sea star","gecko","tortoise","rabbit","canine","feline","monitor lizard",
                         "white headed dwarf gecko","kiwi","okarito kiwi","hummingbird","rooster","chicken","great horned owl","eastern barn owl",
                         "sea cucumber","moth","rhea","axolotl","poison dart frog","red eyed tree frog","manta ray","sawfish","dogfish shark","chimaera",
                         "catfish","goldfish","guppy","beta fish","sturgeon","swordfish","seahorse","lamprey","chinchilla","chipmunk","squirrel",
                         "gopher","pygmy jerboa","flying squirrel","porcupine","pika","brown bear","sun bear","monk seal","red panda","hyena",
                         "jackal","artic fox","linsang","brazilian tapir","orangutan","flying lemur","bonobo","gibbon","mangabey","human","langur"]
        
    elif (category == 'wildcard'):
        print("Category is wildcard.")
        notRecognizedInput = True
        words = ["spatula","anatomy","programming","exorcist","jazz","critique","faux","brunette","klutz","genre","bon appetit",
                         "fuzzy","yummy","rhythm","xylophone","muscle","gluteus maximus","xenophobia","euphemism","bugaboo","triangulation",
                         "coronation","lymph","scapula","memento","numbskull","phlegm","haphazard","bagpipes","banjo","clarinet","oboe","pajamas",
                         "tsunami","gazebo","oxygen","xenon","nitrogen","zombie","polka","mystify","mystery","wildebeest","microwave","nightclub",
                         "gamma ray","jiujitsu","taekwondo","kimchi","pneumonia","witchcraft","voyeurism","pixel","jukebox","matrix","alzheimers disease",
                         "apple strudel","cobalt","blitz","dachshund","doppelganger","fahrenheit","frankfurter","algebra","alcohol","mattress","prosciutto",
                         "peperoni","latte macchiato","marzipan","tortellini","archipelago","masquerade","canoe","paparazzi","barbecue","burrito","filibuster",
                         "enchilada","habanero pepper","hurricane","renegade","teriyaki","haiku","typhoon","hanbok","tycoon","brainwashing","ketchup",
                         "ginseng","rickshaw","qipao","oolang tea","lychee","feng shui","mandala","avatar","basmati rice","rendezvous","bacteriophage",
                         "stratosphere","pickaxe","lecithin","cheese blintz","kosher","moccasin","slaughter","schadenfreude","revolution","destruction",
                         "high fructose corn syrup","steamrolled","turboprop","vermilion","ambidextrous","animus","antediluvian","clandestine","claustrophobia",
                         "commodious","database","caffinated", "decahedron", "encephalitis","hinduism","jazzy","jeopardy","leftovers","meringue","mercenary",
                         "samurai","superstore","blender","food processor","supernova","talcum powder","thymus","toboggan","tiddlywinks","muesli","mynah bird",
                         "mystique","mythical","pterodactyl","psychoanalyse", "psychiatrist","microbiologist","organic chemist","aerospace engineer","utilitarianism",
			 "antidisestablishmentarianism","antiskepticism","zeitgeist","zodiac sign","angora sweater","antiplaque mouthwash","battery charger",
			 "broadband internet","clock radio","crocheted doily","flannel bedsheets","framed poster","gardening gloves","glassware","handwoven wool blanket",
			 "sixteen milimeter film","kitty litter","knitting needles","led flashlight","mousepad","postage stamp","rubbing alcohol","sewing machine",
			 "tackle box","utility drawer","vacuum cleaner","warm fuzzy blanket","wireless headphones","yellow sundress","cake decorator",
			 "correctional officer","executive secretary","graphic designer","intelligence specialist","private chef","mall cop","traffic cop",
			 "wedding planner","yoga instructor","backup singer","casual friend","american citizens","insured motorists","responsible young adult",
			 "jail inmate","supreme court justice","urban explorer","airplane ticket","a trip overseas","insurance estimate","adhesive tape", 
	                 "alkaline batteries","balance beam","best selling novel","birthday cake","bobby pin","cash advance","crash test dummy","daily planner",
			 "designer handbag","dog biscuit","elastic waistband","federal government","freudian slip","gothic architecture","guitar pick",
			 "hawaiian shirt","houseplant","leg warmers","lone survivor","luxury car","mechanical pencil","mindfulness","mutual fund","neon lights",
			 "night vision","optical illusion","patchwork quilt","perpetual motion", "centripetal force","pottery wheel","pressed powder",
			 "pressure cooker","publicity stunt","public school system","radio transmitter","rollerblades","rhythm guitar","satellite images",
			 "science fiction","senior menu","shopping bag","shoebox","silent movie","the fifth dimension","the constitution","touchdown","triangle",
			 "fashion trend","turn signal","underground bunker","username","valid password","volunteer","wavelength","wedding ring","wireless keyboard",
		         "wrist tattoo","young adult novel","zombie attack","zero gravity","zippered suit","zoot suit","river raft","absolutely","chartreuse"
                         "chocolate","synchronize","wardrobe","great escape","fire truck","pop art","citric acid","tomato paste","wheat flour","diploma"]
    else: 
        print("Computer did not recognize your input. Remember to use all lowercase and only alphabetic characters.")
        notRecognizedInput = False
                 
secretWord = ""


def getRandomWord(wordList): #will return random string from word list
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANGRAPHICS, missedLetters, correctLetters, secretWord):
    print(HANGMANGRAPHICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):#this will replace the blanks of a correct letter is inputted
     if secretWord[i] in correctLetters:
         blanks=blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks: #will show the word with spaces between the letters
        print(letter, end = ' ')
    print()

          
def getGuess(alreadyGuessed):
     # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
       print('Guess a letter.')
       guess = input()
       guess = guess.lower()
       if len(guess) != 1:
             print('Please enter a single letter.')
       elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
       elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
       else:
           return guess


def playAgain(): #this function returns True if you want to play again, or else it returns False.
    print("Want to play again?(yes or no)")
    return input().lower().startswith('y')

print("HANGMAN")
missedLetters=""
correctLetters=" "
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANGRAPHICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        #find out if you won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Correct. The mystery is "' + secretWord + '"! You win the game!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANGRAPHICS)-1:
            displayBoard(HANGMANGRAPHICS, missedLetters, correctLetters, secretWord)
            print("you ran out of your guesses \n After " + str(len(missedLetters))+" missed guesses and " + str(len(correctLetters)) + " correct guesses, actual answer was " + secretWord + "")
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters=""
            correctLetters=""
            gameIsDone=False
            secretWord = getRandomWord(words)
        else:
            break


            
            
        
    
