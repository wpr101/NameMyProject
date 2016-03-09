from flask import Flask, render_template, request, redirect
import os, string
#import nltk
#from nltk.corpus import stopwords

import ChooseWord as cw
import CustomNames as cn

app = Flask(__name__)

@app.route('/')
def index():
    
    describe_projects = cw.create_thesaurus_name()

    return render_template('tabbedindex.html',
                           describe_projects = describe_projects)

@app.route('/<string:user_word>')
def CustomName(user_word):

    word_list = user_word.split('-')
    project_names = cn.custom_names(word_list)
    
    return render_template('customnames3.html',
                           project_names = project_names,
                           user_word = user_word)

@app.route('/CustomWords', methods=['GET'])
def CustomWords():
	user_word = request.args['words']
	#translator = str.maketrans({key: None for key in string.punctuation})
	#user_word = user_word.translate(translator)
	punct = set(string.punctuation)
	user_word = ''.join(x for x in user_word if x not in punct)

	word_list = user_word.split()
	for i in range(len(word_list)):
	    word_list[i] = word_list[i].capitalize()
		
        #remove duplicates from the list
	word_list = list(set(word_list))
	
	stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
	for s in stop:
	    for w in word_list:
                if (s.capitalize() == w):
                    word_list.remove(w)
	
		
	redirect_string = '/'
	for i in range(len(word_list)):
	    redirect_string += word_list[i] 
	    redirect_string += "-"
	#remove the trailing slash
	redirect_string = redirect_string[:-1]
	
	word_list = user_word.split('-')
	
	return redirect(redirect_string)
	


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=33507)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
