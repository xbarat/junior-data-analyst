### Test Case: Change Missing Values

#### Description
This test case verifies that the missing values are handled as expected.

#### Preconditions
- The dataset is loaded.
- The missing values are identified.

### Test Case 1: Using PythonTool

#### Steps
1. Use the PythonTool to change the missing values.

#### Expected Results
- The missing values should be changed.
- The dataset should be saved.

#### Expected User Experience
- The user should be able to see the missing values are changed (with 100% confidence)
- The user should have to control to save the changes with yes/no
- *nice to have* The user should be able to re-run with a different strategy (e.g. fill with mean)

#### Actual Results
- the missing values are changed 
- the dataset is not saved (saved in-memory only)

### Test Case 2: Using CLI

#### Steps
1. Use the CLI to change the missing values.

#### Expected Results
- The missing values should be detected.
- The missing values should be changed.
- The dataset should be saved.

#### Expected User Experience
- The user should be able to see the missing values are changed (with 100% confidence)
- The user should have to control to save the changes with yes/no
- *nice to have* The user should be able to re-run with a different strategy (e.g. fill with mean)
- *nice to have* low latency

#### Actual Results
- the missing values are detected using execute_bash_tool
- the missing values are changed using execute_bash_tool
- the dataset is saved to a new file
- slow execution than PythonTool


### terminal logs

#### PythonTool

```bash
(venv) ~/dojo-2/bloombird $ python src/02_missing_values.py
Script Output: Missing Values:
 InvoiceNo           0
StockCode           0
Description      1454
Quantity            0
InvoiceDate         0
UnitPrice           0
CustomerID     135080
Country             0
dtype: int64
Missing Values After Fix:
 InvoiceNo      0
StockCode      0
Description    0
Quantity       0
InvoiceDate    0
UnitPrice      0
CustomerID     0
Country        0
dtype: int64
(venv) ~/dojo-2/bloombird $ python src/02_missing_values.py
Script Output: Missing Values:
 InvoiceNo           0
StockCode           0
Description      1454
Quantity            0
InvoiceDate         0
UnitPrice           0
CustomerID     135080
Country             0
dtype: int64
Missing Values After Fix:
 InvoiceNo      0
StockCode      0
Description    0
Quantity       0
InvoiceDate    0
UnitPrice      0
CustomerID     0
Country        0
dtype: int64
(venv) ~/dojo-2/bloombird $ mkdir tests
(venv) ~/dojo-2/bloombird $ touch tests/02_missing_values.md
```

#### CLI

```bash
(venv) ~/dojo-2/bloombird $ quantalogic --mode full --log debug task "In data/online+retail.xlsx, List missing values in CustomerID and fix them to -1."
/Users/btsznh/dojo-2/bloombird/venv/lib/python3.13/site-packages/fuzzywuzzy/fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning
  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>python3 -c "import pandas as pd; df = pd.read_excel('data/online+retail.xlsx'); 
print(df[df['CustomerID'].isna()])"</command>
    <working_dir>/Users/btsznh/dojo-2/bloombird</working_dir>
    <timeout>60</timeout>
</arguments>
Yes or No [y/n] (y): y
       InvoiceNo StockCode  ... CustomerID         Country
622       536414     22139  ...        NaN  United Kingdom
1443      536544     21773  ...        NaN  United Kingdom
1444      536544     21774  ...        NaN  United Kingdom
1445      536544     21786  ...        NaN  United Kingdom
1446      536544     21787  ...        NaN  United Kingdom
...          ...       ...  ...        ...             ...
541536    581498    85099B  ...        NaN  United Kingdom
541537    581498    85099C  ...        NaN  United Kingdom
541538    581498     85150  ...        NaN  United Kingdom
541539    581498     85174  ...        NaN  United Kingdom
541540    581498       DOT  ...        NaN  United Kingdom

[135080 rows x 8 columns]
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>python3 -c "import pandas as pd; df = pd.read_excel('data/online+retail.xlsx'); df['CustomerID'].fillna(-1, 
inplace=True); df.to_excel('data/online+retail_fixed.xlsx', index=False)"</command>
    <working_dir>/Users/btsznh/dojo-2/bloombird</working_dir>
    <timeout>60</timeout>
</arguments>
Yes or No [y/n] (y): y
<string>:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  import pandas as pd; df = pd.read_excel('data/online+retail.xlsx'); df['CustomerID'].fillna(-1, inplace=True); df.to_excel('data/online+retail_fixed.xlsx', index=False)
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>python3 -c "import pandas as pd; df = pd.read_excel('data/online+retail_fixed.xlsx'); 
print(df[df['CustomerID'] == -1].head())"</command>
    <working_dir>/Users/btsznh/dojo-2/bloombird</working_dir>
    <timeout>60</timeout>
</arguments>
Yes or No [y/n] (y): y
     InvoiceNo StockCode  ... CustomerID         Country
622     536414     22139  ...         -1  United Kingdom
1443    536544     21773  ...         -1  United Kingdom
1444    536544     21774  ...         -1  United Kingdom
1445    536544     21786  ...         -1  United Kingdom
1446    536544     21787  ...         -1  United Kingdom

[5 rows x 8 columns]
╭──────────────────────────────────── Execution Output ────────────────────────────────────╮
│ Task Result:                                                                             │
│ Missing CustomerID values successfully replaced with -1 in data/online+retail_fixed.xlsx │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
(venv) ~/dojo-2/bloombird $ 
```

#### Top Selling Products
```bash
(venv) ~/dojo-2/bloombird $ python src/03_filter_data.py
Script Output: Top-Selling Products:
 Description
WORLD WAR 2 GLIDERS ASSTD DESIGNS     53847
JUMBO BAG RED RETROSPOT               47363
ASSORTED COLOUR BIRD ORNAMENT         36381
POPCORN HOLDER                        36334
PACK OF 72 RETROSPOT CAKE CASES       36039
WHITE HANGING HEART T-LIGHT HOLDER    35317
RABBIT NIGHT LIGHT                    30680
MINI PAINT SET VINTAGE                26437
PACK OF 12 LONDON TISSUES             26315
PACK OF 60 PINK PAISLEY CAKE CASES    24753
```

### Questions:

#### Technical
- How large of a dataset can be processed? (Given 500,000 rows has been processed in 10 seconds)
- How accurate is the missing value detection?
- What are the performance trade-offs between PythonTool and CLI?
- What is the latency of the CLI and PythonTool?

#### UX
- How to ensure user confidence in the execution results?
- How do data analysts currently handle missing values?
- What tools do they use, and familiar with?
- Do they even want to change the missing values?

#### Product
- How to balance between automation and user control?
- How to ensure the user experience is seamless and easy to use?
- How to ensure the user is always in control?


