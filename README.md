# TTS
EC504 Advanced Data Structures final project

<br/>
We selected a text to speech engine because there is nothing quite like it suggested in the example project list. Text to speech via concatenative speech synthesis is an algorithmic approach to this problem without using machine learning. To perform signal processing on the training data of speech including every consonant, vowel, diphthong, and consonant cluster, we must use a custom hash function to support constant time amortized O(1) lookup for all possible pronunciations of these speech segments. This first step of the pipeline will support processing the training data into a custom python dictionary via the custom hash function which has a key including individual characters of consonants, vowels, or diphthongs, or two-three character strings including consonant clusters as consonant digraphs or trigraphs and vowel trigraphs. Examples of consonants or vowels as /e/ for e, /æ/ for a, or /k/ for k, diphthongs such as /eɪ/ (cake, eight), /oʊ/ (boat, rope), /aɪ/ (hi, bite, right), /aʊ/ (wow, about), /ɔɪ/ (boy, avoid), and consonant clusters broken into consonant digraphs and trigraphs, respectively, /ch/, /ck/, /gh/, /kn/, /mb/, /ng/, /ph/, /sh/, /th/, /wh/, /wr/, and /nth/, /sch/, /scr/, /shr/, /spl/, /spr/, /squ/, /str/, /thr/, vowel trigraphs including /eau/, /eou/, /iou/. 
We are using a hashtable to store our voice file of pronunciations, with keys being the possible combinations of diphones, and value being the file that contains the pronunciation of that diphone. After some test runs with linear probing, quadratic probing, and random probing, the use of several hash functions proved that a linear probing method + DJB2 Hash with the result of this hash modulo 2000 gives the best result. If we set to a higher value, then the computational space complexity will be higher because more memory would have to be allocated for the hash table, but with a higher value, the chance of collision will be lower, and reduce the search time because if a match is not found at the result location, we will have to search the next location, which takes O(1) time because we are implementing our hash table with a linked list. A linked list has a pointer that points to the next node from the last node, so when searching for the next possible node, we are only having the amortized cost of O(1),  thus we are trading space with time. Here the we picked modulo by 2000 is because we know our total file size is 1642 files, and 1642 is not a big number, thus setting the modulo value too high will not result in too much of an improvement, after some testing, we found that 2000 is the best number for this method and for our dataset. 
<br/>
	When a user types text into the engine to be spoken, the hash function performs constant lookup for these groups of characters for pronunciation, and concatenates segments of pronunciation to form each word that is to be spoken. We will also use a custom Aho-Corasick algorithm to aid this lookup, where the nodes include vowels, consonants, diphthongs, consonant clusters, and vowel trigraphs. The patterns detected by KMP are passed to the custom hash function which looks up the pronunciation of the detected patterns in O(n*k + m) where n is the total length of text, m is the total number of characters in all words, and k is the total number of input words.
	
| Amortized cost|                              | Space Complexity                                     |
| :----------   | :--------------------------- | :--------------------------------------------------- |
| O(1)          | Diphone concentenation 🏴󠁧󠁢󠁥󠁮󠁧󠁧󠁢󠁥    | O(N)                                                 |
| O(N*k+m)      | Aho-Corasick pattern lookup  | O(W)                                                 |
| O(N)          | Hashing:search 🔃           | O(N*k+m)



<br/>

Sample results

Here the test sentence is broken into words and punctuations. For each word, the word is breaked into a combination of diphones, we combine the diphones and use them as keys to search our dictionary to obtain the audio files, after that, we concatenate the audio to one, and play the generated audio. This is performed in cleo.py with the usage of the cmudict text dataset, which includes every possible English diphone in writing, all paired together to cover every possibility in text. The library ntlk is used in this file as well for the purpose of downloading this dataset cmudict. The audio class in the audio.py module is for the purpose of playback for the concatenated sound in our custom Python dictionary. It has built in functions from pyaudio to support converting from a numpy int16 type to a pyaudio int16 type. Pyaudio is a library which supports this playback directly with the built-in type pyaudio int16.
The implementation of our own custom Python dictionary using DJB2 and linear probing based on linked list results in a 5% faster running time compared to the built in Python dictionary, which is unexpected for us because the built in dictionary is built based on cpython, which is implemented in C code, it had a lots of advantages over implement this in Python, including using pointers and C is a lower level language, while Python is a interpreter, so naturally we are having a lots of disadvantages against the build in dictionary. We were thinking about implementing the dictionary in C code and binding it with Python in early stages of the project, but we realized it is very complicated and might cause some problems so we decided to implement the dictionary in Python. We believed that if the dictionary were implemented in C we will obtain an even better result.

This is the result of concatenated diphones, the sample wav file can be downloaded here.



Future work
Because we are only concatenating the diphones together, thus there are no tone nor emotions in the generated audio sample, in the future, we are going to trying to find a way to implement a method that can mimic the tone and emotions that a human have when reading text, in this way, the audio we generated are much smoother and closer to natural enunciation. This can be achieved with a technique known in many music producing softwares as crossfading, which lowers the amplitude of one signal to 0 while increasing the amplitude of the next signal up from 0, producing a nice blended natural sound. Using diphones instead of phones in this project seeks to utilize this characteristic of better blending sounds together because having an existing dataset of pairs of sounds is bound to sound more natural than concatenating individual sounds.


Setup/installation:

Windows Powershell:
```bash
get-executionpolicy # if Restricted, run the following:
set-executionpolicy remotesigned # run if Restricted in previous line
py -m venv .env  # start virtual environment for package downloads
.env/Scripts/Activate.ps1 # activates the virtual environment
py -m pip install -r requirements.txt
pipwin install pyaudio
py -m python cleo.py -s "text to be spoken"
```
UNIX based terminals Mac, Ubuntu, CentOS, etc.
```bash
python -m venv .env # start virtual environment for package downloads 
.env/bin/activate # activates the virtual environment for UNIX based terminals (Mac, Ubuntu, CentOS, etc.)
pip install -r requirements.txt
python cleo.py -s "text to be spoken"
```
