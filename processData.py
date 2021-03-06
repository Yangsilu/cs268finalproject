# this file process the data files into the regular csv file
import csv
import pdb
inputfile = 'data.fanduel.scsv'
outputfile = 'data.fanduel.formatted.scsv'

playerDict = {}

class Player():
    def __init__(self, name, team, pos):
        self.name = name
        self.team = team
        self.pos = pos
        self.history = []

class Stat():
    def __init__(self, date, salary, fantasypoint, stats):
        self.date = date
        self.salary = salary
        self.fantasypoint = fantasypoint
        self.statline = stats

    def __str__(self):
        return '{0} {1} {2}'.format(self.salary, self.fantasypoint, self.statline)

with open(inputfile, 'r') as csvinput:
    reader = csv.reader(csvinput, delimiter=';')
    reader.next() # remove the header
    dates = []
    for row in reader:
        [date, gid, pos, name, starter, fantasypoint, salary, team, homeaway, oppt, teamscore,\
                opptscore, minute, stats] = row

        fantasypoint = float(fantasypoint)
        stat = Stat(date, salary, fantasypoint, stats)
        if name in playerDict:
            p = playerDict[name]
        else:
            p = Player(name, team, pos)
            playerDict[name] = p
        p.history.append(stat)
        dates.append(date)
    pdb.set_trace()

dates = ['20151120', '20151121', '20151122', '20151123', '20151124', '20151125'\
        , '20151127', '20151128', '20151129', '20151130']

# outputing to the new csv
with open(outputfile, 'w') as csvoutput:
    writer = csv.writer(csvoutput, delimiter=';')
    for name in playerDict:
        p = playerDict[name]
        playerinfo = [p.name, p.team, p.pos]
        playerhistory = []
        for d in dates:
            hist = filter(lambda h:h.date==d, p.history)
            if hist:
                hist = hist[0]
                playerhistory += [hist.salary, hist.fantasypoint]
            else:
                playerhistory += ['NaN', 'NaN']
        row = playerinfo + playerhistory
        writer.writerow(row)
