import os

def profile(input_file):
    try:
        user_profile = {'Books':[]}
        for line_number,line in enumerate(input_file):
            if line_number < 8:
                key,value = line.rstrip().split(':',2)
                if line_number == 1:
                    value = value.strip()[0].upper()
                elif line_number in (3,6,7):
                    value = set(c.strip() for c in value.split(',') if c)
                elif line_number == 4:
                    value = int(value.strip())
                elif line_number == 5:
                    min_age, max_age = value.split('-')
                    value = range(int(min_age), int(max_age))
                else:
                    value = value.strip()
                user_profile[key] = value
            if line_number >9:
                user_profile['Books'].append(line.rstrip())
        return user_profile
    except:
        return None

def profiles_from(directory):
    male_profiles, female_profiles = {}, {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(directory + filename) as f:
                profiledict = profile(f)
                if profiledict:
                    if profiledict['Gender'] == 'F':
                        female_profiles[filename] = profiledict
                    elif profiledict['Gender'] == 'M':
                        male_profiles[filename] = profiledict
                else:
                    return None, None
    return male_profiles, female_profiles


def read_txt(name,directory='' ):
    with open(directory+name) as f:
        return f.read()

def read_all_from(profiles):
    profile_text = ''
    for filename in profiles:
        profile_text += read_txt(filename)+'\n\n'
    return profile_text
