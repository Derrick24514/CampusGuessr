from cmu_graphics import *
import math
from spot import Spot

def onAppStart(app):
    setActiveScreen('mainScreen')
    app.width = 800
    app.height = 600
    app.leaderboard = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}
    # app.globe = 
    app.map = 'cmumap.jpg'
    app.pin = (400, 80)
    app.score = 0
    lon = 40.444623
    lat = -79.943013
    app.image = Spot(lon,lat,0,-0.76)
    app.currLoc = app.image.latLonToPoint()
    
    app.startGameHighlight = 'white'
    app.howToPlayHighlight = 'white'
    app.aboutHighlight = 'white'
    app.creditsHighlight = 'white'
    
    app.startGameXButtonHighlight = 'white'
    app.howToPlayXButtonHighlight = 'white'
    app.aboutXButtonHighlight = 'white'
    app.creditsXButtonHighlight = 'white'
    app.gameXButtonHighlight = 'white'
    app.guessXButtonHighlight = 'black'
    
    app.yesButtonHighlight = 'white'
    app.noButtonHighlight = 'white'
    app.guessButtonHighlight = 'white'
    app.submitButtonHighlight = 'black'
    
def mainScreen_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawRect(60, 170, 280, 400, fill = None, border = 'white', borderWidth = 2)
    drawRect(460, 170, 150, 50, fill = None, border = app.startGameHighlight, borderWidth = 2)
    drawRect(460, 230, 150, 50, fill = None, border = app.howToPlayHighlight, borderWidth = 2)
    drawRect(460, 290, 150, 50, fill = None, border = app.aboutHighlight, borderWidth = 2)
    drawCircle(80, 80, 40, border = app.creditsHighlight)
    drawCircle(800, 600, 275, border = 'white')
    drawCircle(400, 160, 10, fill = 'white')

    drawLine(400, 160, 400, 580, lineWidth = 5, fill = 'white')
    drawLine(80, 225, 320, 225, lineWidth = 2, fill = 'white')
    for key in app.leaderboard:
        drawLabel(f'{key}: {app.leaderboard[key]}', 120, 220 + 32*key, size = 20, fill = 'white')

    drawLabel('CampusGuessr', 400, 80, size = 60, fill = 'white', bold = True)
    drawLabel('>>>>>>>>>>>>>>>>>>>>>>>>>>', 400, 140, size = 30, fill = 'white')
    drawLabel('N', 645, 140, size = 25, fill = 'red', bold = True)
    drawLabel('S', 155, 138, size = 25, fill = 'dodgerBlue', bold = True)
    
    drawLabel('Start Game', 535, 195, size = 20, fill = 'limeGreen')
    drawLabel('How to Play', 535, 255, size = 20, fill = 'limeGreen')
    drawLabel('About', 535, 315, size = 20, fill = 'limeGreen')
    drawLabel('Credits', 80, 80, size = 20, fill = 'limeGreen')
    drawLabel('Leaderboard Legends:', 200, 200, size = 20, fill = 'white', bold = True)
        
def mainScreen_onMouseMove(app, mouseX, mouseY):
    if mouseInStartGameButton(app, mouseX, mouseY, 460, 170, 150, 50):
        app.startGameHighlight = 'limeGreen'
    else:
        app.startGameHighlight = 'white'
    if mouseInHowToPlayButton(mouseX, mouseY, 460, 230, 150, 50):
        app.howToPlayHighlight = 'limeGreen'
    else:
        app.howToPlayHighlight = 'white'
    if mouseInAboutButton(mouseX, mouseY, 460, 290, 150, 50):
        app.aboutHighlight = 'limeGreen'
    else:
        app.aboutHighlight = 'white'
    if mouseInCreditsButton(mouseX, mouseY, 80, 80, 40):
        app.creditsHighlight = 'limeGreen'
    else:
        app.creditsHighlight = 'white'

def mainScreen_onMousePress(app, mouseX, mouseY):
    if mouseInStartGameButton(app, mouseX, mouseY, 460, 170, 150, 50):
        setActiveScreen('game')
    elif mouseInHowToPlayButton(mouseX, mouseY, 460, 230, 150, 50):
        setActiveScreen('howToPlay')
    elif mouseInAboutButton(mouseX, mouseY, 460, 290, 150, 50):
        setActiveScreen('about')
    elif mouseInCreditsButton(mouseX, mouseY, 80, 80, 40):
        setActiveScreen('credits')

def mouseInStartGameButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

def mouseInHowToPlayButton(mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

def mouseInAboutButton(mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

def mouseInCreditsButton(mouseX, mouseY, cX, cY, r):
    if distance(cX, cY, mouseX, mouseY) <= r:
        return True
    else:
        return False

        
def mouseInXButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

# game screen

def game_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawImage('street_view_image.jpg',0,0)
    drawRect(740, 20, 40, 40, fill = None, border = app.gameXButtonHighlight, borderWidth = 2)
    drawRect(600, 400, 160, 160, fill = None, border = 'white')
    
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    drawLabel('Guess', 680, 460, size = 30, fill = 'limeGreen')
    drawLabel('Location', 680, 500, size = 30, fill = 'limeGreen')
    

def game_onMouseMove(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        app.gameXButtonHighlight = 'limeGreen'
    else:
        app.gameXButtonHighlight = 'white'
    if mouseInGuessButton(app, mouseX, mouseY, 600, 400, 160, 160):
        app.guessButtonHighlight = 'limeGreen'

def game_onMousePress(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        setActiveScreen('areYouSure')
    elif mouseInGuessButton(app, mouseX, mouseY, 600, 400, 160, 160):
        setActiveScreen('guess')

def game_onKeyPress(app,key):
    if key == 'up':
        app.image.changePitchUp()
    elif key == 'down':
        app.image.changePitchDown()
    elif key == 'left':
        app.image.changeHeadingLeft()
    elif key == 'right':
        app.image.changeHeadingRight()
    app.image.getImage()
    

#--------* are you sure secondary screen

def areYouSure_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawRect(230, 200, 340, 160, fill = None, border = 'white', borderWidth = 2)
    drawRect(740, 20, 40, 40, fill = None, border = app.creditsXButtonHighlight, borderWidth = 2)
    
    drawLabel('Are you sure you want to quit?', 400, 240, fill = 'limeGreen', size = 20, bold = True)
    drawLabel('Yes', 320, 305, fill = 'limeGreen', size = 25)
    drawLabel('No', 480, 305, fill = 'limeGreen', size = 25)
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    
    drawRect(260, 280, 120, 50, fill = None, border = app.yesButtonHighlight, borderWidth = 2)
    drawRect(420, 280, 120, 50, fill = None, border = app.noButtonHighlight, borderWidth = 2)
        
def areYouSure_onMouseMove(app, mouseX, mouseY):
    if mouseInYesButton(app, mouseX, mouseY, 260, 280, 120, 50):
        app.yesButtonHighlight = 'limeGreen'
    else:
        app.yesButtonHighlight = 'white'
        
    if mouseInNoButton(app, mouseX, mouseY, 420, 280, 120, 50):
        app.noButtonHighlight = 'limeGreen'
    else:
        app.noButtonHighlight = 'white'

def areYouSure_onMousePress(app, mouseX, mouseY):
    if mouseInYesButton(app, mouseX, mouseY, 260, 280, 120, 50):
        setActiveScreen('mainScreen')
    elif mouseInNoButton(app, mouseX, mouseY, 420, 280, 120, 50):
        setActiveScreen('game')
    
def mouseInYesButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False
    
def mouseInNoButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

# how to play screen
    
def howToPlay_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawRect(740, 20, 40, 40, fill = None, border = app.creditsXButtonHighlight, borderWidth = 2)
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    
    drawLabel('How To Play', 400, 100, fill = 'white', size = 40, bold = True)
    drawLine(140, 150, 660, 150, fill = 'white', lineWidth = 2)
    drawLabel('1: There are a total of 5 rounds', 400, 200, fill = 'limeGreen', size = 25)
    drawLabel('2: On each round, you will be shown a location', 400, 250, fill = 'limeGreen', size = 25)
    drawLabel('3: Click the arrows to look around', 400, 300, fill = 'limeGreen', size = 25)
    drawLabel('4: Click/drag the icon on the minimap to guess where you are', 400, 350, fill = 'limeGreen', size = 25)
    drawLabel('5: The closer your guess is, the more points you recieve', 400, 400, fill = 'limeGreen', size = 25)
    drawLabel('6: Try to place on the leaderboard!', 400, 450, fill = 'limeGreen', size = 25)

def howToPlay_onMouseMove(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        app.creditsXButtonHighlight = 'limeGreen'
    else:
        app.creditsXButtonHighlight = 'white'

def howToPlay_onMousePress(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        setActiveScreen('mainScreen')
        
# about screen
    
def about_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawRect(740, 20, 40, 40, fill = None, border = app.creditsXButtonHighlight, borderWidth = 2)
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    
    drawLabel('About', 400, 100, fill = 'white', size = 40, bold = True)
    drawLine(140, 150, 660, 150, fill = 'white', lineWidth = 2)
    
    drawLabel('Shameless Github plug lol:', 400, 200, fill = 'limeGreen', size = 30)
    drawLabel('https://github.com/KurthaTheBurtha/campusguess', 400, 250, fill = 'limeGreen', size = 30)
    
def about_onMouseMove(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        app.creditsXButtonHighlight = 'limeGreen'
    else:
        app.creditsXButtonHighlight = 'white'

def about_onMousePress(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        setActiveScreen('mainScreen')
        
# credits screen
    
def credits_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawLabel('Roll Credits!!!', 400, 100, fill = 'white', size = 40, bold = True)
    drawLine(140, 150, 660, 150, fill = 'white', lineWidth = 2)
    drawLabel('The Team: Derrick, Han, Kurt, Spanden', 400, 200, fill = 'limeGreen', size = 25)
    drawLabel('The Class: 15-112, CMU', 400, 250, fill = 'limeGreen', size = 25)
    drawLabel('The Date: 11/16/24', 400, 300, fill = 'limeGreen', size = 25)
    drawLabel('...and a MASSIVE thank you to Kosbie, Austin,', 400, 350, fill = 'limeGreen', size = 25)
    drawLabel('and all our wonderful TAs for making Hack112', 400, 400, fill = 'limeGreen', size = 25)
    drawLabel('(and this project) possible, and of course for', 400, 450, fill = 'limeGreen', size = 25)
    drawLabel('teaching us wayyyyy too much about list aliasing :)', 400, 500, fill = 'limeGreen', size = 25)
    
    drawRect(740, 20, 40, 40, fill = None, border = app.creditsXButtonHighlight, borderWidth = 2)
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    
def credits_onMouseMove(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        app.creditsXButtonHighlight = 'limeGreen'
    else:
        app.creditsXButtonHighlight = 'white'

def credits_onMousePress(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        setActiveScreen('mainScreen')
        
# guess screen

def guess_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawImage(app.map, 0, 0)
    drawCircle(app.pin[0], app.pin[1], 10, fill = 'red')
    drawLabel('Click around to guess!', 550, 40, fill = 'black', size = 30, bold = True)
    
    drawRect(40, 520, 160, 60, fill = 'black', border = app.submitButtonHighlight, borderWidth = 2)
    drawLabel('Submit guess', 120, 550, fill = 'limeGreen', size = 10, bold = True)
    
    drawRect(740, 20, 40, 40, fill = None, border = app.guessXButtonHighlight, borderWidth = 2)
    drawLabel('X', 760, 40, size = 40, fill = 'red')
    
def guess_onMouseMove(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        app.guessXButtonHighlight = 'limeGreen'
    else:
        app.guessXButtonHighlight = 'black'
    if mouseInSubmitButton(app, mouseX, mouseY, 40, 520, 160, 60):
        app.submitButtonHighlight = 'limeGreen'
    else:
        app.submitButtonHighlight = 'black'

def guess_onMousePress(app, mouseX, mouseY):
    if mouseInXButton(app, mouseX, mouseY, 740, 20, 40, 40):
        setActiveScreen('game')
    else:
        app.pin = (mouseX, mouseY)
        print(app.pin)
    if mouseInSubmitButton(app, mouseX, mouseY, 40, 520, 160, 60):
        setActiveScreen('score')
        
        # run all score calculations in here

def mouseInGuessButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False
        
def mouseInSubmitButton(app, mouseX, mouseY, rectX, rectY, width, height):
    if (rectX <= mouseX <= rectX + width) and (rectY <= mouseY <= rectY + height):
        return True
    else:
        return False

def mouseInPin(mouseX, mouseY, pinX, pinY, pinR):
    return distance(mouseX, mouseY, pinX, pinY) <= pinR

# score screen

def score_redrawAll(app):
    drawRect(0, 0, 800, 600, fill = 'black')
    drawImage(app.map, 0, 0)
    
    drawCircle(app.pin[0], app.pin[1], 10, fill = 'red')
    drawCircle(app.currLoc[0], app.currLoc[1], 10, fill = 'purple')
    drawLine(app.pin[0], app.pin[1], app.currLoc[0], app.currLoc[1], fill = 'black')

    drawLabel(f'You were {rounded(distance(app.pin[0], app.pin[1], app.currLoc[0], app.currLoc[1]))}m away.', 600, 50, fill = 'black', size = 30, bold = True)
    drawLabel(f'Score + {app.score}', 600, 80, fill = 'black', size = 30, bold = True)
    
# other functions
    
def distance(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
runAppWithScreens('mainScreen')