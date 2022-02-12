def matching_algo(person_a, person_b):
    interests_a = set([x.name.lower() for x in person_a.interests])
    interests_b = set([x.name.lower() for x in person_b.interests])
    return len(interests_a & interests_b)
