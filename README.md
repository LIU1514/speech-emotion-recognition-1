# Speech Emotion Recognition
![Hackathon logo](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1560831611&di=22db538d48595890560224f8d692d7ed&imgtype=jpg&er=1&src=http%3A%2F%2Fphotocdn.sohu.com%2F20151105%2Fmp39895639_1446700026815_5.jpeg)

This project is based on the open source tool ***openSmile*** [here](https://www.audeering.com/opensmile/). It aims to extract audio features from the speech, thus recognizing the emotion what the utterance embodies. In addition, this project is one of the projects of ***Ximalaya*** ® 's Hackathon.

## Installation

### macOS

It is tricky to compile openSmile on macOS. Basically, you can refer to this [link](https://blog.csdn.net/weixin_42120869/article/details/80837216).

### win

You can simply use the release version in **/bin/Win32** or you can compile it. The official guidance is on the webpage of ***openSmile***, **Installation and Documentation** part.

## Corpus

**CASIA** is a corpus that published by ***Chinese Linguistic Data Consortium (CLDC)***. Four professional speakers are required to utter 200 non-parallel sentences in five emotions. There are 1,000 sentences in all which can be used in the research about emotional speech.

## Usage

The basic introduction of ***openSmile*** is [here](https://blog.csdn.net/lccever/article/details/78621892). 
For our specific project, you can use command tool to run this executable file like this:

```
SMILExtract -C ./opensmile/opensmile-2.3.0/config/IS09_emotion.conf -I ./opensmile/audio/in/1.wav -O ./opensmile/audio/out/1.txt
```

The first argument **-C** should be followed by a config file that determines which features to extract. The config files are contained by the directory **/config** The second argument **-I** is the audio input while the last argument is the result.

Or you can directly use our ***feature_extraction.py*** to run this specific project.