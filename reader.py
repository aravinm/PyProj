def profile(input_file):
    user_profile = {'Books':[]}
    for line_number,line in enumerate(input_file):
        if line_number < 8:
            key,value = line.rstrip().split(':',2)
            if line_number in (3,6,7):
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

