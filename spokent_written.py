

class convert_spoken_text_to_written():
  def __init__(self):
    '''This method intializes the conversion rules'''
    self.rules= {"single words":{
                          "zero": '0',
                          "one" : '1',
                          "two": '2',
                          "three": '3',
                          "four": '4',
                          "five": '5',
                          "six": '6',
                          "seven": '7',
                          "eight": '8',
                          "nine": '9',
                          "ten": '10',
                          "twenty": '20',
                          "thirty": '30',
                          "forty": '40',
                          "fourty": '40',
                          "fifty": '50',
                          "sixty": '60',
                          "seventy": '70',
                          "eighty": '80',
                          "ninety": '90',
                          "hundred": '100',
                          "thousand":"K",
                          "million":"M",
                          "billion":"B",
                          "single":'1',
                          "double":'2',
                          "triple":'3',
                          "quadruple":'4',
                          "quintuple":'5',
                          "sextuple":'6',
                          "septuple":'7',
                          "octuple":'8',
                          "nonuple":'9',
                          "decuple":'10'}
  ,"Double Word":{
                            "C M": "CM",
                            "P M": "PM",
                            "D M": "DM",
                            "A M": "AM",

                        }}
  def convert(self,text):
    '''This method converts the spoken text to written'''
    b=text.split()
    c=[]
    i=0
    while i<len(b):
      if (b[i]=='dollar') or (b[i]=='dollars'):
          tmp=c[-1]
          c[-1]="$"
          c.append(tmp)
          i=i+1
          continue
      if b[i] in list(rules['single words'].keys()):

          c.append(self.rules['single words'][b[i]])
          i=i+1
          continue
      elif i<(len(b)-1) and  (b[i]+' '+(b[i+1][0])) in list(rules['Double Word'].keys()):
          c.append(self.rules['Double Word'][b[i]+' '+b[i+1][0]])
          i=i+2
          continue
      else:
          c.append(b[i])
          i=i+1
          continue
    return ' '.join(c)


