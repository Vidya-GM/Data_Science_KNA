## Numpy:
### Part 1: NumPy Basics & Array Fundamentals
- What a NumPy array is

- How it’s different from Python lists

- How to inspect array properties (shape, dtype, dimensions)

1. What is NumPy (Very Short & Practical)

    NumPy provides:

        Fast numerical arrays

        Vectorized operations (no loops)

        Memory efficiency

    Python lists:

        Can store mixed types

        Slower for math

    NumPy arrays:

        Same data type

        Extremely fast for numbers

2. Why NumPy Is Better Than Lists (Quick Demo)
    Python list
        lst = [1, 2, 3]
        print(lst * 2)   # duplicates list

    Output: [1, 2, 3, 1, 2, 3]

    NumPy array
        arr = np.array([1, 2, 3])
        print(arr * 2)   # math operation
    Output: [2 4 6]

#### Key Takeaways (Very Important)

✔ NumPy arrays store homogeneous data

✔ Shape & dimensions matter a lot later

✔ NumPy enables math without loops

================================================

### Part 2: NumPy Array Creation Methods

1. Know multiple ways to create arrays

2. Understand when to use each method

3. Be able to simulate real-world data

1️⃣ np.zeros() and np.ones()
Use case (Real world):

    Initializing data buffers

    Placeholder arrays

    Image / matrix initialization

2️⃣ np.arange() (Most Used)
Use case:

    Index values

    Time steps

    Iteration replacement

3️⃣ np.linspace(start, stop, num=x) (Very Important)
Difference vs arange

arange : Step-based, Floating errors possible            
linspace: Count-based, Precise endpoints

4️⃣ Random Data (Real-World Simulation)

Uniform random values

    rand_arr = np.random.rand(5)
    print(rand_arr)

Integers

    rand_int = np.random.randint(10, 50, size=6)
    print(rand_int)

Normal distribution (VERY IMPORTANT)

    normal_data = np.random.normal(loc=50, scale=10, size=100)
    print(normal_data[:5])

#### Used heavily in:

    - Finance
    - ML
    - Simulations

5️⃣ Reproducibility (CRITICAL)

    Always set seed in real projects:
    np.random.seed(42)
    This ensures same random results every run.

#### Key Takeaways:
    ✔ Use zeros/ones for initialization
    ✔ Use arange for index-like sequences
    ✔ Use linspace for precise ranges
    ✔ Random data is essential for simulations    

=============================================

### Part 3: Indexing & Slicing (1D + 2D)

    - Access and modify elements efficiently
    - Slice arrays like real datasets
    - Understand views vs copies (VERY IMPORTANT)

1️⃣ 1D Array Indexing

    arr = np.array([10, 20, 30, 40, 50])
    arr[0]    # first element
    arr[-1]   # last element

    - Modify elements
    arr[2] = 99
    print(arr)

2️⃣ 1D Array Slicing

    arr[start : stop : step]
    print(arr[1:4])     # elements at index 1,2,3
    print(arr[:3])      # from start
    print(arr[::2])     # every 2nd element

    *Stop index is excluded

3️⃣ 2D Array Indexing (Tables)

    data = np.array([
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ])

    - data[1]        # entire second row
    - data[:, 1]     # all rows, column index 1 (2nd column)
    - data[2, 0]     # row 2, column 0 (A specific element)

4️⃣ 2D Array Slicing (Very Important)

    Extract sub-matrix:
        sub = data[0:2, 1:3] 
        --> 0:2-for rows, exclude 2, so rows included 0, 1
        --> 1:3-for columns, exclude 3, so columns included 1, 2
        print(sub)

        output: [
            [200, 300]
            [500, 600]
        ]

    * Rows = records, Columns = features

5️⃣ Fancy Indexing

    arr = np.array([10, 20, 30, 40, 50])
    print(arr[[0, 2, 4]])
    output: [10, 30, 50]

6️⃣ Boolean Indexing (🔥 VERY IMPORTANT 🔥)
    
    This is used everywhere in real projects.
    
    arr = np.array([25, 30, 35, 40, 45])

    mask = arr > 35
    print(mask)
    print(arr[mask])

    output:
    [False False False  True  True] --> mask is an array of True, False
    [40 45] --> arr[mask], includes values at indices whose value is 'True'

    In-short: arr[arr > 35]

7️⃣ Views vs Copies (CRITICAL CONCEPT): 
    
    Slice = View (shared memory) --> Gives view of sliced memory

    a = np.array([1, 2, 3, 4, 5, 6, 7])
    b = a[1:4]
    b[0] = 99
    print(a)
    output: a = [1, 99, 2, 3, 4, 5, 6, 7]

    * Changing 'a' changes 'b'

    To avoide this 'Force a copy':
    b = a[1:4].copy()
    Now changes won’t affect original.

    * Boolean Indexing Returns a Copy, Not a View

### Part 4: Boolean Masking (Deep Dive)

    Filter data without loops
    Update data conditionally
    Combine multiple conditions
    Think in data rules, not if-statemens

1️⃣ What Is Boolean Masking?

    A boolean mask is an array of True / False values used to:
        - Select data
        - Modify data
    
    arr = np.array([10, 20, 30, 40, 50])
    mask = arr > 25

    print(mask)         [False False  True  True  True]
    print(arr[mask])    [30 40 50]

2️⃣ Real-World Example: Salary Filtering

    salaries = np.array([25000, 40000, 55000, 70000])
    high_salary = salaries > 50000
    print(salaries[high_salary])

3️⃣ Modifying Values Using Mask

    Give bonus to low salaries
    salaries[salaries < 50000] *= 1.10
    print(salaries)

**No loops. Fully vectorized.**

4️⃣ Multiple Conditions (&, |, ~)

    **Important rule:**
    Use &, |, ~
    NOT and, or, not

    Example:

    - AND condition
    ages = np.array([18, 25, 30, 40, 55])
    working_age = (ages >= 18) & (ages <= 60)
    print(ages[working_age])

    - OR Condition
    young_or_old = (ages < 20) | (ages > 50)
    print(ages[young_or_old])

    - NOT Condition
    not_working = ~(ages >= 18)
    print(ages[not_working])

5️⃣ Boolean Masking on 2D Arrays
    data = np.array([
        [22, 30000],
        [28, 45000],
        [35, 60000],
        [40, 80000]
    ])

    Filter rows where salary > 50000
        high_income = data[data[:, 1] > 50000]
        print(high_income)

    Increase salary for age > 30
        data[data[:, 0] > 30, 1] *= 1.05
        print(data)

6️⃣ np.where() (Very Useful)

    Conditional selection
        arr = np.array([10, 20, 30, 40])
        result = np.where(arr > 25, arr * 2, arr)
        print(result)

    Meaning:
        IF arr > 25 → multiply by 2  
        ELSE → keep original

7️⃣ Why Boolean Masking Beats Loops

*Loop approach:*

    for i in range(len(arr)):
        if arr[i] > 25:
            arr[i] *= 2


✅ NumPy approach:

    arr[arr > 25] *= 2
    ✔ Faster
    ✔ Cleaner
    ✔ Less error-prone



