# pearson_correlation:
# this script uses the recommendations module
# to calculate pearson correlation scores between different critics
# it also prints out the most similar critic to each critic.
import recommendations
import operator
rating_pearson={}
for person1 in recommendations.critics:
    ratings={}
    for person2 in recommendations.critics:
        if person1 != person2:
            print(person1+', '+person2)
            ratings.update({person2:recommendations.sim_pearson(recommendations.critics, person1, person2)})
    rating_pearson.update({person1:ratings})
#rating_distance.sort()
print(rating_pearson)

#sort the distance by closest to 1 first.
#show the closest related person to each person.
closest_person = []
for person in rating_pearson.keys():
    sorted_pearson = sorted(rating_pearson.get(person).items(), key=operator.itemgetter(1), reverse=True)
    closest_person.append({person:sorted_pearson[0]})
print(closest_person)
