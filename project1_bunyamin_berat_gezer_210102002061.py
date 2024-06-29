my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"




def read_file(filename="test_puzzle.txt") :
    filename= open(filename,"r")

    new_list_total=[]
    words=[]
    board=[]
    words1=filename.readlines()
    for w in words1 :    
        w=w.replace("\n","")
        new_list_total.append(w)
    
    for i in new_list_total:
        if i=="" :
            break

        words.append(i)

    for i in new_list_total:
        if i in words : 
            continue
        board.append(i)
    board.pop(0)
    return words,board
print(read_file("sample_puzzle.txt"))


def check_consistency(board):

    for i in range(len(board)) : 
        if len(board[i-1]) != len(board[i]):
            return False
    return True
        
        


def create_board(board):
    list1=[]
    list2=[]

    for i in board:
        for n in i : 
            list1+=[int(n)]
        list2+=[list1]
        list1=[]
    board.clear()
    for i in list2 : 
        board.append(i)    





def identifier(words):
    id_list_words=[]
    for i in words:
        id_list_words+=[False]
    return id_list_words





def print_board(board) :

    board_showing=""
    t_f=False
    for i in board:
        while t_f==True:
            board_showing+="\n"
            t_f=False
        t_f=True
            
        for x in i : 
            if 1==x :
                board_showing+="   "
            elif 0==x:
                board_showing+="+"
    


def print_board_w_c(board) : 
    r=0
    w_c_board="   "
    t_f=False
    for i in board:        
        for c in range(len(i)):
            w_c_board+="C{}".format(int(c)+1)
        break
    w_c_board+="\n"

    
    for i in board:
        if t_f==True:
            w_c_board+="\n"
        t_f=True

        w_c_board+="R{}".format(int(r)+1) 
        r+=1
        
        for x in i :
            if x == 1 :
                w_c_board+="   "
            elif x==0:
                w_c_board+=" +"
            

    

def print_wordlist(words,wstatus):
    number=1
    boşluk=" "
    str_showing_status_board=""
    str_showing_status_board+="WORD LİST            Status"+"\n"
    for i in words:
        str_showing_status_board+="W{}".format(number)+"  "
        
        str_showing_status_board+=str(i)
        str_showing_status_board+=boşluk*(16-len(words))   
        if wstatus[number-1]==False:
            str_showing_status_board+="NOT USED"
        elif wstatus[number-1]==True:
            str_showing_status_board+="USED"
        number+=1
        str_showing_status_board+="\n"

    






def check_entries(coordinates,wordno,board,words):

    check_coordinates=True
    check_word_no=True
    if  len(board)>=coordinates[0] and len(board[0])>=coordinates[1]:
        check_coordinates=True
    else :
        check_coordinates=False
    
    if wordno <= len(words) and wordno>0:
        check_word_no=True
    else :
        check_word_no=False
    

    return check_coordinates,check_word_no 


    

def check_location(board,words,coordinates,wordno,direction='H') : 


    output1=True
    output2=0


    if board[coordinates[0]-1][coordinates[1]-1]== "0":
        output1=False
        output2=1
    


    if output1==True and direction=="V" and coordinates[0]-2>=0 and coordinates[1]-1>=0 and board[coordinates[0]-2][coordinates[1]-1]=="1":
        output1=False
        output2=2
     

    
    if output1==True and direction=="H" and  coordinates[0]-1>=0 and coordinates[1]-2>=0 and board[coordinates[0]-1][coordinates[1]-2]=="1":
        output1=False
        output2=3



    if output1==True and direction=="H" and len(board[0])<len(words[wordno-1]):
        output1=False
        output2=4
    

    if output1==True and direction=="V" and len(board)<len(words[wordno-1]):
        output1=False
        output2=7



    if output1==True and direction=="H":
        r=0
        for i in range(coordinates[1]-1,len(board[coordinates[0]-1])):
            a=board[coordinates[0]-1][i]
            if int(a) == 1 or board[coordinates[0]-1][i]==words[wordno-1][i]:
                r+=1
            else:
                break 
        if r<len(words[wordno-1]):
            output1=False
            output2=5



    if output1==True and direction=="V":
        new_a=0
        for i in range(coordinates[0]-1,len(board)):
            c=board[i][coordinates[1]-1]
            if int(c)==1 or  board[i][coordinates[0]-1]==words[wordno-1][i]:
                new_a+=1
            else:
                break
        if new_a<len(words[wordno-1]):
            output1=False
            output2=8



    if output1==True and direction=="H":
        r=0
        for i in range(coordinates[1]-1,len(board[coordinates[0]-1])):
            a=board[coordinates[0]-1][i]
            if int(a) == 1:
                r+=1
            else:
                break 
        if r>len(words[wordno-1]):
            output1=False
            output2=6


    if output1==True and direction=="V":
        new_a=0
        for i in range(coordinates[0]-1,len(board)):
            c=board[i][coordinates[1]-1]
            if int(c)==1:
                new_a+=1
            else:
                break
        if new_a>len(words[wordno-1]):
            output1=False
            output2=9
    


    return output1,output2
    











def check_word_fits(board,words,coordinates,wordno,direction='H'):
    

    check_word_fits_t_f=True
    check_word_fits_c_n=0
    
    if coordinates=="V":    
        for i in range(len(words[wordno-1])):

            if board[coordinates[0]-1+i][coordinates[1]-1]== 1 :
                continue
            else:
                check_word_fits_t_f=False
                check_word_fits_c_n=2
        check_word_fits_t_f=True
        check_word_fits_c_n=0

    if coordinates=="V":

        for i in range(len(words[wordno-1])):
            a=words[wordno-1][i]

            if a==board[coordinates[0]-1+i][coordinates[1]-1] or board[coordinates[0]-1+i][coordinates[1]-1]==1 :
                continue
            else:
                check_word_fits_t_f=False
                check_word_fits_c_n=2
        check_word_fits_t_f=True
        check_word_fits_c_n=0

    if coordinates=="H":
        for i in range(len(words[wordno-1])):
            if board[coordinates[0]-1][coordinates[1]-1+i]== 1 :
                continue
            else:
                check_word_fits_t_f=False
                check_word_fits_c_n=1
        check_word_fits_t_f=True
        check_word_fits_c_n=0

    if coordinates=="H":
        for i in range(len(words[wordno-1])):
            a=words[wordno-1][i]

            if a==board[coordinates[0]-1][coordinates[1]-1+i] or board[coordinates[0]-1][coordinates[1]-1+i]==1 :
                continue
            else:
                check_word_fits_t_f=False
                check_word_fits_c_n=1
        check_word_fits_t_f=True
        check_word_fits_c_n=0
    return check_word_fits_t_f,check_word_fits_c_n    




def clear_board(board,wstatus):

    for i in range(len(wstatus)):
        if wstatus[i]==True:
            wstatus.pop(i)
            wstatus.insert(0,False)
        else:
            continue
    
    for i in range(len(board)):
        for x in range(len(board[i])):
            if board[i][x]== 1 or board[i][x]== 0 :
                continue
            else:
                board[i].pop(x)
                board[i].insert(x,1)









def decompose_command(str1) :
    output1=0
    output2=0
    output3=0
    output4=0
    str1=str1.upper()
    coordinate=[]
    

    for i in str1:
        if  i=="W":
            if type(int(str1[str1.index("W")+1])) == int :
                output1=0  
            else:
                output1=-1
        if i=="R":        
            if type(int(str1[str1.index("R")+1])) == int :
                output1=0
            else:
                output1=-1
        if i=="C":
            if type(int(str1[str1.index("C")+1])) == int :
                output1=0
            else:
                output1=-1    
                
        

    if "W" in str1 and "C" in str1 and "R" in str1 and "D" in str1 :         
        output1=0
    else : 
        output1=-1

    if output1==0:
        for x in str1:
            if x =="W":
                if str1.index("W")==6 or str1.index("W")==7 or  str1.index("W")==8 : 
                    w1=str1[str1.index("W")+1]
                    w2=str1[-1]
                    
                    for i in range(99):
                        if w1 == str(i)   :
                            w1=str(i)
                            print(id(w1))
                            w=w1
                            w1=str1[str1.index("W")+1]
                            
                            break
                    if int(id(w1)) == int(id(w2)):
                        break       
                    else:
                         
                        w=w1+w2 
                        break 
                else:    
                    w1=str1[str1.index("W")+1]
                    w2=str1[str1.index("W")+2]
                    for i in range(99):
                        if w1 == str(i)   :
                            w1=str(i)
                            w=w1
                            continue
                        
                        if w2 == str(i) :
                            w2=str(i)  
                            w=w1+w2 
                            break 
        output2=int(w)
        
    if output1==-1:
        output2=None

    if output1==0:

        
        for x in str1:
            if x =="C":
                if str1.index("C")==6 or str1.index("C")==7 or  str1.index("C")==8 : 
                    c1=str1[str1.index("C")+1]
                    c2=str1[-1]
                    
                    for i in range(99):
                        if c1 == str(i)   :
                            c1=str(i)
                            print(id(c1))
                            c=c1
                            c1=str1[str1.index("C")+1]
                            
                            break
                    if int(id(c1)) == int(id(c2)):
                        break       
                    else:
                         
                        c=c1+c2 
                        break 
                else:    
                    c1=str1[str1.index("C")+1]
                    c2=str1[str1.index("C")+2]
                    for i in range(99):
                        if c1 == str(i)   :
                            c1=str(i)
                            c=c1
                            continue
                        
                        if c2 == str(i) :
                            c2=str(i)  
                            c=c1+c2 
                            break


            
                        
                    
            if x =="R":
                if str1.index("R")==6 or str1.index("R")==7 or  str1.index("R")==8 : 
                    r1=str1[str1.index("R")+1]
                    r2=str1[-1]
                   
                    for i in range(99):
                        if r1 == str(i)   :
                            r1=str(i)
                            
                            r=r1
                            r1=str1[str1.index("R")+1]
                            
                            break
                    if int(id(r1)) == int(id(r2)):
                        break       
                    else:
                         
                        r=r1+r2 
                        break 
                else:    
                    r1=str1[str1.index("R")+1]
                    r2=str1[str1.index("R")+2]
                    for i in range(99):
                        if r1 == str(i)   :
                            r1=str(i)
                            r=r1
                            continue
                        
                        if r2 == str(i) :
                            r2=str(i)  
                            r=r1+r2 
                            break

        coordinate.append(int(r))
        coordinate.append(int(c))

        output3=coordinate
    if output1==-1:
        output3=None

    if output1==0:
        if str1[str1.index("D")+1] =="V":
            output4="V"
        else:
            output4="H"
    if output1==-1:
        output4=None


    return output1,output2,output3,output4
    



 


def word_it(board,words,wstatus,coordinates,wordno,direction):
    a=check_location(board,words,coordinates,wordno,direction='H')== (True,0)
    b=check_word_fits(board,words,coordinates,wordno,direction='H')==(True,0)
    c=wstatus[wordno-1]
    if a==True and b==True and c==False:
        if direction=="H":
            for i in range(len(board)):
                if board[i][coordinates[1]-1]==1 or words[wordno-1][i]==board[i][coordinates[1]-1]:
                    board.pop(board[i][coordinates[1]-1])
                    board.insert(board[i][coordinates[1]-1],words[wordno][i])
                    
                    wstatus.pop(wordno-1)
                    wstatus.insert(wordno-1)



        return True
    else:
        return False


        




           
def copy_board(board):
    copy=[x[:] for x in board]

    return copy


 

def track_move(mvn,trackboard,coordinates,wordno,direction,board,wstatus):
    copy= wstatus [:]
    mvn+=1
    trackboard.append((coordinates,wordno,direction,copy_board(board),copy))
    return mvn


def check_solved(board):
    list1=[]
    t_x=True
    if t_x==True:

        for i in range(len(board)):
            for r in range(len(board[0])):
                list1.append(board[i][r])


        if 1 not in list1:
            return True
        else:
            return False


    


def solve_board(board,words):
    pass


def word_puzzle():
    pass



     
                
            

        
            
            











    
    
    
















































            






    

        
    
   

        

        






    
    

