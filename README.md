# 🛒 E-Commerce Website Testing - Test Cases

This repository contains **manual test cases** for an E-Commerce website (`demowebshop.tricentis.com`).  
The test cases cover **Registration, Login, Product Search and Cart** functionalities.

---

## 📂 Files Included

- **Ecommerce_Test_Cases_Updated.xlsx** → Detailed test cases with Test Case IDs, Preconditions, Steps, Inputs, and Expected Results.

---

## ✅ Modules Covered

1. **Registration**

   - Verify user can register with valid details
   - Verify registration with duplicate email (negative test)

2. **Login**

   - Verify login with valid credentials
   - Verify login with invalid credentials (negative test)

3. **Product Search**

   - Verify search with valid product name
   - Verify search with invalid product name

4. **Cart**
   - Verify adding products to cart
   - Verify viewing cart page
   - Verify removing product from cart

---

## 📊 Test Case Format

Each test case is documented with:

- **Test Case ID** → Unique identifier (e.g., TC001, TC002)
- **Test Scenario** → High-level description
- **Steps** → Sequential actions to perform
- **Actions** → What action have to be perform
- **Input Data** → Test data used
- **Expected Result** → System behavior to validate

---

## ⚙️ Tools Used

- **Excel / Google Sheets** → Manual test case documentation & execution tracking
- **Selenium (Python)** → Automation scripts for login, registration, cart, and checkout workflows

---

## 🚀 Execution Strategy

1. Execute **manual test cases** first to validate business workflows.
2. Automate **critical scenarios** using Selenium for regression testing.
3. Update **Actual Result** and **Status (Pass/Fail)** in the Excel sheet during execution.

---

## 📝 Author

Prepared by **Mratyunjay Saxena**  
Role: _Python, Web Developer and Test Engineer_
