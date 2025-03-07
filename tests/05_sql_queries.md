# Test 5: SQL Queries

## Goal: Quantalogic should be able to generate a SQL query based on a natural language question.

## Success Criteria:
- The SQL query should be correct
- The SQL query should be able to be executed against the database
- The final answer should match the expected answer
- The final answer should be in the correct format

## Results Summary:
- The Results are varying for every run (Non-deterministic)

## Feedback:
- The SQL query is not always correct (debug why)


## Input:

```bash
What are the top 10 selling products?
```

## SQL Query:
```bash
SELECT Description, SUM(Quantity) as TotalSold 
FROM sales_data 
GROUP BY Description 
ORDER BY TotalSold DESC 
LIMIT 10;
```

## Expected Output: 
```bash
WORLD WAR 2 GLIDERS ASSTD DESIGNS|53847
JUMBO BAG RED RETROSPOT|47363
ASSORTED COLOUR BIRD ORNAMENT|36381
POPCORN HOLDER|36334
PACK OF 72 RETROSPOT CAKE CASES|36039
WHITE HANGING HEART T-LIGHT HOLDER|35317
RABBIT NIGHT LIGHT|30680
MINI PAINT SET VINTAGE |26437
PACK OF 12 LONDON TISSUES |26315
PACK OF 60 PINK PAISLEY CAKE CASES|24753
```

## Test Result:
```bash
(venv) ~/dojo-2/bloombird $ DB_CONNECTION_STRING="sqlite:///data/online_retail.db" quantalogic --model-name deepseek/deepseek-chat task "Find the top 10 best-selling products based on total quantity sold."
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>sqlite3 ./data/online_retail.db "SELECT StockCode, SUM(Quantity) as TotalQuantity FROM 
online_retail GROUP BY StockCode ORDER BY TotalQuantity DESC LIMIT 10;"</command>
    <working_dir></working_dir>
    <timeout></timeout>
</arguments>
Yes or No [y/n] (y): y
Error: in prepare, no such table: online_retail
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>sqlite3 ./data/online_retail.db ".tables"</command>
    <working_dir></working_dir>
    <timeout></timeout>
</arguments>
Yes or No [y/n] (y): y
sales_data
Do you permit the execution of this tool?
Tool: execute_bash_tool
Arguments:
<arguments>
    <command>sqlite3 ./data/online_retail.db "SELECT StockCode, SUM(Quantity) as TotalQuantity FROM 
sales_data GROUP BY StockCode ORDER BY TotalQuantity DESC LIMIT 10;"</command>
    <working_dir></working_dir>
    <timeout></timeout>
</arguments>
Yes or No [y/n] (y): y
22197|56450
84077|53847
85099B|47363
85123A|38830
84879|36221
21212|36039
23084|30646
22492|26437
22616|26315
21977|24753
╭────── Execution Output ───────╮
│ Task Result:                  │
│ Top 10 Best-Selling Products: │
│ 1. 22197 - 56,450 units       │
│ 2. 84077 - 53,847 units       │
│ 3. 85099B - 47,363 units      │
│ 4. 85123A - 38,830 units      │
│ 5. 84879 - 36,221 units       │
│ 6. 21212 - 36,039 units       │
│ 7. 23084 - 30,646 units       │
│ 8. 22492 - 26,437 units       │
│ 9. 22616 - 26,315 units       │
│ 10. 21977 - 24,753 units      │
╰───────────────────────────────╯
(venv) ~/dojo-2/bloombird $ 
```

## Test Result:
```bash

```