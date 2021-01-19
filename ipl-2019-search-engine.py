# Programmer: Rohan Kosalge
# Creation Date: May 2, 2019
# Purpose: Basic search engine for the IPL 2019 season. Includes
# stats, games (kind of buggy), players and teams. 

from tkinter import *

handle = open('/Users/rohankosalge/Desktop/Screenshots/iplPlayerStats.txt', 'r')
global tings
tings = handle.read().splitlines()
playersAdv = []
playersAdv2 = []
players = []
for x in range(len(tings)):
    tingSeg = tings[x]
    for x in range(len(tingSeg)):
        if tingSeg[x] == ',':
            playersAdv.append(tingSeg[:x])

for x in range(len(playersAdv)):
    if x%4==0:
        playersAdv2.append(playersAdv[x])
#print(playersAdv2)
for x in range(len(playersAdv2)):
    pSeg = playersAdv2[x]
    pSeg2 = pSeg.replace(" ", "").upper()
    players.append(pSeg2)

    
#print(players)
properTeams = ['Kings XI Punjab', 'Mumbai Indians', 'Chennai Super Kings', 'Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Rajasthan Royals', 'Delhi Capitals', 'Kolkata Knight Riders']
teams = ['KINGSXIPUNJAB', 'MUMBAIINDIANS', 'CHENNAISUPERKINGS', 'SUNRISERSHYDERABAD', 'ROYALCHALLENGERSBANGALORE', 'RAJASTHANROYALS', 'DELHICAPITALS', 'KOLKATAKNIGHTRRIDERS']
teamQueries = ['KINGSXI', 'PUNJAB', 'MUMBAI', 'INDIANS', 'CHENNAI', 'SUPERKINGS', 'SUNRISERS', 'HYDERABAD', 'ROYALCHALLENGERS', 'CHALLENGERS', 'BANGALORE', 'CHALLENGERSBANGALORE', 'RAJASTHAN', 'ROYALS', 'DELHI', 'CAPITALS', 'KOLKATA', 'KNIGHTRIDERS', 'DC', 'RR', 'CSK', 'KKR', 'RCB', 'MI', 'SRH', 'KXIP']
inList = ['CSK', 'DC', 'RR', 'KXIP', 'SRH', 'KKR', 'MI', 'RCB']
inToTeamList = {'CSK':'Chennai Super Kings', 'DC':'Delhi Capitals', 'SRH':'Sunrisers Hyderabad', 'RR':'Rajasthan Royals', 'RCB':'Royal Challengers Bangalore', 'MI':'Mumbai Indians', 'KKR':'Kolkata Knight Riders', 'KXIP':'Kings XI Punjab'}
#main: search up stats
#profile: search up people
#team: search up teams
main = Tk()
main.title('Smart Stats')

search = Entry(main, width=45)
search.insert(END, 'Search a stat, cricketer, team, or match in IPL 2019!')
search.grid(row=0, column=0)

statBoard = Canvas(height=350, width=520, bg='#e4e4e4')
statBoard.grid(row=1, columnspan=3)

def clear():
    statBoard.create_rectangle(0, 0, 550, 375, fill='#e4e4e4', outline='#e4e4e4')

home = Button(main, text='Home', command=clear)
home.grid(row=0, column=2)

global allLists
allLists = [['David Warner', 'KL Rahul', 'Quinton de Kock', 'Shikhar Dhawan', 'Andre Russell', 'Chris Gayle', 'Rishabh Pant', 'Virat Kohli', 'Shreyas Iyer', 'Jonny Bairstow'], ['Jonny Bairstow', 'Ajinkya Rahane', 'Sanju Samson', 'David Warner', 'KL Rahul', 'Virat Kohli', 'Chris Gayle', 'Prithvi Shaw', 'Dinesh Karthik', 'Shikhar Dhawan'], ['Shikhar Dhawan', 'David Warner', 'Rohit Sharma', 'KL Rahul', 'Jonny Bairstow', 'Parthiv Patel', 'Virat Kohli', 'Quinton de Kock', 'Chris Gayle', 'Suryakumar Yadav'], ['Andre Russell', 'Chris Gayle', 'Hardik Pandya', 'Rishabh Pant', 'AB de Villiers', 'KL Rahul', 'Quinton de Kock', 'MS Dhoni', 'Chris Lynn', 'Kieron Pollard'], ['Andre Russell', 'Hardik Pandya', 'Sam Curran', 'Sunil Narine', 'Moeen Ali', 'Rishabh Pant', 'Wriddhiman Saha', 'Jonny Bairstow', 'Nicholas Pooran', 'Kieron Pollard'], ['Hardik Pandya', 'Rishabh Pant', 'KL Rahul', 'Andre Russell', 'Kieron Pollard', 'Andre Russell', 'Sam Curran', 'Moeen Ali', 'David Warner', 'Manish Pandey'], ['Jonny Bairstow', 'Sanju Samson', 'David Warner', 'Virat Kohli', 'Ajinkya Rahane', 'KL Rahul'], ['David Warner', 'KL Rahul', 'Shikhar Dhawan', 'AB de Villiers', 'Quinton de Kock', 'Andre Russell', 'Chris Gayle', 'Chris Lynn', 'Rishabh Pant', 'Shreyas Iyer'], ['MS Dhoni', 'David Warner', 'Andre Russell', 'Jonny Bairstow', 'KL Rahul', 'Marcus Stoinis', 'Sarfaraz Khan', 'Hardik Pandya', 'AB de Villiers', 'Manish Pandey'], ['Imran Tahir', 'Kagiso Rabada', 'Deepak Chahar', 'Shreyas Gopal', 'Jasprit Bumrah', 'Khaleel Ahmed', 'Mohammed Shami', 'Yuzvendra Chahal', 'Rashid Khan', 'Harbhajan Singh'], ['Jofra Archer', 'Deepak Chahar', 'Rashid Khan', 'Ravindra Jadeja', 'Imran Tahir', 'Harbhajan Singh', 'Shreyas Gopal', 'Ishant Sharma', 'Sunil Narine', 'Ish Sodhi'], ['Deepak Chahar', 'Jasprit Bumrah', 'Bhuvneshwar Kumar', 'Rashid Khan', 'Imran Tahir', 'Navdeep Saini', 'Ravindra Jadeja', 'Rahul Chahar', 'Ishant Sharma', 'Jofra Archer'], ['Deepak Chahar', 'Yuzvendra Chahal', 'Imran Tahir', 'Varun Aaron', 'Deepak Chahar', 'Mohammad Nabi', 'Shreyas Gopal', 'Alzarri Joseph', 'Rashid Khan', 'Navdeep Saini'], ['Anukul Roy', 'Jagadeesha Suchith', 'Alzarri Joseph', 'Kagiso Rabada', 'Khaleel Ahmed', 'Oshane Thomas', 'Imran Tahir', 'Ish Sodhi', 'Dale Steyn', 'Shreyas Gopal'], ['Anukul Roy', 'Rashid Khan', 'Stuart Binny', 'Ravindra Jadeja', 'Rahul Chahar', 'Rahul Tewatia', 'Jasprit Bumrah', 'Mohammad Nabi', 'Imran Tahir', 'Mitchell Santner'], ['Yuzvendra Chahal', 'Imran Tahir', 'Krunal Pandya', 'Mohammed Siraj', 'Mohammad Nabi', 'Shreyas Gopal', 'Ravindra Jadeja', 'Mitchell Santner', 'Mohammad Nabi', 'Alzarri Joseph'], ['Alzarri Joseph', 'Mohammad Nabi', 'Sam Curran', 'Imran Tahir', 'Kagiso Rabada', 'Kagiso Rabada', 'Imran Tahir', 'Lasith Malinga', 'Lasith Malinga', 'Yuzvendra Chahal'], ['Faf du Plessis', 'Hardik Pandya', 'Deepak Hooda', 'Vijay Shankar', 'Axar Patel', 'Suryakumar Yadav', 'Ravindra Jadeja', 'Kieron Pollard', 'Shreyas Iyer', 'David Miller'], ['Andre Russell', 'Hardik Pandya', 'Deepak Chahar', 'Imran Tahir', 'Quinton de Kock', 'Rashid Khan', 'Rishabh Pant', 'Jasprit Bumrah', 'Ravindra Jadeja', 'Chris Gayle'], ['Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Delhi Capitals', 'Sunrisers Hyderabad', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Royal Challengers Bangalore'], ['Ashton Turner', 'Chris Morris', 'Rashid Khan', 'Shane Watson', 'Pawan Negi', 'Keemo Paul', 'Kuldeep Yadav', 'Marcus Stoinis', 'Chris Lynn', 'Ravichandran Ashwin'], ['Mumbai Indians', 'Chennai Super Kings', 'Delhi Capitals', 'Sunrisers Hyderabad', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Rajasthan Royals', 'Royal Challengers Bangalore']]

global colorsLists
colorsLists = [['orange', 'red'], ['yellow', 'blue'], ['#f24a3e', '#ccd2dd'], ['blue', 'yellow'], ['#4988ed', '#f24a3e'], ['purple', 'yellow'], ['#f9b8df', '#1b4fd3'], ['red', 'yellow']]

def runs():
    global allLists
    rList = allLists[0]
    rPoints = ['692', '593', '529', '521', '510', '490', '488', '464', '463', '445']

    rpC = [colorsLists[0],colorsLists[2],colorsLists[3],colorsLists[4],colorsLists[5],colorsLists[2],colorsLists[4],colorsLists[7],colorsLists[4],colorsLists[0]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='RUNS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='David Warner scored the most amount of runs, punching a massive 692 runs this year.', font=('Ubuntu', 10, 'normal'))

def runs2():
    global colorsLists
    global allLists
    rList = allLists[1]
    rPoints = ['114 (56)', '105 (63)', '102 (55)', '100 (55)', '100 (64)', '100 (58)', '99 (64)', '99 (55)', '97 (50)', '97 (63)']

    rpC = [colorsLists[0], colorsLists[6], colorsLists[6], colorsLists[0], colorsLists[2], colorsLists[7], colorsLists[2], colorsLists[4], colorsLists[5], colorsLists[4]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='SCORE', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Jonny Bairstow scored the most amount of runs in a single match, smashing a fast 114 single-handedly.', font=('Ubuntu', 10, 'normal'))

def fours():
    global colorsLists
    global allLists
    rList = allLists[2]
    rPoints = ['64', '57', '52', '49', '48', '48', '46', '45', '45', '45']

    rpC = [colorsLists[4], colorsLists[0], colorsLists[3], colorsLists[2], colorsLists[0], colorsLists[7], colorsLists[7], colorsLists[3], colorsLists[2], colorsLists[3]] 

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='FOURS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Shikhar Dhawan hit the most number of fours this year, knocking an impressive 64 shots.', font=('Ubuntu', 10, 'normal'))

def sixes():
    global colorsLists
    global allLists
    rList = allLists[3]
    rPoints = ['52', '34', '29', '27', '26', '25', '25', '23', '22', '22']

    rpC = [colorsLists[5], colorsLists[2], colorsLists[3], colorsLists[4], colorsLists[7], colorsLists[2], colorsLists[3], colorsLists[1], colorsLists[5], colorsLists[3]] 

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='SIXES', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Andre Russell pounded 52 sixes, 18 more than the next person.', font=('Ubuntu', 10, 'normal'))

def sr():
    global colorsLists
    global allLists
    rList = allLists[4]
    rPoints = ['204.81', '191.42', '172.72', '166.27', '165.41', '162.66', '162.26', '157.24', '157.00', '156.74']

    rpC = [colorsLists[5], colorsLists[3], colorsLists[2], colorsLists[5], colorsLists[7], colorsLists[4], colorsLists[0], colorsLists[0], colorsLists[2], colorsLists[3]] 

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='STRIKE RATE', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Andre Russell maintained the highest strike rate, keeping it above 200.', font=('Ubuntu', 10, 'normal'))

def f1():
    global colorsLists
    global allLists
    rList = allLists[5]
    rPoints = ['17', '18', '19', '21', '22', '23', '23', '24', '24', '25']

    rpC = [colorsLists[3], colorsLists[4], colorsLists[2], colorsLists[5], colorsLists[3], colorsLists[5], colorsLists[2], colorsLists[7], colorsLists[0], colorsLists[0]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='BALLS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Hardik Pandya smashed a score of 50 in just 17 balls!', font=('Ubuntu', 10, 'normal'))

def c1():
    global colorsLists
    global allLists
    rList = allLists[6]
    rPoints = ['52', '54', '54', '57', '58', '63']

    rpC = [colorsLists[0], colorsLists[6], colorsLists[0], colorsLists[7], colorsLists[6], colorsLists[2]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='BALLS', font=('Ubuntu', 15, 'bold'))

    for x in range(6):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Out of only six people, Jonny Bairstow hit the fastest in 52 balls.', font=('Ubuntu', 10, 'normal'))

def f2():
    global colorsLists
    global allLists
    rList = allLists[7]
    rPoints = ['8', '6', '5', '5', '4', '4', '4', '4', '3', '3']

    rpC = [colorsLists[0], colorsLists[2], colorsLists[4], colorsLists[7], colorsLists[3], colorsLists[5], colorsLists[2], colorsLists[5], colorsLists[4], colorsLists[4]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='FIFTIES', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='In just 12 innings, David Warner hit a fifty in 8 of them!', font=('Ubuntu', 10, 'normal'))

def c2():
    global colorsLists
    global allLists
    rList = allLists[6]
    rPoints = ['1', '1', '1', '1', '1', '1']

    rpC = [colorsLists[0], colorsLists[6], colorsLists[0], colorsLists[7], colorsLists[6], colorsLists[2]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='CENTURIES', font=('Ubuntu', 15, 'bold'))

    for x in range(6):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Six people are tied for this stat.', font=('Ubuntu', 10, 'normal'))

def ba1():
    global colorsLists
    global allLists
    rList = allLists[8]
    rPoints = ['83.20', '69.20', '56.66', '55.62', '53.90', '52.75', '45.00', '44.66', '44.20', '43.00']

    rpC = [colorsLists[1], colorsLists[0], colorsLists[5], colorsLists[0], colorsLists[2], colorsLists[7], colorsLists[2], colorsLists[3], colorsLists[7], colorsLists[0]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='AVERAGE', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='MS Dhoni rarely got out in his time on the pitch.', font=('Ubuntu', 10, 'normal'))

def wickets():
    global colorsLists
    global allLists
    rList = allLists[9]
    rPoints = ['26', '25', '22', '20', '19', '19', '19', '18', '17', '16']

    rpC = [colorsLists[1], colorsLists[4], colorsLists[1], colorsLists[6], colorsLists[3], colorsLists[0], colorsLists[2], colorsLists[7], colorsLists[0], colorsLists[1]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='WICKETS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Imran Tahir notched up 26 wickets this year.', font=('Ubuntu', 10, 'normal'))

def maidens():
    global colorsLists
    global allLists
    rList = allLists[10]
    rPoints = ['2', '2', '1', '1', '1', '1', '1', '1', '1', '1']

    rpC = [colorsLists[6], colorsLists[1], colorsLists[0], colorsLists[1], colorsLists[1], colorsLists[1], colorsLists[6], colorsLists[4], colorsLists[5], colorsLists[6]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='MAIDENS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Jofra Archer and Deepak Chahar were the only ones to get two maidens.', font=('Ubuntu', 10, 'normal'))

def dots():
    global colorsLists
    global allLists
    rList = allLists[11]
    rPoints = ['190', '169', '168', '166', '149', '141', '128', '125', '122', '121']

    rpC = [colorsLists[1], colorsLists[3], colorsLists[0], colorsLists[0], colorsLists[1], colorsLists[7], colorsLists[1], colorsLists[3], colorsLists[4], colorsLists[6]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='DOTS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Deepak Chahar comes in twice in this list, bowling 20 and 17 individually in single matches alone!', font=('Ubuntu', 10, 'normal'))

def dots2():
    global colorsLists
    global allLists
    rList = allLists[12]
    rPoints = ['20', '18', '18', '17', '17', '16', '16', '16', '16', '16']

    rpC = [colorsLists[1], colorsLists[7], colorsLists[1], colorsLists[6], colorsLists[1], colorsLists[0], colorsLists[6], colorsLists[3], colorsLists[0], colorsLists[7]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='DOTS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Deepak Chahar bowled a scary 190 dots, a lot compared to everyone else.', font=('Ubuntu', 10, 'normal'))

def ba2():
    global colorsLists
    global allLists
    rList = allLists[13]
    rPoints = ['11.00', '14.00', '14.50', '14.72', '15.10', '15.80', '16.57', '16.75', '17.25', '17.35']

    rpC = [colorsLists[3], colorsLists[4], colorsLists[3], colorsLists[4], colorsLists[0], colorsLists[6], colorsLists[1], colorsLists[6], colorsLists[7], colorsLists[6]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='AVERAGE', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Anukul Roy had the lowest bowling average, 3 less than the next person.', font=('Ubuntu', 10, 'normal'))

def econ():
    global colorLists
    global allLists
    rList = allLists[14]
    rPoints = ['5.50', '6.28', '6.28', '6.35', '6.35', '6.63', '6.63', '6.65', '6.69', '6.71']

    rpC = [colorsLists[3], colorsLists[0], colorsLists[6], colorsLists[1], colorsLists[3], colorsLists[4], colorsLists[3], colorsLists[0], colorsLists[1], colorsLists[1]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='ECONOMY', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Anukul Roy had the lowest economy, and is the outlier compared to everyone else.', font=('Ubuntu', 10, 'normal'))

def econ2():
    global colorsLists
    global allLists
    rList = allLists[15]
    rPoints = ['1.50', '2.25', '2.33', '2.50', '2.75', '3.00', '3.00', '3.25', '3.25', '3.27']

    rpC = [colorsLists[7], colorsLists[1], colorsLists[3], colorsLists[7], colorsLists[0], colorsLists[6], colorsLists[1], colorsLists[1], colorsLists[0], colorsLists[3]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='ECONOMY', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Yuzvendra Chahal\'s economy is the best, with under 2 runs per over conceded!', font=('Ubuntu', 10, 'normal'))

def bf():
    global colorsLists
    global allLists
    rList = allLists[16]
    rPoints = ['6/12', '4/11', '4/11', '4/12', '4/21', '4/22', '4/27', '4/31', '4/37', '4/38']

    rpC = [colorsLists[3], colorsLists[0], colorsLists[2], colorsLists[1], colorsLists[4], colorsLists[4], colorsLists[1], colorsLists[3], colorsLists[3], colorsLists[7]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='FIGURES', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Alzarri Joseph boasted the best figures of all time in IPL, with 6 wickets for only twice the runs.', font=('Ubuntu', 10, 'normal'))

def catches():
    global colorsLists
    global allLists
    rList = allLists[17]
    rPoints = ['12', '11', '10', '10', '9', '9', '9', '8', '8', '7']

    rpC = [colorsLists[1], colorsLists[3], colorsLists[0], colorsLists[0], colorsLists[4], colorsLists[3], colorsLists[1], colorsLists[3], colorsLists[4], colorsLists[2]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='CATCHES', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Faf du Plessis had a great time on the field, with 12 catches in total.', font=('Ubuntu', 10, 'normal'))

def pp():
    global colorsLists
    global allLists
    rList = allLists[18]
    rPoints = ['369', '342', '274.5', '255', '247.5', '247.5', '247', '240.5', '234.5', '231.5']
    
    rpC = [colorsLists[5], colorsLists[3], colorsLists[1], colorsLists[1], colorsLists[3], colorsLists[0], colorsLists[4], colorsLists[3], colorsLists[1], colorsLists[2]] 

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='POINTS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Andre Russell had the best performance and the most popularity out of everyone.', font=('Ubuntu', 10, 'normal'))

def tp():
    global colorsLists
    global allLists
    rList = allLists[19]
    rPoints = ['232', '231', '218', '213', '213', '212', '206', '205', '203', '202']

    rpC = [colorsLists[5], colorsLists[0], colorsLists[5], colorsLists[7], colorsLists[4], colorsLists[0], colorsLists[5], colorsLists[7], colorsLists[5], colorsLists[7]]

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='TEAM', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='TOTAL', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Kolkata hit a crazy four 200+ totals in the league!', font=('Ubuntu', 10, 'normal'))

def ducks():
    global colorsLists
    global allLists
    rList = allLists[20]
    rPoints = ['3', '3', '3', '3', '2', '2', '2', '2', '2', '2']

    rpC = [colorsLists[6], colorsLists[4], colorsLists[0], colorsLists[1], colorsLists[7], colorsLists[4], colorsLists[5], colorsLists[7], colorsLists[5], colorsLists[2]]        

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='PLAYER', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='DUCKS', font=('Ubuntu', 15, 'bold'))

    for x in range(10):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Four people are tied for this stat.', font=('Ubuntu', 10, 'normal'))

def standings():
    global colorsLists
    global allLists
    rList = allLists[21]
    rPoints = ['14', '14', '14', '12', '12', '12', '11', '11']

    rpC = [colorsLists[3], colorsLists[1], colorsLists[4], colorsLists[0], colorsLists[5], colorsLists[2], colorsLists[6], colorsLists[7]] 

    statBoard.create_rectangle(0, 0, 420, 30, outline='black', width=2)
    statBoard.create_rectangle(420, 0, 520, 30, outline='black', width=2)
    statBoard.create_text(210, 15, text='TEAM', font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(470, 15, text='POINTS', font=('Ubuntu', 15, 'bold'))

    for x in range(8):
        statBoard.create_rectangle(0, 30+(30*x), 420, 60+(30*x), outline='black', width=2, fill=rpC[x][0])
        statBoard.create_rectangle(420, 30+(30*x), 520, 60+(30*x), outline='black', width=2, fill=rpC[x][1])
        statBoard.create_text(20, 45+(30*x), text=rList[x], anchor=W, font=('Ubuntu', 12, 'italic'))
        statBoard.create_text(470, 45+(30*x), text=rPoints[x], font=('Ubuntu', 15, 'italic'))

    statBoard.create_text(260, 340, text='Mumbai was first in the end of the regular season.', font=('Ubuntu', 10, 'normal'))

    
def pFunc(name):

    colorTeamMap = {'CSK':['yellow', 'blue'], 'SRH':['orange', 'red'], 'KKR':['purple', 'yellow'], ' MI':['blue', 'yellow'], 'RCB':['red', 'yellow'], ' RR':['#f9b8df', '#1b4fd3'], ' DC':['#4988ed', '#f24a3e'], 'XIP':['#f24a3e', '#ccd2dd']}
    initialToTeamMap = {'CSK':'Chennai Super Kings', 'SRH':'Sunrisers Hyderabad', 'KKR':'Kolkata Knight Riders', ' MI':'Mumbai Indians', 'RCB':'Royal Challengers Bangalore', ' RR':'Rajasthan Royals', ' DC':'Delhi Capitals', 'XIP':'Kings XI Punjab'}
    global tings
    statBoard.create_rectangle(0, 0, 520, 100, outline='black', width=2)
    statBoard.create_rectangle(0, 100, 520, 200, outline='black', width=2)
    for x in range(4):
        statBoard.create_rectangle(0, 150+(50*x), 420, 200+(50*x), outline='black', width=2)
        statBoard.create_rectangle(420, 150+(50*x), 520, 200+(50*x), outline='black', width=2)

    for x in range(len(players)):
        if (name == players[x]) or (name in players[x]):
            playerN = playersAdv2[x]

    for x in range(len(tings)):
        if playerN in tings[x]:
            playerList = tings[x]

    teamName = playerList[-3:]
    #print(teamName)
    playerStats = []
    cc = 0
    for x in range(len(playerList)):
        if playerList[x] == ',':
            cc += 1
            if cc == 1:
                in1 = x+2
            if cc == 4:
                in2 = x

    
    realStats = playerList[in1:in2]
    cc2 = 0
    for x in range(len(realStats)):
        if realStats[x] == ',':
            cc2 += 1
            if cc2 == 1:
                m1 = x
            if cc2 == 2:
                m2 = x

    innings = realStats[:m1]
    runs = realStats[m1+2:m2]
    wickets = realStats[m2+2:]
    realStatsList = []
    teamName2 = initialToTeamMap[teamName]
    realStatsList.append(teamName2)
    realStatsList.append(innings)
    realStatsList.append(runs)
    realStatsList.append(wickets)
    
    realStatsQs = ['Team:', 'Number of Matches Played:', 'Number of Runs Scored:', 'Number of Wickets Taken:']
    
    statBoard.create_rectangle(0, 0, 520, 100, fill=(colorTeamMap[teamName])[0], outline='black', width=2)
    statBoard.create_text(260, 50, text=playerN, font=('Ubuntu', 30, 'bold'))
    statBoard.create_rectangle(0, 100, 520, 150, fill=(colorTeamMap[teamName])[1], outline='black', width=2)
    statBoard.create_text(260, 125, text='Statistics in IPL 2019:', anchor=E, font=('Ubuntu', 20, 'bold italic'))

    for x in range(4):
        statBoard.create_rectangle(0, 150+(50*x), 300, 200+(50*x), fill=(colorTeamMap[teamName])[0], outline='black', width=2)
        statBoard.create_rectangle(300, 150+(50*x), 520, 200+(50*x), fill=(colorTeamMap[teamName])[0], outline='black', width=2)
        statBoard.create_text(20, 175+(50*x), text=realStatsQs[x], anchor=W, font=('Ubuntu', 15, 'italic'))
        statBoard.create_text(410, 175+(50*x), text=realStatsList[x], font=('Ubuntu', 15, 'bold'))

def tFunc(name):
    global teams
    global properTeams
    global playersAdv2
    global inList
    global inToTeamList
    for x in range(len(teams)):
        if (name in teams[x]) or name == teams[x]:
            team = properTeams[x]

    if name in inList:
        team = inToTeamList[name]

    #print(playersAdv2[0:25])
    #print(playersAdv2[25:50])
    #print(playersAdv2[50:73])
    #print(playersAdv2[73:94])
    #print(playersAdv2[94:120])
    #print(playersAdv2[120:145])
    #print(playersAdv2[145:169])
    #print(playersAdv2[169:191])

    teamRatingMap = {'Chennai Super Kings':'10', 'Mumbai Indians':'10', 'Sunrisers Hyderabad':'8', 'Royal Challengers Bangalore':'7', 'Kolkata Knight Riders':'6', 'Delhi Capitals':'5', 'Kings XI Punjab':'5', 'Rajasthan Royals':'3'}
    teamColorMap = {'Chennai Super Kings':['yellow', 'blue'], 'Sunrisers Hyderabad':['orange', 'red'], 'Kolkata Knight Riders':['purple', 'yellow'], 'Mumbai Indians':['blue', 'yellow'], 'Royal Challengers Bangalore':['red', 'yellow'], 'Rajasthan Royals':['#f9b8df', '#1b4fd3'], 'Delhi Capitals':['#4988ed', '#f24a3e'], 'Kings XI Punjab':['#f24a3e', '#ccd2dd']}
    teamSquadMap = {'Chennai Super Kings':playersAdv2[0:25], 'Delhi Capitals':playersAdv2[25:50], 'Kings XI Punjab':playersAdv2[50:73], 'Kolkata Knight Riders':playersAdv2[73:94], 'Mumbai Indians':playersAdv2[94:120], 'Rajasthan Royals':playersAdv2[120:145], 'Royal Challengers Bangalore':playersAdv2[145:169], 'Sunrisers Hyderabad':playersAdv2[169:191]}
    teamChampMap = {'Chennai Super Kings':'2010, 2011, \n 2018', 'Mumbai Indians':'2013, 2015, \n 2017, 2019', 'Sunrisers Hyderabad':'2016', 'Kolkata Knight Riders':'2012, 2014', 'Rajasthan Royals':'2008', 'Royal Challengers Bangalore':'None', 'Kings XI Punjab':'None', 'Delhi Capitals':'None'} 
    teamCaptainMap = {'Chennai Super Kings':'MS Dhoni', 'Rajasthan Royals':'Ajinkya Rahane/Steve Smith', 'Sunrisers Hyderabad':'Kane Williamson', 'Kings XI Punjab':'Ravichandran Ashwin', 'Mumbai Indians':'Rohit Sharma', 'Royal Challengers Bangalore':'Virat Kohli', 'Delhi Capitals':'Shreyas Iyer', 'Kolkata Knight Riders':'Dinesh Karthik'}
    teamInitialMap = {'Chennai Super Kings':'CSK', 'Sunrisers Hyderabad':'SRH', 'Royal Challengers Bangalore':'RCB', 'Mumbai Indians':'MI', 'Delhi Capitals':'DC', 'Kolkata Knight Riders':'KKR', 'Kings XI Punjab':'KXIP', 'Rajasthan Royals':'RR'}

    teamRating = teamRatingMap[team]
    teamColorList = teamColorMap[team]
    teamSquadList = teamSquadMap[team]
    teamChamp = teamChampMap[team]
    teamCaptain = teamCaptainMap[team]
    teamInitial = teamInitialMap[team]

    statBoard.create_rectangle(0, 0, 520, 75, fill=teamColorList[0], outline='black', width=2)
    statBoard.create_text(260, 37.5, text=team, font=('Ubuntu', 30, 'bold'))
    statBoard.create_rectangle(0, 75, 520, 100, fill=teamColorList[1], outline='black', width=2)
    statBoard.create_text(20, 87.5, anchor=W, text='Otherwise known as: ' + teamInitial, font=('Ubuntu', 15, 'italic'))
    statBoard.create_text(260, 87.5, anchor=W, text='Captain: ' + teamCaptain, font=('Ubuntu', 15, 'italic'))
    statBoard.create_rectangle(0, 100, 260, 225, fill=teamColorList[0], outline='black', width=2)
    statBoard.create_text(130, 141, text='Championship(s):', font=('Ubuntu', 20, 'bold italic'))
    statBoard.create_text(130, 182, text=teamChamp, font=('Ubuntu', 25, 'bold'))
    statBoard.create_rectangle(0, 225, 260, 350, fill=teamColorList[0], outline='black', width=2)
    statBoard.create_text(130, 266, text='Overall Team Rating:', font=('Ubuntu', 20, 'bold italic'))
    statBoard.create_text(130, 307, text=teamRating + '/10', font=('Ubuntu', 25, 'bold'))
    statBoard.create_rectangle(260, 100, 520, 350, fill=teamColorList[0], outline='black', width=2)
    statBoard.create_text(300, 225, text='2019 IPL Squad:', angle=90, font=('Ubuntu', 25, 'bold italic'))
    for x in range(len(teamSquadList)):
        statBoard.create_text(390, 110+(9.75*x), text=teamSquadList[x], font=('Ubuntu', 10, 'italic'))

def match(m):
    teamCount = 0
    global teamQueries
    teamList = []
    teamColorMap = {'Chennai Super Kings':['yellow'], 'Sunrisers Hyderabad':['orange'], 'Kolkata Knight Riders':['purple'], 'Mumbai Indians':['blue'], 'Royal Challengers Bangalore':['red'], 'Rajasthan Royals':['#f9b8df'], 'Delhi Capitals':['#4988ed'], 'Kings XI Punjab':['#f24a3e'], 'N/A':['#e4e4e4']}
    teamColorMap2 = {'CSK':['yellow'], 'SRH':['orange'], 'KKR':['purple'], 'MI':['blue'], 'RCB':['red'], 'RR':['#f9b8df'], 'DC':['#4988ed'], 'KXIP':['#f24a3e'], 'N/A':['#e4e4e4']}
    shortToRealMap = {'CHENNAI':'Chennai Super Kings', 'CSK':'Chennai Super Kings', 'SUPERKINGS':'Chennai Super Kings', 'CHENNAISUPERKINGS':'Chennai Super Kings', 'PUNJAB':'Kings XI Punjab', 'KXIP':'Kings XI Punjab', 'KINGSXI':'Kings XI Punjab', 'KINGSXIPUNJAB':'Kings XI Punjab', 'MUMBAI':'Mumbai Indians', 'INDIANS':'Mumbai Indians', 'MI':'Mumbai Indians', 'MUMBAIINDIANS':'Mumbai Indians', 'BANGALORE':'Royal Challengers Bangalore', 'ROYALCHALLENGERS':'Royal Challengers Bangalore', 'RCB':'Royal Challengers Bangalore', 'ROYALCHALLENGERSBANGALORE':'Royal Challengers Bangalore', 'KOLKATA':'Kolkata Knight Riders', 'KNIGHTRIDERS':'Kolkata Knight Riders', 'KKR':'Kolkata Knight Riders', 'KOLKATAKNIGHTRIDERS':'Kolkata Knight Riders', 'RAJASTHAN':'Rajasthan Royals', 'JAIPUR':'Rajasthan Royals', 'RR':'Rajasthan Royals', 'ROYALS':'Rajasthan Royals', 'RAJASTHANROYALS':'Rajasthan Royals', 'JAIPURROYALS':'Rajasthan Royals', 'DELHI':'Delhi Capitals', 'DC':'Delhi Capitals', 'DD':'Delhi Capitals', 'CAPITALS':'Delhi Capitals', 'DAREDEVILS':'Delhi Capitals', 'DELHIDAREDEVILS':'Delhi Capitals', 'DELHICAPITALS':'Delhi Capitals', 'HYDERABAD':'Sunrisers Hyderabad', 'SRH':'Sunrisers Hyderabad', 'SUNRISERS':'Sunrisers Hyderabad', 'SUNRISERSHYDERABAD':'Sunrisers Hyderabad'}
    inToTeamList = {'CSK':'Chennai Super Kings', 'DC':'Delhi Capitals', 'SRH':'Sunrisers Hyderabad', 'RR':'Rajasthan Royals', 'RCB':'Royal Challengers Bangalore', 'MI':'Mumbai Indians', 'KKR':'Kolkata Knight Riders', 'KXIP':'Kings XI Punjab', 'N/A':'N/A'}
    for x in range(len(teamQueries)):
        if teamQueries[x] in m:
            teamList.append(shortToRealMap[teamQueries[x]])

    if (len(teamList) != 2) or (teamList[0] == teamList[1]):
        statBoard.create_rectangle(0, 0, 550, 400, fill='#e4e4e4', outline='#e4e4e4')
        statBoard.create_text(260, 175, text='SORRY, I COULDN\'T UNDERSTAND YOUR SEARCH. \n                                         TRY AGAIN.', font=('Ubuntu', 20, 'bold'))

    handle = open('/Users/rohankosalge/Desktop/Screenshots/iplInfoMatches2019.txt', 'r')
    matches = handle.read().splitlines()
    #print(matches)

    fileIndexes = []
    
    for x in range(len(matches)-2):
        testList = [matches[x], matches[x+2]]
        if (matches[x] == teamList[0] and matches[x+2] == teamList[1]) or (matches[x] == teamList[1] and matches[x+2] == teamList[0]):
            fileIndexes.append(x)

    i1 = fileIndexes[0]
    i2 = fileIndexes[1]

    teamOne1 = matches[i1]
    teamTwo1 = matches[i2]
    teamOne2 = matches[i1+2]
    teamTwo2 = matches[i2+2]
    i1Score1 = matches[i1+1]
    i1Score2 = matches[i1+3]
    i2Score1 = matches[i2+1]
    i2Score2 = matches[i2+3]
    result1 = matches[i1+4]
    result2 = matches[i2+4]
    motm1 = matches[i1+5]
    motm2 = matches[i2+5]

    for x in range(len(motm1)):
        if motm1[x] == '(':
            in1 = x+1
        if motm1[x] == ')':
            winner1Key = motm1[in1:x]

    for x in range(len(motm2)):
        if motm2[x] == '(':
            in1 = x+1
        if motm2[x] == ')':
            winner2Key = motm2[in1:x]

    winnerColor1 = (teamColorMap2[winner1Key])[0]
    winnerColor2 = (teamColorMap2[winner2Key])[0]
    winner1 = inToTeamList[winner1Key]
    winner2 = inToTeamList[winner2Key]

    statBoard.create_line(0, 175, 520, 175, width=4)

    statBoard.create_rectangle(0, 0, 260, 125, fill=teamColorMap[teamOne1], outline='black', width=2)
    statBoard.create_rectangle(260, 0, 520, 125, fill=teamColorMap[teamTwo1], outline='black', width=2)
    statBoard.create_rectangle(0, 125, 520, 150, fill=winnerColor1, outline='black', width=2)
    statBoard.create_rectangle(0, 150, 520, 175, fill=winnerColor1, outline='black', width=2)

    statBoard.create_rectangle(0, 175, 260, 300, fill=teamColorMap[teamOne2], outline='black', width=2)
    statBoard.create_rectangle(260, 175, 520, 300, fill=teamColorMap[teamTwo2], outline='black', width=2)
    statBoard.create_rectangle(0, 300, 520, 325, fill=winnerColor2, outline='black', width=2)
    statBoard.create_rectangle(0, 325, 520, 350, fill=winnerColor2, outline='black', width=2)

    statBoard.create_text(130, 55, text=teamOne1, font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(130, 70, text=i1Score1, font=('Ubuntu', 10, 'bold italic'))
    statBoard.create_text(390, 55, text=teamTwo1, font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(390, 70, text=i1Score2, font=('Ubuntu', 10, 'bold italic'))
    statBoard.create_text(260, 137.5, text=result1, font=('Ubuntu', 10, 'normal'))
    statBoard.create_text(260, 162.5, text=motm1, font=('Ubuntu', 10, 'normal'))

    statBoard.create_text(130, 230, text=teamOne2, font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(130, 245, text=i2Score1, font=('Ubuntu', 10, 'bold italic'))
    statBoard.create_text(390, 230, text=teamTwo2, font=('Ubuntu', 15, 'bold'))
    statBoard.create_text(390, 245, text=i2Score2, font=('Ubuntu', 10, 'bold italic'))
    statBoard.create_text(260, 312.5, text=result2, font=('Ubuntu', 10, 'normal'))
    statBoard.create_text(260, 337.5, text=motm2, font=('Ubuntu', 10, 'normal'))

def go():
    uIn = search.get().upper().replace(' ', '')
    statBoard.create_rectangle(0, 0, 520, 350, fill='#e4e4e4', outline='#e4e4e4')
    if (('RUNS' in uIn) and ('MATCH' not in uIn) and ('INNINGS' not in uIn) and ('TEAM' not in uIn) and ('NO' not in uIn) and ('0' not in uIn) and ('ZERO' not in uIn)) or ('ORANGECAP' in uIn):
        runs()
    elif (('RUNS' in uIn or 'SCORE' in uIn) and ('MATCH' in uIn)) or (('RUNS' in uIn or 'SCORE' in uIn) and ('INNINGS' in uIn)) or (('RUNS' in uIn or 'SCORE' in uIn) and ('DAY' in uIn)) or (('RUNS' in uIn or 'SCORE' in uIn) and ('GAME' in uIn)):
        runs2()
    elif ('FOURS' in uIn) or ('4S' in uIn):
        fours()
    elif ('SIXES' in uIn) or ('6S' in uIn):
        sixes()
    elif ('STRIKERATE' in uIn):
        sr()
    elif ('FIFTIES' in uIn or '50S' in uIn or 'FIFTY' in uIn or '50' in uIn) and ('FASTEST' in uIn or 'QUICKEST' in uIn):
        f1()
    elif ('CENTURIES' in uIn or '100s' in uIn or 'CENTURY' in uIn or '100' in uIn) and ('FASTEST' in uIn or 'QUICKEST' in uIn):
        c1()
    elif ('FIFTIES' in uIn or '50S' in uIn or 'FIFTY' in uIn or '50' in uIn) and ('LARGEST' in uIn or 'MOST' in uIn or 'GREATEST' in uIn):
        f2()
    elif ('CENTURIES' in uIn or '100S' in uIn or 'CENTURY' in uIn or '100' in uIn) and ('LARGEST' in uIn or 'MOST' in uIn or 'GREATEST' in uIn):
        c2()
    elif ('BATTINGAVERAGE' in uIn):
        ba1()
    elif (('WICKETS' in uIn) and ('MATCH' not in uIn) and ('INNINGS' not in uIn)) or 'PURPLECAP' in uIn:
        wickets()
    elif 'MAIDENS' in uIn:
        maidens()
    elif 'DOTS' in uIn and ('INNINGS' not in uIn and 'GAME' not in uIn and 'MATCH' not in uIn):
        dots()
    elif ('DOTS' in uIn) and (('INNINGS' in uIn) or ('GAME' in uIn) or ('MATCH' in uIn) or ('DAY' in uIn)):
        dots2()
    elif 'BOWLINGAVERAGE' in uIn or 'BOWLINGAVERAGES' in uIn:
        ba2()
    elif ('ECONOMY' in uIn or 'ECONOMIES' in uIn) and (('INNINGS' not in uIn) and ('MATCH' not in uIn) and ('GAME' not in uIn) and ('DAY' not in uIn)):
        econ()
    elif ('ECONOMY' in uIn or 'ECONOMIES' in uIn) and (('INNINGS' in uIn) or ('MATCH' in uIn) or ('GAME' in uIn) or ('DAY' in uIn)):
        econ2()
    elif ('BOWLING' in uIn) and ('INNINGS' in uIn or 'FIGURES' in uIn):
        bf()
    elif ('CATCHES' in uIn):
        catches()
    elif ('VIP' in uIn) or ('PLAYERPOINTS' in uIn) or (('BEST' in uIn) and (('PLAYER' in uIn) or ('BATSMAN' in uIn) or ('PERSON' in uIn) or ('CRICKETER' in uIn))):
        pp()
    elif (('HIGHEST' in uIn) or ('LARGEST' in uIn) or ('MOST' in uIn)) and ('TEAM' in uIn) and (('SCORE' in uIn) or ('RUNS' in uIn) or ('POINTS' in uIn)):
        tp()
    elif ('DUCKS' in uIn) or (('NO' in uIn) or ('0' in uIn) or ('ZERO' in uIn)) and (('RUNS' in uIn) or ('SCORE' in uIn) or ('POINTS' in uIn)):
        ducks()
    elif ('STANDING' in uIn) or ('RANKING' in uIn):
        standings()
    elif ('VS' in uIn) or ('VERSUS' in uIn) or ('AGAINST' in uIn) or ('V' in uIn):
        match(uIn)
    elif (uIn in teamQueries) or (uIn in teams):
        tFunc(uIn)
    else:
        for x in range(len(players)):
            if (uIn == players[x]) or (uIn in players[x]) or (players[x] in uIn):
                pFunc(uIn)
                break
            if (x == len(players)-1) and ((uIn != players[x]) or (uIn not in players[x]) or (players[x] not in uIn)):
                statBoard.create_rectangle(0, 0, 550, 400, fill='#e4e4e4', outline='#e4e4e4')
                statBoard.create_text(260, 175, text='SORRY, I COULDN\'T UNDERSTAND YOUR SEARCH. \n                                         TRY AGAIN.', font=('Ubuntu', 20, 'bold'))
                
start = Button(main, text='Search', command=go)
start.grid(row=0, column=1)





