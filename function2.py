import os

directory = "C:/Users/yum/Desktop/SIT/ICT1002-Prog fundamentals/Project/Sample data for assignment 1/"
male_profiles = {}
female_profiles = {}


def profile(input_file):
    user_profile = {'Books': []}
    for line_number, line in enumerate(input_file):
        if line_number < 8:
            key, value = line.rstrip().split(":", 2)
            user_profile[key] = value
        if line_number > 9:
            user_profile['Books'].append(line.rstrip())
    return user_profile


for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(directory + filename) as f:
            profiledict = profile(f)
            if "Female" in profiledict['Gender'] or "female" in profiledict['Gender'] or "F" in profiledict[
                'Gender'] or "f" in profiledict['Gender']:
                female_profiles[filename] = profiledict
            elif "Male" in profiledict['Gender'] or "male" in profiledict['Gender'] or "M" in profiledict[
                'Gender'] or "m" in profiledict['Gender']:
                male_profiles[filename] = profiledict


def male_to_female_country_match(male_profiles, female_profiles):
    matched_profiles_score = {}

    for maleprofile in male_profiles.values():

        matched_profiles_score[maleprofile['Name']] = {}

        for femaleprofile in female_profiles.values():

            if maleprofile['Country'] in femaleprofile['Acceptable_country'] and femaleprofile['Country'] in \
                    maleprofile['Acceptable_country']:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '2'
            elif maleprofile['Country'] in femaleprofile['Acceptable_country'] or femaleprofile['Country'] in \
                    maleprofile['Acceptable_country']:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '1'
            else:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '0'

    return matched_profiles_score


def female_to_male_country_match(male_profiles, female_profiles):
    matched_profiles_score = {}

    for femaleprofile in female_profiles.values():

        matched_profiles_score[femaleprofile['Name']] = {}

        for maleprofile in male_profiles.values():

            if femaleprofile['Country'] in maleprofile['Acceptable_country'] and maleprofile['Country'] in \
                    femaleprofile['Acceptable_country']:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '2'

            elif femaleprofile['Country'] in maleprofile['Acceptable_country'] or maleprofile['Country'] in \
                    femaleprofile['Acceptable_country']:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '1'

            else:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '0'

    return matched_profiles_score


def all_profile_country_match(male_profiles, female_profiles):
    matched_profiles_score = {}

    for maleprofile in male_profiles.values():

        matched_profiles_score[maleprofile['Name']] = {}

        for femaleprofile in female_profiles.values():

            if maleprofile['Country'] in femaleprofile['Acceptable_country'] and femaleprofile['Country'] in \
                    maleprofile['Acceptable_country']:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '2'

            elif maleprofile['Country'] in femaleprofile['Acceptable_country'] or femaleprofile['Country'] in \
                    maleprofile['Acceptable_country']:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '1'

            else:
                matched_profiles_score[maleprofile['Name']][femaleprofile['Name']] = '0'

    for femaleprofile in female_profiles.values():

        matched_profiles_score[femaleprofile['Name']] = {}

        for maleprofile in male_profiles.values():

            if femaleprofile['Country'] in maleprofile['Acceptable_country'] and maleprofile['Country'] in \
                    femaleprofile['Acceptable_country']:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '2'

            elif femaleprofile['Country'] in maleprofile['Acceptable_country'] or maleprofile['Country'] in \
                    femaleprofile['Acceptable_country']:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '1'

            else:
                matched_profiles_score[femaleprofile['Name']][maleprofile['Name']] = '0'

    return matched_profiles_score


male_to_female_country_scores = male_to_female_country_match(male_profiles, female_profiles)
female_to_male_country_scores = female_to_male_country_match(male_profiles, female_profiles)
all_profiles_country_scores = all_profile_country_match(male_profiles, female_profiles)

"""
for x in male_to_female_country_scores:
    print (x)
    for y in male_to_female_country_scores[x]:
        print y + ':' + male_to_female_country_scores[x][y]
    print '\n'

for x in female_to_male_country_scores:
    print (x)
    for y in female_to_male_country_scores[x]:
        print y + ':' + female_to_male_country_scores[x][y]
    print '\n'


for x in all_profiles_country_scores:
    print (x)
    for y in all_profiles_country_scores[x]:
        print y + ':' + all_profiles_country_scores[x][y]
    print '\n'

"""