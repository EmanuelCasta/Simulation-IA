
import pickle
import time
import pandas as pd
import numpy as np
import os
import shutil
from pandas import json_normalize




def read(name="data.txt"):
    with open(f"preprocesordata/{name}", "rb") as f:
        obj = pickle.load(f)
    # Imprime [1, 2, 3, 4].
    for i in obj:
        print("")
        print("Cada Articulo")

        for k, v in i.items():
            print("===============")
            print(k+":  "+str(v))

       

def save(info,name='data.txt'):
    try:
        with open(f"tools/functional/preprocesordata/{name}", "wb") as f:
            pickle.dump(info, f)
        return
    except:
        with open(f"../tools/functional/preprocesordata/{name}", "wb") as f:
            pickle.dump(info, f)
        return

def delete_trash(names='ScienceDirect_'):
    
    file_destination =os.path.abspath(os.getcwd())+"\\"+"tools\\functional\\preprocesordata"
    
    file_source = 'C:\\Users\\Admin\\Downloads'
    get_files = os.listdir(file_source)
    for fichero in get_files:
        if os.path.isfile(os.path.join(file_source, fichero)):
                if fichero.startswith(names):
                    try:
                        os.remove(file_source+"\\"+fichero)
                        
                        break
                    except FileNotFoundError:
                        time.sleep(2)
                        if count >= 2:
                            count = 0    
                            print("[ADV] No found file delete")
                            break
                        count = count + 1
    get_files = os.listdir(file_destination)
    for fichero in get_files:
        if os.path.isfile(os.path.join(file_destination, fichero)):
                if fichero.startswith(names):
                    try:
                        os.remove(file_destination+"\\"+fichero)
                        
                        break
                    except FileNotFoundError:
                        time.sleep(2)
                        if count >= 2:
                            count = 0    
                            break
                        count = count + 1


def move(names='ScienceDirect_',extension = '.txt',number=0):

    count = 0
    file_destination =os.path.abspath(os.getcwd())+"\\"+"tools\\functional\\preprocesordata"
    
    file_source = 'C:\\Users\\Admin\\Downloads'
    
    get_files = os.listdir(file_source)
    for fichero in get_files:
        if os.path.isfile(os.path.join(file_source, fichero)) and fichero.endswith(".crdownload"):
                if fichero.startswith(names):
                    try:
                        file = open(file_source+"\\"+fichero)
                        file.close()
                     
                        break
                    except FileNotFoundError:
                        time.sleep(3)
                        if count >= 2:
                            count = 0    
                            print("[ERROR.1] No found file")
                            break
                        count = count + 1
        
        
    if names.startswith("ScienceDirect_"):
        get_files = os.listdir(file_source)
        
        deletes =[]
        dat= ""
        for fichero in get_files:
            if os.path.isfile(os.path.join(file_source, fichero)) and fichero.endswith(extension):
                if fichero.startswith(names):
                    
                    try:
                        file = open(file_source+"\\"+fichero,'r',encoding='utf-8')
                        dat = file.read() +'\n'+ dat
                        file.close()
                        time.sleep(1)
                        deletes.append(file_source+"\\"+fichero)
                        
                    except FileNotFoundError:
                        print("[ERROR.1] No found file")

        for na in deletes:
            os.remove(na)
        if dat != '':
            document = open(file_source+"\\"+names+".txt",'w',encoding='utf-8')
            document.write(dat)
            document.close()
            
    
    time.sleep(2)
    count = 0
    while True:
        get_files = os.listdir(file_source)
        try:
            for fichero in get_files:
                
                if os.path.isfile(os.path.join(file_source, fichero)) and fichero.endswith(extension):         
                    
                    if fichero.startswith(names):
                        file_oldname = os.path.join(file_source, fichero)
                        newName = fichero.split('.')[0]+str(number)+extension
                        file_newname_newfile = os.path.join(file_source,newName)

                        os.rename(file_oldname, file_newname_newfile)
                        shutil.move(file_source +"\\"+ newName, file_destination)
                        break
            
            print("[SAVE]  found file")
            return newName 
           
        except:
            time.sleep(1)
            if count >= 200:
                count = 0
                print("[ERROR PROBLEM] No found file")
                break
            count = count + 1

def generate_words(info):
    count =0
    combination =[]
    
    everyrule = []
    word = ""
    for count in range(len(info['NombreClave'])):
        word = ""
        rules ={'logic': [], 'words': [], 'condictional': '  "Image" AND NOT "Mhealth" '}
        for key, values in info.items():
            word = word+" " +values[count] 
            if key=="NombreClave":
                rules['words'].append(values[count])
            if key=="LogicaClave":
                rules['logic'].append(values[count])
            if key=="Nombrecaracteristica":
                rules['words'].append(values[count])
            if key=="LogicaCaracteristica":
                rules['logic'].append(values[count])
            if key=="NombreComplementario":
                rules['words'].append(values[count])
            if key=="LogicaComplementaria":
                rules['logic'].append(values[count]) 
        word = word + ' "Image" AND NOT "Mhealth"'
        combination.append(word)
        everyrule.append(rules)

    return combination,everyrule
        



           
        

def  organizated_data_Scopus(last=False):
    try:
        file_source =os.path.abspath(os.getcwd())+"\\"+"preprocesordata"
        get_files = os.listdir(file_source)
    except:
        file_source =os.path.abspath(os.getcwd())+"\\"+"tools\\functional\\preprocesordata"
        get_files = os.listdir(file_source)
    dataset =[]
    count = 0
    for fichero in get_files:
        
        if os.path.isfile(os.path.join(file_source, fichero)) and fichero.endswith('.csv'):                                      
            if fichero.startswith('scopus'):
                df = pd.read_csv(file_source+"\\"+fichero)
                df['nameFichero'] = fichero
                dataset.append(df)
                if last:
                    os.remove(file_source+"\\"+fichero)
                    break
    
    if dataset == []:
        return dataset
    df = pd.concat(dataset)
    df.reset_index(drop=True, inplace=True)
    return df
                     
def organizated_data_ScienceDirect(last=False):
    try:
        file_source =os.path.abspath(os.getcwd())+"\\"+"preprocesordata"
        get_files = os.listdir(file_source)
    except:
        file_source =os.path.abspath(os.getcwd())+"\\"+"tools\\functional\\preprocesordata"
        get_files = os.listdir(file_source)
    dataset =[]
   
    for fichero in get_files:
        if os.path.isfile(os.path.join(file_source, fichero)) and fichero.endswith('.txt'):                      
            if fichero.startswith('ScienceDirect_'):
                data =[]
                document = open(file_source+"\\"+fichero,'r',encoding='utf-8')
                datas = document.read()
                document.close()
                divisionData = datas.split(sep ='\n')
                newlist =[]
            
                for i in divisionData:
                    if i == '':
                        data.append(newlist)
                        newlist =[]
                        continue
                    newlist.append(i)    
                
                for values in data:
                    parameters ={ 'Authors':''
                        ,'Title':'',
                        'Source title':'',
                        'Volume':'',
                        'Issue':'',
                        'Year':'',
                        'Page start':'',
                        'Page end':'',
                        'DOI':'',
                        'Link':'',
                        'Abstract':'',
                        'Author Keywords':'',
                        "nameFichero":''}
                    parameters['nameFichero'] =fichero
                    count = 0
                    for value in values:
                        if ',' == value[-1:]:
                            value =value[:-1]
                        if count == 0:
                            parameters['Authors'] = value
                        if count == 1:
                            parameters['Title'] = value
                        if count == 2:
                            parameters['Source title'] = value
                        if value.startswith("20"):
                            parameters['Year']=value
                        if value.startswith("Vol"):
                            sublist = value.split(',')
                            try:
                                volsublist = sublist[0].strip().split(' ')[1]
                                parameters['Volume']=volsublist
                            except:
                                pass

                            try:
                                issusublist = sublist[1].strip().split(' ')[1]
                                parameters['Issue']=issusublist
                            except:
                                pass
                            
                        if value.startswith("https://doi.org/"):
                            parameters['DOI']=value
                        if value.startswith("Keywords"):
                            parameters['Author Keywords']=value
                        
                        if value.startswith("Pages"):
                            pagesplit = value.split('-')
                            parameters['Page start']=pagesplit[0].split(" ")[1]
                            parameters['Page end']=pagesplit[1]

                        if value.startswith("Abstract"):
                            sub = value
                            try:
                                if  'Background' in sub:
                                    sub =sub+" " +values[count+1] 
                            except:
                                pass
                            try:
                                sub_1 = values[count+2]
                                if 'Methods' in sub_1:
                                    sub =sub+" "+ values[count+3] 
                            except:
                                pass

                            try:
                                sub_2 = values[count+4]
                                if 'Results' in sub_2:
                                    sub =sub+" " +values[count+5] 
                            except:
                                pass

                            try:
                                sub_3 = values[count+6]
                                if 'Conclusion' in sub_3:
                                    sub =sub+" "+ values[count+7] 
                            except:
                                pass

                            parameters['Abstract']=sub 
                        if value.startswith("(https://www"):
                            parameters['Link']=value
                        count = count + 1
                    dataset.append(parameters)
                if last:
                    os.remove(file_source+"\\"+fichero)
                    break

    return  json_normalize(dataset)
            


            
   


    
if __name__ == "__main__":
    #print(move())
    
    try:
        read(name="Direct.txt")
    except:
        pass

    try:
        read(name="DataScopus.txt")
    except:
        pass

    #print(organizated_data_Scopus())
    print(organizated_data_ScienceDirect(last=True))
    #a['Source title'] =1
    #print(a)


    

