# RandomSong
# Replace words of a song with its synonyms
# By Connor Slade :P

from datetime import datetime
import random
import json

############ VARS ############
wordFile = 'data/words.json'   # Synonym Data
songFile = 'data/song.txt'     # Song to read
outFile = 'data/out.txt'       # New Song Output

RandomIndex = True             # Use random Synonyms (True, Any Number)

DEBUG = True                   # Show Program ourputs
COLOR = True                   # Disable Ansi Code Color

ColorCodes = {'black': '30', 'red': '31', 'yellow': '33', 'green': '32', 'blue': '34',
              'cyan': '36', 'magenta': '35', 'white': '37', 'gray': '90', 'reset': '0'}

######### FUNCTIONS #########


def colored(text, color):
    if not COLOR:
        return text
    return '\033[' + ColorCodes[str(color).lower()] + 'm' + str(text) + "\033[0m"


def DebugPrint(Category, Text, Color):
    if not DEBUG:
        return
    print(colored('['+datetime.now().strftime("%H:%M:%S")+'] ', 'yellow') +
          colored('['+Category+'] ', 'magenta')+colored(Text, Color))


# Load and Parse Synonym Data
def loadWordData(file):
    DebugPrint('WordFile', 'Loading File', 'cyan')
    try:
        data = open(file, 'r', encoding='utf-8').read()
    except:
        DebugPrint('WordFile', 'Error Reading File', 'red')
        return None
    DebugPrint('WordFile', 'Success', 'green')
    DebugPrint('WordFile', 'Starting Parse', 'cyan')
    try:
        jsonLoaded = json.loads(data)
    except:
        DebugPrint('WordFile', 'Error : /', 'red')
        return None
    DebugPrint('WordFile', 'Complete', 'green')
    return jsonLoaded


# Get Synonym for a word
def getWordForWord(data, word, RandomIndex):
    words = data[word]
    index = random.randint(0, len(words)-1)
    rng = words[RandomIndex if RandomIndex != True else index]
    return rng


# Replace words in text with synonyms
def forEachInSong(songFile, wordData, RandomIndex):
    DebugPrint('SongFile', 'Loading File', 'cyan')
    try:
        data = open(songFile, 'r', encoding='utf-8').read()
    except:
        DebugPrint('SongFile', 'Error Reading File', 'red')
        return None
    DebugPrint('SongFile', 'Success', 'green')
    DebugPrint('SongFile', 'Genarateing Song', 'cyan')
    working = ''
    words = data.split(' ')
    for word in words:
        try:
            working += getWordForWord(wordData, word, RandomIndex)
        except:
            working += word
        working += ' '
    DebugPrint('SongFile', 'Done :P', 'green')
    return working


# Save new song to a file
def saveNewSong(outFile, data):
    DebugPrint(
        'Output', f'Saveing File {colored("["+outFile+"]", "blue")}', 'cyan')
    file = open(outFile, 'w', encoding='utf-8')
    file.write(data)
    file.close()
    DebugPrint('Output', 'Saveing Complete', 'green')

####### MAIN FUNCTION #######


def main():
    data = loadWordData(wordFile)
    newSong = forEachInSong(songFile, data, RandomIndex)
    saveNewSong(outFile, newSong)


if __name__ == "__main__":
    DebugPrint('Main', 'Starting...', 'green')
    main()
    DebugPrint('Main', 'Exiting...', 'red')
