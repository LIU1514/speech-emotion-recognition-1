 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import shutil

emotion_dic = {'angry' : 0, 'fear' : 1, 'sad' : 2, 'happy' : 3, 'neutral' : 4}

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]

def test_data(config_file,model_file):

    config_path = os.path.join('./config',config_file+'.conf')
    model_path = os.path.join('./model',model_file)
    audio_path = '/test_audio'
    data_path = './output_data'
    if (os.path.isfile('./accuracy.txt')):
        os.remove('./accuracy.txt')

    n = 0; m = 0

    for key in emotion_dic.keys():
        data_create_dir = os.path.join(data_path,key)
        if not os.path.exists(data_create_dir):
            os.makedirs(data_create_dir)
        else:
            shutil.rmtree(data_create_dir)
            os.makedirs(data_create_dir)

    emotion_list = os.listdir(audio_path)

    for emotion in emotion_list: 
        if (os.path.isfile(emotion)):
            continue

        audio_sub_path = os.path.join(audio_path,emotion)
        data_sub_path = os.path.join(data_path,emotion)
        audio_list = os.listdir(audio_sub_path)
        # generate the .txt file comprising the name and value of result features for each speech
        for audio in audio_list:
            if audio[-4:]=='.wav':
                m += 1
                this_path_input = os.path.join(audio_sub_path,audio)
                this_path_output = os.path.join(data_sub_path,audio[:-4]+'.txt')
                # the second argument .conf determines which features would be extracted
                cmd = './opensmile-2.3.0/SMILExtract -C '+config_path+' -I '+this_path_input+' -O '+this_path_output
                os.system(cmd)
                # extract the feature values only
                f = open(this_path_output)
                last_line = f.readlines()[-1]
                f.close()
                os.remove(this_path_output)
                features = last_line.split(',') 
                del features[0]; del features[-1]

                label = emotion_dic.get(emotion,4)
                svm_format = "%d" % (label)  # add the emotion [label]
                # add [index1]:[value1] according to the libsvm format
                for i in range(0, len(features)):
                    svm_format = "%s %d:%s" % (svm_format,i+1,features[i])
                svm_format = svm_format + '\n'

                svm_data = open(this_path_output,'w')
                svm_data.write(svm_format)
                svm_data.close()

                cmd = './svm-predict '+this_path_output+' '+model_path+' '+'./result.txt'
                os.system(cmd)
                result_data = open('./result.txt','r')
                emotion_index = result_data.readlines()[-1]
                result_data.close()

                accuracy = "%s    %s : %s    " % (emotion + '-' + audio, emotion, get_key(emotion_dic,int(emotion_index)))
                if emotion_dic[emotion] == int(emotion_index):
                    accuracy = accuracy + 'True' + '\n'
                    n += 1
                else:
                    accuracy = accuracy + 'Wrong' + '\n'

                accuracy_data = open('./accuracy.txt','a')
                accuracy_data.write(accuracy)
    
    accuracy = accuracy + '\n' + "%s" % (float(n)/m)     
    accuracy_data.write(accuracy)      
    accuracy_data.close()

if  __name__ == '__main__':
    test_data('IS13_ComParE_Voc','SuckerModel1')