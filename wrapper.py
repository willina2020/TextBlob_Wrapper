from textblob import TextBlob



class blobwrapper:
  text=''
  
  
  def _check_arguments(self, text):
        """
        Checks if the passed argument and the text variable are empty. If they are the function raises a ValueError.
        If the argument text varibale is not empty it will be set as class variable.
        :param text: the input argument to check
        """
        if text == '':
            if self.text == '':
                raise ValueError('You have to pass a text or set the `self.text` variable of this class to tokenize a '
                                 'text')
        else:
            self.text = TextBlob(text)
            
   def pos_tagging(self, text=''):
       self._check_arguments(text)
       pos= self.text.tags
       return pos
    
    
   def noun_phrase_extraction(self,text=''):
       self._check_arguments(text)
       noun= self.text.noun_phrases
       return noun
    
   
  def sentiment_analysis (self, text=''):
      self._check_arguments(text)
      sent= self.text.sentiment
      return sent
  def polarity (self, text=''):
      self._check_arguments(text)
      pol= self.text.sentiment.polarity
      return pol
  def subjectivity (self, text=''):
      self._check_arguments(text)
      subj= self.text.sentiment.subjectivity
      reurn subj
      
      
   def word_tokenization (self, text=''):
       self._check_arguments(text)
       wordz= self.text.words
       return wordz
    
    def sentence_tokenization (self, text=''):
      self._check_arguments(text)
      sentz= self.text.sentences
      return sentz
    
    
    
      
      
