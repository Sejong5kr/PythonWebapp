import pickle

class AthleteList(list):
    def __init__(self, a_name, a_dob, a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
    
    def top3(self):
        return(sorted(set(self))[0:3])

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    
    (min, sec)=time_string.split(splitter)
    return(min+'.'+sec)

def getCoachData(fileName):
    try:
        with open(fileName) as f:
            data=f.readline()
        data_list=data.strip().split(',')

        clean_data=[]
        for each_t in data_list:
            clean_data.append(sanitize(each_t.strip()))

        return(AthleteList(clean_data.pop(0),clean_data.pop(0),clean_data))

    except IOError as ioerr:
        print("File error:"+str(ioerr))
        return(None)


def put_to_store(files_list):
    all_athletes={}
    for each_file in files_list:
        ath= getCoachData(each_file)
        all_athletes[ath.name]=ath  #Each athelete's name is used as the "key" in the dictionary
    
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_to_store):'+str(ioerr))
    
    return(all_athletes)

def get_from_store():
    all_athletes={}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes=pickle.load(athf)
    
    except IOError as ioerr:
        print('File error(get_from_store):'+str(ioerr))

    return(all_athletes)




