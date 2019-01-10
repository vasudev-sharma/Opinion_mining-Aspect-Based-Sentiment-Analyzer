
from __future__ import division


class Unsupervised(): 
    '''
    Source:
	Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA,
    Download lexicon at: http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar
	"""
    '''


    PATH_TO_LEXICONS = "opinion-lexicon-English/"

    def __init__(self):
        """
        Read in the lexicons. 
        """

        pos_path = self.PATH_TO_LEXICONS + "positive-words.txt"
        neg_path = self.PATH_TO_LEXICONS + "negative-words.txt"

        self.pos_lex = self.read_lexicon(pos_path)
        self.neg_lex = self.read_lexicon(neg_path)


    def read_lexicon(self, path):
        '''
        INPUT: LiuFeaturizer, string (path)
        OUTPUT: set of strings
        Takes path to Liu lexicon and 
        returns set containing the full 
        content of the lexicon. 
        '''

        start_read = False
        lexicon = set() # set for quick look-up

        with open(path, 'r') as f: 
            for line in f: 
                if start_read:
                    lexicon.add(line.strip())
                if line.strip() == "":
                    start_read = True
        return lexicon


    def predict(self, tokenized_sent):
        '''
        INPUT: list of strings
        OUTPUT: 
        Note: tokens should be a list of 
        lower-case string tokens, possibly
        including negation markings. 
        '''
#        doc_len = len(tokenized_sent)
        #features = {}
#        assert doc_len > 0, "Can't featurize document with no tokens." 
        if(len(tokenized_sent)!=0):
                num_pos = sum([1 if tok in self.pos_lex else 0 for tok in tokenized_sent])
                num_neg = sum([1 if tok in self.neg_lex else 0 for tok in tokenized_sent])
        
                #features['liu_pos'] = num_pos/doc_len
                #features['liu_neg'] = num_neg/doc_len
        
                score = (num_pos - num_neg)/len(tokenized_sent)        
                return score
        else:
            return 0
                #return 1 if score > 0.5 else 0






