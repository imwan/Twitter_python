import sys
import json
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans



def userCluster(filename,k, min_ngram=1,max_ngram=1,min_df=1,max_df=0.8,with_idf=True,max_features=8):
    '''
    filename: This is the path to the JSONL filename that we want to analyze.
    k: number of clusters
    min-df:this is the minimum document-frequency
    max-df:this is the maximum document frequency for a feature
    min-ngram: this the lower boundary for n-grams to be extracted
    max-ngram:this is the upper boundary for n-grams to be extracted
    no-idf: whether to use idf to rescale the weight
    '''
    if min_ngram > max_ngram:
        print("Error: incorrect value for --min-ngram ({}): it can't be higher than --max-value ({})".format(min_ngram, max_ngram))
        sys.exit(1)
    with open(filename) as f:
        # load data
        users = []
        for line in f:
            profile = json.loads(line)
            users.append(profile['description'])
        # create vectorizer
        vectorizer = TfidfVectorizer(max_df=max_df,
                                     min_df=min_df,
                                     max_features=max_features,
                                     stop_words='english',
                                     ngram_range=(min_ngram, max_ngram),
                                     use_idf=with_idf)
        # fit data
        X = vectorizer.fit_transform(users)
        print(X)
        #print("Data dimensions: {}".format(X.shape))
        # perform clustering
        km = KMeans(n_clusters=k)
        km.fit(X)
        clusters = defaultdict(list)
        for i, label in enumerate(km.labels_):
            clusters[label].append(users[i])
        # print 10 user description for this cluster
        for label, descriptions in clusters.items():
            print('---------- Cluster {}'.format(label))
            for desc in descriptions[:10]:
                print(desc)
    return clusters