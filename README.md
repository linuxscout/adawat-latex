[![GitHub issues](https://img.shields.io/github/issues/linuxscout/adawat-latex)](https://github.com/linuxscout/adawat-latex/issues)
[![GitHub forks](https://img.shields.io/github/forks/linuxscout/adawat-latex)](https://github.com/linuxscout/adawat-latex/network)
[![GitHub stars](https://img.shields.io/github/stars/linuxscout/adawat-latex)](https://github.com/linuxscout/adawat-latex/stargazers)
[![GitHub license](https://img.shields.io/github/license/linuxscout/adawat-latex)](https://github.com/linuxscout/adawat-latex/blob/master/LICENSE)

# Adawat-latex
Text tools to handle conversion into Latex with arabic support
برنامج فيه أدوات لتسهيل نقل النصوص إلى نظام التنضيد لاتخ
 
## مزايا
*  مزايا لغوية
	* تحويل النص العربي من الرومنة إلى اليونيكود
	* كشف مقاطع اللغة العربية وتحديدها
	* قلب نص 
	* تفريق نص إلى كلمات
* الجداول والقوائم
	* تحويل ملف نصي إلى جدول بصيغة لاتخ، HTML و Markdown
	* تحويل الأسطر إلى قائمة نقاط مرقمة أو غير مرقمة
	* تحويل اسطر إلى جدولات ذات محاذاة في لاتخ
	* إستعادة شكل جدول وتقسيم الاسطر إلى أعمدة
	* تحويل أسطر إلى جداول بيثون أو json
* عمليات مركبة
	يمكن تركيب أكثر من عملية:
	* تقسيم الاسطر إلى أعمدة جدول، ثم تحويلها إلى جدول
	* كشف اللغة وتحويل الاسطر إلى نقاط
	* كشف اللغة، وتحويل الأسطر إلى جدول
* Compiste command:
	You can recopy the out put to do more command on the smae text, for example:
	* reshape and convert into table
	* detect laguage and itemize
	* detect laguage and tabulize

## Features
*  Language features
   * Transliterate (TIM buckwaleter, Unicode, Sampa)
   * Detect Arabic language segments
   * Inverse text
   * Tokenize
* tables and Lists  for Latex
	* Convert a CSV to tabular
	* Converts lines into itemize or enumerate environment
	* Converts CSV lines into tabbing environment
	* Detect and delimite arabic language for Arabtex environment
	* Reshape a lines into CSV tabs
* Compiste command:
	You can recopy the out put to do more command on the smae text, for example:
	* reshape and convert into table
	* detect laguage and itemize
	* detect laguage and tabulize

### Usage  استعمال
 * Command line  سطر الأوامر
 ```
 python adawat-latex.py  -c tabulize -f inputfile.txt
 ```

 * GUI  الواجهة الرسومية
 ```
 python adawat-latex-gui.py
 ```

 ![Gui](./docs/adawat-latex.png)

 ## How To use   كيفية الاستعمال
 
 
### Tables and lists  الجداول والقوائم
* Itemize and Enumerate 
* CSV to latex table
* CSV to  latex tabbing
* Reshape a list into a table
* CSV to JSON or Python table
* Composite commands
 #### Itemize and Enumerate  قائمة نقاط مرقمة وغير مرقمة
 if you have a list of point and you want to convert it to a list, for example:

 use "itemize" with parameters option [itemize, enumerate]
 
 إذا لديك  أسطر، وتريد تحويلها إلى قائمة مرقمة أو غير مرقمة استعمل الأمر "itemize" 
 مع خيارين للقائمة المرقمة وغير المرقمة في لاتخ (itemize, enumerate)
 


 ```text
One entry in the list
Another entry in the list
Another entry in the list
Another entry in the list
 ```
  Output will be 
  ```tex
  \begin{itemize}
\item One entry in the list
\item Another entry in the list
\item Another entry in the list
\item Another entry in the list 
\end{itemize}
  ```
  ```tex
  \begin{enumerate}
\item One entry in the list
\item Another entry in the list
\item Another entry in the list
\item Another entry in the list 
\end{enumerate}

  ```

#### CSV to table
يمكن تحويل الأطسر ذات الأعمدة المفصولة بجدولات إلى جدول
باستعمال الأمر "tabulize" 
If you have a table on Excel or text with tab as délimeter, you can choose "tabulize" to convert it into:

الصيغ الممكنة:
	* Latex
	* HTML
	* Markdown

* Input as csv or text delimited by tab  النص المدخل حيث الاعمدة مفصولة بجدولة
```csv
head1	Head2	head3
cell	cell2	cell3
cell	cell2	cell3
cell	cell2	cell3
cell	cell2	cell3
```

* Output as Tex المخرج بصيغة لاتخ
```tex
\begin{table}
 \begin{tabular}{|c|c|c|}
\hline head1 & Head2 & head3\\
\hline cell & cell2 & cell3\\
\hline cell & cell2 & cell3\\
\hline cell & cell2 & cell3\\
\hline cell & cell2 & cell3\\
\hline

    \end{tabular}

    \caption{mytab:table}

    \label{mytab:table}

     \end{table}                 
```
 * Output as HTML الناتج بصيغة وب
```html
<table>
<tr><td>head1 </td><td>Head2 </td><td>head3</td></tr>
<tr><td>cell </td><td>cell2 </td><td>cell3</td></tr>
<tr><td>cell </td><td>cell2 </td><td>cell3</td></tr>
<tr><td>cell </td><td>cell2 </td><td>cell3</td></tr>
<tr><td>cell </td><td>cell2 </td><td>cell3</td></tr>
</table>
```

 * Output as Markdown الناتج بصيغة ماركداون
```md
head1 | Head2 | head3
cell | cell2 | cell3
cell | cell2 | cell3
cell | cell2 | cell3
cell | cell2 | cell3
```



#### Make a latex tabbing   تحويل الأسطر إلى جدولة لاتخ

الجدولة في لاتخ هي ضيغة تظهر في شكل اعمدة محاذاة غلى بعضها البعض،
لذا يمكنك استعمال الأمر "tabbing" لتحويل أسطر بها أعمدة إلى جدولة
مع اختيار علامة الفصل بين الحقول

If you have a table on Excel or text with tab as délimeter, you can choose "tabbing" to convert it into :
	* Latex  tabbing 

You can choose different separator (tab, space, etc..) in the input text
```csv
head1	Head2	head3
cell	cell2	cell3
cell	cell2	cell3
cell	cell2	cell3
cell	cell2	cell3
```

* Output as Tex
```tex
 \begin{tabbing}
\hspace{4cm}\=\hspace{4cm}\=\hspace{4cm}\=\kill
head1 \> Head2 \> head3\\
cell \> cell2 \> cell3\\
cell \> cell2 \> cell3\\
cell \> cell2 \> cell3\\
cell \> cell2 \> cell3\\
\end{tabbing}                 
```

##### Reshape a list into a table  إعادة تشكيل أسطر في جدول
أحيانا بعض البرامج تنسخ الجداول في شكل أسطر تضيع معها معالم الأعمدة، لذا فخاصة "reshape"
تعيد تقسيم الأسطر إلى أعمدة بعدد معين يمكن ضبطه

Some programs copy tables as list instead of table or matrix, which generate problems.
The "Reshape" command helps to handle this issue

* Original table  الجدول الأصلي
```text
1	one
2	two
3	three
```
 * The input as it has copied format of the table,  الجدول بعد نسخه يصبح مجرد أسطر متتابعة
```python
1
one
2
two
3
three
```
* Out pur with "Reshape" command with "2" columns as option  استعمال إعادة التسكيل مع الخيار "2"
```
1	one
2	two
3	three
```


#### CSV to Python list  أسطر إلى جدول بيثون

تحويل ملف نصي ذي أعمدة مفصولة إلى  جدول بيثون،
حيث العمود الاول للمفتاح والعمود الثاني للقيمة،
مع وضع اسم الجدول في السطر الأول

If you have a list of key values in CSV file, you can convert it to python list, or Json, by using "Python List" command.

The first line is the name of table "Table", and colomns are separated by tabulation.

* Input as CSV
```text
mytable
1	one
2	two
3	three
```
 * Output as python list
```python
mytable={}
mytable['1']={}
mytable['one']={}
mytable[u'one'][u'1']='one'
mytable[u'one'][u'2']='two'
mytable[u'one'][u'3']='three'
```




### Language features وظائف لغوية
* Transliterate arabic text between (utf, tim bukwalter, Sampa)
* Detect Arabic segment and tag it
* Tokenize : convert text into list of words
* Inverse text
#### Transliterate  تحويل النص بين الرومنة والحروف العربيو
 
 يمكن نقحرة النص العربي أي كتابته بالأحرف اللاتينية في نظام تيم بولكولتر أو sampa
 والتحويل بين هذه الأنظمة
 
 The transliterate convere arabic text like this :
* from Unicode(UTF8) to Tim Bulkwalters transcription,
* from Tim Bulkwalters transcription  to Unicode(UTF8)
* from Tim Bulkwalters transcription  to SAMPA transcription

 * Input as text
```text
السلام عليكم ورحمة الله وبركاته
```
 * Output as SAMPA
```text
a:lsla:m ?'ljkm wrxmh a:llh wbrka:th
```

#### Detect Arabic segment and tag it كشف اللغة وتحديدها

في ملفات لاتخ، نحتاج إلى وضع علامات على بداية المقاطع بالعربية،
هذه الوظيفة تفعل ذلك
بوضع علامات
مثل: (\RL, \begin{arab} environment}


If you have a mix text and you want to put it within a Tex document by using Polyglossia, ArabTex or ArabXeTex packages, you can use "language command" with options (\RL, \begin{arab} environment}


* Input as text
```text
The man said السلام عليكم and he goes.
```
 * Output as Tex with "\RL" option
```tex
The man said  \RL{السلام عليكم}  and he goes.
```
 * Output as Tex with "arab environment" option
```tex
The man said  
\begin{arab}[utf] السلام عليكم \end{arab} 
 and he goes.
```

#### Tokenize تفريق النص إلى كلمات

IIf you want to split text into words or tokens, just use tokenize

* Input as text
```text
The man said السلام عليكم and he goes.
```
 * Output as list of word
```
The
man
said
السلام
عليكم
and
he
goes
.
```




#### Inverse text قلب النص
Some programs generate an arabic inversed text, which needs to be inversed.
It can be used for english, or just to inverse a text.

بعض البرامج تعكس الكلمات العربية، لذا تساعدك هذه الوظيفة في استرجاع النص الاصلي

* Input as text
```text
.seog eh dna مكيلع مالسلا dias nam ehT
```
 *  Output as inversed  text
```
The man said السلام عليكم and he goes.
```





