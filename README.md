# Alphabetical sorting of backslash dictionary files 

Mac version, 1 Feb 2021


## Files required

- A backslash `.txt` file needing to be alphabetised. See `input.txt` for an example.
- A text file containing alphabet characters comma-separated, eg
  `a, b, c, d, n, ny`. See `alphabet.txt` for an example.
- The python script `sort.py`


## System requirements

1.1 Requires Python version 3 (not version 2), and the NLTK Python package.

1.2 To check the version of Python you have, open a Terminal window and type the following commands and see what version is displayed.
```bash
python --version

python3 --version
```

1.3 If Python 3 is installed this should display something like Python 3.x.x.  If you don’t have Python 3, either find someone who does or follow installation instructions online.

1.4 To install NLTK, type the following command.

```bash
pip3 install nltk
```



## Using the script

2.1. Put the backslash dictionary file, alphabet file and script file in the same working directory, e.g. in a folder called `Alpha` on the Desktop.

2.2. Open Terminal (i.e. go to Applications/Utilities folder and double click on Terminal icon).

2.3. In the Terminal window at the prompt, type the following to get the Terminal into the working directory where your files are, and press Return.

```bash
cd ~/Desktop/Alpha
```

2.4. Type or copy the following command into the terminal, replacing the file names with your real file names if they are different, and press Return. The name following the `-i` is the name of your backslash dictionary file, the name following the `-o` is what the sorted dictionary will be saved as.

```bash
python3 sort.py -a alphabet.txt -i dictionary.txt -o dictionary-sorted.txt
```


## Options

3.1 If your alphabet file is called alphabet.txt you don't need to include this in the command. You can just do this:
```bash
python3 sort.py -i dictionary.txt -o dictionary-sorted.txt
```

3.2 The script will ignore leading hyphens in headwords by default. You can manually specify the order position of hyphenated entries instead, by including a hyphen in your alphabet file, and making the `ignore dashes (-d)` setting False, eg:
```bash
python3 sort.py -i dictionary.txt -o dictionary-sorted.txt -d False
```
