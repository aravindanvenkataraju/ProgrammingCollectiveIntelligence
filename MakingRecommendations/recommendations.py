# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum_of_squares=sum((prefs[person1][item]-prefs[person2][item])**2
                       for item in prefs[person1] if item in prefs[person2])
    return 1/(1+sum_of_squares**0.5)

def sim_pearson(prefs, person1, person2):
    si=[]
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)

    n = len(si)

    # if no common ratings, return 0
    if n ==0 : return 0
    
    #sum of ratings
    person1_sum = sum(prefs[person1][movie] for movie in si)
    person2_sum = sum(prefs[person2][movie] for movie in si)

    #sum of squares of ratings
    person1_sqsum = sum(prefs[person1][movie]**2 for movie in si)
    person2_sqsum = sum(prefs[person2][movie]**2 for movie in si)

    #sum of products of rating by person1 and person2
    prdt_sum = sum(prefs[person1][movie]*prefs[person2][movie] for movie in si)

    #numerator : prdt_sum -(product of sum of ratings/number of ratings)
    numerator = prdt_sum - (person1_sum*person2_sum/n)

    #denomenator : square root of (product of(sum of square of rating-(sum of ratings)^2/n))
    denominator = ((person1_sqsum-(person1_sum**2/n))*(person2_sqsum-(person2_sum**2/n)))**0.5

    if denominator == 0 : return 0

    return numerator/denominator

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(prefs, person,other), other)
            for other in prefs if other !=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def topRecommendations(prefs, person, similarity=sim_pearson):
    total={}
    simSums={}
    for others in prefs:
        if others != person:
            sim=similarity(prefs, person, others)
            if sim > 0:
                for item in prefs[others]:
                    if item not in prefs[person] or prefs[person][item]==0:
                        total.setdefault(item, 0)
                        total[item] += prefs[others][item]*sim
                        simSums.setdefault(item, 0)
                        simSums[item] += sim
    rankings = [(total/simSums[item], item) for item, total in total.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

                        
