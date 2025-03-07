# TODO

---

### **Note:** 
- Done: Exploration, Data Cleaning
- Next: Query Generation, Insights & Charts
- Time: 8 hours/48 hours

---

## **Phase 1: Testing Capability - Data Analysis**

*Basic Exploration:*
- [X] Load dataset & preview structure
- [X] Detect missing values & duplicates
- [ ] Results captured in tests/01-basic-exploration.md

*Data Cleaning:* (SUCCESS)
- [X] Implement cleaning: fill nulls, drop bad data
- [X] Validate: Ensure cleaned dataset structure
- [X] Results captured in tests/02-missing-values.md

- [X] Filtering & Aggregations (Find top selling products)
- [X] Time-based Analysis (Identify peak transaction hours from InvoiceDate)
- [X] Anamoly Detection (Find orders with Quantity < 0)
- [X] Data Formatting & Cleanup (Ensure correct data types for all columns)

*Text to SQL Generation:* (PARTIAL SUCCESS)
- [X] AI converts NL → SQL (5 test queries)
- [X] Compare AI queries vs. manually written SQL
- [X] Results captured in tests/05_sql_queries.md
- [ ] Log & fix incorrect AI-generated queries
- [ ] Ensure AI queries return valid results

*Insights & Charts:*
- [ ] Generate summary stats (mean, median, mode)
- [ ] Create bar, line, & scatter plots
- [ ] Ensure visuals match business expectations
- [ ] Validate AI-driven insights for anomalies

*CLI/Web UI:*
- [ ] Build CLI/Web UI for user input
- [ ] Run through 10 real user test cases
- [ ] Log feedback & refine based on errors
- [ ] Deploy & collect final validation metrics

⏳ Timebox: Each phase = 48 hours.
🎯 Goal: Get AI to automate structured data tasks without breaking stuff.



Backlog:
- [ ] Migrate python executions from execute_bash_tool to python_tool
- [ ] Improve UX for in-memory data modifications before file changes
- [ ] Add observability for each tool execution (results, outputs, errors, logs)
- [ ] Add data processing logging and debugging mode
- [ ] How does MCP (Model Context Protocol) work?
- [ ] Research Technical Tradeoffs for building a MCP-compliant agent


Feature Requests:
- [ ] Test multi-step transformations (currently find missing values & fill them works)
- [ ] Allow user-defined transformations in prompts (show missing value strategy, replace with mean, etc.)
- [ ] Test data pipelines across multiple file formats (CSV, Excel, JSON, etc.
- [ ] Error handling and Safe execution (rollback on error, etc.)