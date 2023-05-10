class MatchResult():
    def __init__(self, data, season, round):
        self.season = season
        self.round = round

        try:
            self.date_time = [x.strip() for x in data[0].split(',')]
        except:
            self.date_time = [None, None]

        self.location = data[1].strip()

        try:
            self.teams = [x.strip() for x in data[2].split(' - ')]
        except:
            self.teams = [None, None]

        try:
            self.result = [int(x) for x in data[3].split(':')]
        except:
            self.result = None

        if data[4] != '?':
            self.attendance = int(data[4].replace('.', ''))
        else:
            self.attendance = 0

    def __str__(self):
        return '%s/%s | %s @ %s | %s -> %s (%s viewers)' % (self.season, self.round, ' '.join(self.date_time), self.location, ' VS '.join(self.teams), ':'.join(map(str,self.result)), self.attendance)
    
    def to_dict(self):
        #ISSUE: date_time[1] doesn't always exist
        try:
            return {
                'season': self.season,
                'round': self.round,
                'date': self.date_time[0],
                'time': self.date_time[1],
                'location': self.location,
                'team1': self.teams[0],
                'team2': self.teams[1],
                'result1': self.result[0],
                'result2': self.result[1],
                'attendance': self.attendance
            }
        except:
            return {}