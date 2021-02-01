# Alphabetical sorting of backslash dictionary files 

Mac version, 1 Feb 2021


## Files required

1.1 A backslash `.txt` file needing to be alphabetised.

1.2 The python script `sort.py`



## System requirements

2.1 You also need to have Python version 3 (not version 2) and the NLTK Python package.

2.2 To check the version of Python you have, open a Terminal window and type the following commands and see what version is displayed.
```bash
python --version

python3 --version
```

2.3 If Python 3 is installed this should display something like Python 3.x.x.  If you don’t have Python 3, either find someone who does or follow installation instructions online.

2.4 To install pandas, type the following command.

```bash
pip3 install nltk
```



## Using the script

3.1. Put the backslash dictionary file and script file in the same working directory, e.g. in a folder called `Alpha` on the Desktop.

3.2. Open `Terminal` (i.e. go to Applications/Utilities folder and double click on Terminal icon).

3.3. In the Terminal window at the prompt, type the following to get the terminal into the working directory where your files are, and press Return.

```bash
cd ~/Desktop/Alpha
```

3.4. Type or copy the following command into the terminal, and press Return.

```bash
python3 sort.py -i name-of-dictionary-file.txt -o name-of-new-file.txt
```

3.5 The name following -i is the filename of the input backslash file, e.g. you might type the following:

```bash
python3 sort.py -i Ngarinyman_dict.txt -o Ngarinyman_dict_alpha.txt
```

3.6 Then `Ngarinyman_dict_alpha.txt` will appear in your Alpha folder on the Desktop as the alphabetised version of the backslash file.
