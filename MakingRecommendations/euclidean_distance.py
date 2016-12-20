import recommendations
import operator
rating_distance={}
for person1 in recommendations.critics:
    ratings={}
    for person2 in recommendations.critics:
        if person1 != person2:
            print(person1+', '+person2)
            ratings.update({person2:recommendations.sim_distance(recommendations.critics, person1, person2)})
    rating_distance.update({person1:ratings})
#rating_distance.sort()
print(rating_distance)

#sort the distance by closest to 1 first.
#show the closest related person to each person.
closest_person = []
for person in rating_distance.keys():
    sorted_distance = sorted(rating_distance.get(person).items(), key=operator.itemgetter(1), reverse=True)
    closest_person.append({person:sorted_distance[0]})
print(closest_person)
