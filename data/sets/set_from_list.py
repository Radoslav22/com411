def observed():
    observations = []

    for count in range(7):
        print("Please enter an observation:")
        item = input()
        observations.append(item)
    return observations
def run():
    print("Counting observations...")
    observations = observed()
    observations_set = set()
    for observation in observations:
        occurrences = observations.count(observation)
        observations_set.add( (observation, occurrences))
    for key, value in observations_set:
        print(f"{key} observed {value} times")
   

run()