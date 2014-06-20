class Athlete:
    def __init__(self, name, times = []):
        self.name = name
        self.times = times
        
    def top3(self):
        return sorted(self.times)[0:3]

    def add_time(self, value):
        self.times.append(value)

    def add_times(self, value):
        self.times.extend(value)

class AthleteList(list):
    def __init__(self, name, times = []):
        list.__init__(self)
        self.name = name

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs

def get_coach_data(filename):
    try:
        with open(filename) as f:
            flist = list(set([sanitize(each) for each in f.readline().strip().split(',')]))
        return Athlete(filename.split('.')[0], flist)
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None
    
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
roy = get_coach_data('roy.txt')

print james.name + '\'s fastest time ->' + str(james.top3())
print julie.name + '\'s fastest time ->' + str(julie.top3())
print mikey.name + '\'s fastest time ->' + str(mikey.top3())
print sarah.name + '\'s fastest time ->' + str(sarah.top3())

