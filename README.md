# Lab 1: Infrastructure, Functions, and Logic

Welcome to your first lab! This week is focused on setting up your development environment, understanding Python functions, and applying logic to solve problems.

> [!IMPORTANT]
> **Submission Note:** The work for Days 3, 4, and 5 will be submitted together via GitHub on **Friday (1/16)**.

---

## 📅 Schedule & Tasks

### Day 3: Infrastructure Setup (Monday, 1/12)

**Goal:** Get your coding environment (GitHub Codespaces) ready.

1. **GitHub Account:** Create a [GitHub account](https://github.com) if you don't have one.
2. **Join Classroom:** Click the [INSERT_LINK] provided by your instructor.
3. **Launch Codespaces:** Inside your new repo, click **Code** (green button) → **Codespaces** → **Create codespace**.
4. **Coding Task:** Open `lab1_3.py` and create a function named `add(x, y)` that returns the sum of two numbers.
5. **Verify:** Run `python3 test_3.py` in the terminal.

### Day 4: Functions (Wednesday, 1/14)

**Goal:** Translate requirements into working Python functions. Open `lab1_4.py` and write the following:

| Function Name | Arguments | Description |
| --- | --- | --- |
| `calculate_average` | `num1, num2, num3` | Calculate the mathematical average of three different numbers. |
| `add_tax` | `bill_total` | Given a dollar amount, return the total after adding a **10%** sales tax. |
| `greet_user` | `name` | Accept a string and return a greeting that says "Hello" followed by that name. |

**Verify:** Run `python3 test_4.py` in the terminal.

### Day 5: Boolean Logic & Testing (Friday, 1/16)

**Goal:** Use conditional logic to solve more complex problems. Open `lab1_5.py` and write the following:

| Function Name | Arguments | Description |
| --- | --- | --- |
| `check_multiple` | `number` | Return `True` if the number is a multiple of **both** 3 and 5. Otherwise, return `False`. |
| `check_password` | `input_string` | Compare the input to a secret word of your choice. Return `"access granted"` if they match, or `"access denied"` if they don't. |
| `calculate_federal_tax` | `salary` | Use chained conditionals to return a tax amount based on these brackets: <br>

<br>• <= $11k: **10%** <br>

<br>• $11k - $44,725: **12%** <br>

<br>• $44,725 - $95,375: **22%** <br>

<br>• Over $95,375: **24%** |

**Verify:** Run `python3 test_5.py` in the terminal.

---

## 🐍 New to Python?

### What is a `.py` file?

A file ending in `.py` is a plain text file containing Python code. The computer reads this "script" from top to bottom. In this lab, your `.py` files contain **functions** (reusable blocks of code), while your `test_` files check if those functions work correctly.

### Running Code via the Command Line

The **Terminal** is the text interface at the bottom of your screen. To run your code or tests, you must tell the Python "interpreter" which file to read.

* **To run your script:** ```bash
python3 lab1_4.py
```

```


* **To run your tests (Recommended):** ```bash
python3 test_4.py
```



```



---

## 📥 Submission Instructions

Once Day 5 is complete, use the **Source Control** (branch icon) menu in Codespaces:

1. **Stage:** Click the **+** next to your changed files.
2. **Commit:** Type "Completed Lab 1" in the box and click **Commit**.
3. **Push:** Click **Sync Changes** to upload your work to GitHub.
4. **Verify:** Go to your GitHub URL and ensure your code appears there.
