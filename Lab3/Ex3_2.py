def add_score(subject_score, student , subject , score) :
    if student not in subject_score :
      subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score

def calc_average_score(subject_score) :
    sum = 0
    count = 0
    id = ''
    for k in subject_score :
      id = k
      for a,b in subject_score[k].items() :
        sum += b
        count += 1
    avg = sum/count
    return ({id :"%.2f" % round(avg,2)})
    