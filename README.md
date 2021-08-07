# Adawat-latex
Text tools to handle conversion into Latex with arabic support


## Features
### Arabic Language
* Transliterate (TIM buckwaleter, Unicode, Sampa)
* Detect language segments
* Inverse text
* Tokenize
### Latex
* Convert a CSV to tabular
* Converts lines into itemize or enumerate environment
* Converts CSV lines into tabbing environment
* Detect and delimite arabic language for Arabtex environment
* Reshape a lines into CSV tabs


### Usage 
 * Command line
 ```
 python adawat-latex.py  -c tabulize -f inputfile.txt
 ```
 
 * GUI
 ```
 python adawat-latex-gui.py
 ```
 
 ![Gui](docs/latex-adawat.png)
