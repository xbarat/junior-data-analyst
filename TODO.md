# TODO

---

### **Note:** 
- Done: Exploration
- Next: Data Cleaning
- Time: 8 hours/48 hours

---

## **Phase 1: Testing Capability - Data Analysis**

*Basic Exploration:*
- [X] Load dataset & preview structure
- [X] Detect missing values & duplicates
- [ ] Results captured in tests/01-basic-exploration.md

*Data Cleaning:*
- [ ] Implement cleaning: fill nulls, drop bad data
- [ ] Validate: Ensure cleaned dataset structure
- [ ] Results captured in tests/02-missing-values.md

*Query Generation:*
- [ ] AI converts NL → SQL (5 test queries)
- [ ] Compare AI queries vs. manually written SQL
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


Feature Requests:
- [ ] Test multi-step transformations (currently find missing values & fill them works)
- [ ] Allow user-defined transformations in prompts (show missing value strategy, replace with mean, etc.)
- [ ] Test data pipelines across multiple file formats (CSV, Excel, JSON, etc.
- [ ] Error handling and Safe execution (rollback on error, etc.)