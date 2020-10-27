#define  the first function observed with no paremeters
def observed ():
    observations = []
    #populate the list 7 times with the user input
    for count in range (7):
        print("Please enter an observation:")
        observation = input()
        observations.append(observation)
    return observations
#second function with no paremeters 
def run():
    print("Counting observations...")
    observations = observed()
    observation_set = set()
    for observation in observations:
        observation_set.add((observation, observations.count(observation)))
    observation_tuple = (observation, observations.count(observation))
    print (f"{observation[0]} observed {observation[1]}")
run()