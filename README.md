# Python Learning Journey 🚀

A structured repository documenting daily Python concepts, code implementations, Data Structures & Algorithms (DSA), and hands-on mini-projects.

---

## 📁 Repository Structure

```text
python-learning-journey/
│
├── day1/
│   ├── calculator.py          # Basic arithmetic CLI calculator
│   ├── hello.py               # Intro syntax & output formatting
│   ├── marks_analyzer.py      # Grade calculation & conditional logic
│   └── welcome.py             # User input & greeting scripts
│
├── day2/
│   ├── abc.py                 # Persistent student record manager with file storage
│   ├── arr.py                 # Manual list iterations, min, max & average
│   ├── calcfunc.py            # Modular function-based calculator with error handling
│   ├── marks.py               # Conditional pass/fail grading logic
│   ├── name.py                # String manipulation and function definitions
│   ├── sq.py                  # Math functions & square calculations
│   ├── student_marks.py       # In-memory dictionary-based student record processor
│   └── student_records.txt    # Text-based flat-file storage
│
├── day3/
│   ├── case.py                # String case methods & character length logic
│   ├── file.py                # File read/write operations via context managers
│   ├── notes.txt              # Sample user profile text data file
│   ├── pro3.py                # Menu-driven student record file saver
│   └── student_records.txt    # Appended student text database
│
├── day4/
│   ├── bank.py                # Bank account class (encapsulation demo)
│   ├── book.py                # Library book tracking system
│   ├── car.py                 # Vehicle class methods & initialization
│   ├── evenodd.py             # Parity check utilities without built-ins
│   ├── maxlist.py             # Linear scan maximum finder without built-ins
│   ├── pro4.py                # Integrated OOP student report generator with file export
│   ├── report_cards.txt       # Generated report card output
│   └── reverse.py             # Sequence reversal via slicing and explicit loops
│
├── day5/
│   ├── Day05_Advanced_Python/
│   │   ├── recursion_practice.py     # Recursive countdown, sum, factorial, fibonacci, reverse, power
│   │   └── lambdas_and_builtins.py   # Anonymous lambda functions, map(), and filter()
│   │
│   ├── DSA/
│   │   ├── Stacks/
│   │   │   └── stack_list.py         # LIFO stack implementation via Python list
│   │   └── Queues/
│   │       └── queue_deque.py        # FIFO queue implementation using collections.deque
│   │
│   └── Mini_Projects/
│       └── stack_queue_simulator.py  # Menu-driven Stack & Queue console emulator
│
├── day6/
│   ├── DSA/
│   │   ├── count_occurrences.py      # Target frequency count without .count()
│   │   ├── frequency_counter.py      # Full frequency map via dictionary
│   │   ├── linear_search.py          # Linear search with O(n) complexity note
│   │   └── second_largest.py         # Single-pass second maximum finder
│   │
│   └── NumPy/
│       ├── numpy_basics.py           # 1D/2D array inspection & reshaping
│       └── student_performance.py    # 2D array statistics across axes
│
├── day7/
│   ├── DSA/
│   │   ├── binary_search.py          # Iterative & recursive binary search
│   │   ├── floor_and_ceiling.py      # Bound search in sorted array
│   │   └── search_insert_position.py # Target search and insertion index finder
│   │
│   ├── Mini_Projects/
│   │   └── sensor_analyzer.py        # Pipeline: Noise cleaning, imputation & search benchmark
│   │
│   └── NumPy/
│       ├── boolean_masking.py        # Outlier filtering and imputation
│       └── broadcasting_basics.py    # Dimension expansion & row/col operations
│
├── day8/
│   ├── DSA/
│   │   ├── remove_element.py         # Two-pointer in-place value removal
│   │   ├── two_sum_sorted.py         # Two-pointer pair sum on sorted array
│   │   └── valid_palindrome.py       # Inward two-pointer palindrome verification
│   │
│   └── Pandas/
│       ├── data_inspection.py        # Profiling via head, tail, info, and describe
│       └── series_and_dataframes.py  # Series indexing and DataFrame creation
│
├── day9/
│   ├── DSA/
│   │   ├── contains_duplicate_ii.py  # Sliding window with set for nearby duplicates
│   │   ├── max_sum_subarray.py       # Fixed-size sliding window (size k)
│   │   └── smallest_subarray_sum.py  # Dynamic-size sliding window (target sum)
│   │
│   └── Pandas/
│       ├── filtering_selection.py    # Conditional filtering, .loc vs .iloc indexing
│       └── handling_missing_data.py  # isna(), fillna(), dropna(), and forward/backward fill
│
└── day10/
    ├── DSA/
    │   ├── peak_element.py            # Finding a local peak element in O(log n)
    │   ├── search_rotated_array.py    # Binary search in a rotated sorted array
    │   └── search_2d_matrix.py        # Matrix search using virtual 1D index mapping
    │
    └── Pandas/
        ├── groupby_aggregations.py    # GroupBy splits, multi-column aggregates, and transforms
        └── feature_transformations.py # Value binning (pd.cut), string operations, and derived columns
```

---

## 🛠️ How to Run

Clone the repository and run any module directly:

```bash
git clone [https://github.com/soumilichanda/python-learning-journey.git](https://github.com/soumilichanda/python-learning-journey.git)
cd python-learning-journey

# Example: Run Day 5 Advanced Python recursion tasks
python day5/Day05_Advanced_Python/recursion_practice.py

# Example: Run Day 6 Student Performance NumPy script
python day6/NumPy/student_performance.py

# Example: Run the Stack & Queue Simulator Mini-Project
python day5/Mini_Projects/stack_queue_simulator.py
```