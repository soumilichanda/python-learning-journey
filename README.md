
# Python Learning Journey 🚀

A structured repository documenting daily Python concepts, code implementations, Data Structures & Algorithms (DSA), Machine Learning foundations, and production serving engines.

---

## 📁 Repository Structure

```text
python-learning-journey/
│
├── day01/
│   ├── calculator.py                  # Basic arithmetic CLI calculator
│   ├── hello.py                       # Intro syntax & output formatting
│   ├── marks_analyzer.py              # Grade calculation & conditional logic
│   └── welcome.py                     # User input & greeting scripts
│
├── day02/
│   ├── abc.py                         # Persistent student record manager with file storage
│   ├── arr.py                         # Manual list iterations, min, max & average
│   ├── calcfunc.py                    # Modular function-based calculator with error handling
│   ├── marks.py                       # Conditional pass/fail grading logic
│   ├── name.py                        # String manipulation and function definitions
│   ├── sq.py                          # Math functions & square calculations
│   ├── student_marks.py               # In-memory dictionary-based student record processor
│   └── student_records.txt            # Text-based flat-file storage
│
├── day03/
│   ├── case.py                        # String case methods & character length logic
│   ├── file.py                        # File read/write operations via context managers
│   ├── notes.txt                      # Sample user profile text data file
│   ├── pro3.py                        # Menu-driven student record file saver
│   └── student_records.txt            # Appended student text database
│
├── day04/
│   ├── bank.py                        # Bank account class (encapsulation demo)
│   ├── book.py                        # Library book tracking system
│   ├── car.py                         # Vehicle class methods & initialization
│   ├── evenodd.py                     # Parity check utilities without built-ins
│   ├── maxlist.py                     # Linear scan maximum finder without built-ins
│   ├── pro4.py                        # Integrated OOP student report generator with file export
│   ├── report_cards.txt               # Generated report card output
│   └── reverse.py                     # Sequence reversal via slicing and explicit loops
│
├── day05/
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
├── day06/
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
├── day07/
│   ├── DSA/
│   │   ├── binary_search.py          # Logarithmic search in sorted array
│   │   └── search_insert_position.py # Binary search ceiling index lookup
│   │
│   └── NumPy/
│       └── sensor_analyzer.py        # Milestone 1: 2D vector broadcasting, boolean masks, matrix aggregation
│
├── day08/
│   ├── DSA/
│   │   ├── remove_element.py         # In-place array overwrite with two pointers
│   │   ├── two_sum_sorted.py         # Two-pointer inward scan on sorted arrays
│   │   └── valid_palindrome.py       # Two-pointer alphanumeric validation
│   │
│   └── Pandas/
│       ├── data_inspection.py        # DataFrame schema, dtypes, summary metrics
│       └── series_and_dataframes.py  # Series indexing and DataFrame creation
│
├── day09/
│   ├── DSA/
│   │   ├── contains_duplicate_ii.py  # Sliding window lookup with set
│   │   ├── max_sum_subarray.py       # Fixed-size sliding window (size k)
│   │   └── smallest_subarray_sum.py  # Dynamic sliding window target sum
│   │
│   └── Pandas/
│       ├── filtering_selection.py    # Boolean masks, .loc vs .iloc slicing
│       └── handling_missing_data.py  # Null detection, dropna, and statistical imputation
│
├── day10/
│   ├── DSA/
│   │   └── search_rotated_sorted.py  # Binary search on rotated monotonic segments
│   │
│   └── Pandas/
│       └── groupby_aggregations.py   # Multi-level aggregations and statistical transformations
│
├── day11/
│   ├── DSA/
│   │   └── merge_sort.py             # Divide-and-conquer sorting in O(n log n)
│   │
│   └── Pandas/
│       └── merge_and_concat.py       # Relational joins, keys, and axis concatenations
│
├── day12/
│   ├── DSA/
│   │   ├── group_anagrams.py         # Frequency tuple signatures for hash grouping
│   │   ├── two_sum_hashmap.py        # One-pass hash map complement search in O(n)
│   │   └── valid_anagram.py          # Character frequency hash table comparison
│   │
│   └── Vision_Prep/
│       ├── image_augmentations.py    # Horizontal flip, brightness delta, and Gaussian noise
│       └── image_resizing_scaling.py # Nearest-neighbor resize and [0.0, 1.0] scaling
│
├── day13/
│   ├── DSA/
│   │   ├── delete_node.py            # Pointer manipulation for head, middle, tail deletion
│   │   ├── search_linked_list.py     # Element search and iterative length traversal
│   │   └── singly_linked_list.py     # Node creation, head/tail insertion, traversal
│   │
│   └── ML_Foundations/
│       ├── feature_scaling_prep.py   # Zero-leakage MinMax & Standard scaling
│       └── train_test_split.py       # Random permutation dataset partitioning in pure NumPy
│
├── day14/
│   ├── DSA/
│   │   ├── linked_list_cycle.py      # Floyd's cycle detection via two-speed pointers
│   │   ├── middle_of_linked_list.py  # Fast and slow pointer midpoint lookup
│   │   └── reverse_linked_list.py    # In-place iterative 3-pointer list reversal
│   │
│   └── ML_Classification/
│       ├── logistic_regression.py    # Sigmoid, binary cross-entropy, and gradient descent
│       └── model_evaluation.py       # Confusion matrix, Precision, Recall, and F1 calculations
│
├── day15/
│   ├── DSA/
│   │   ├── next_greater_element.py   # Monotonic decreasing stack in O(n)
│   │   └── valid_parentheses.py      # Stack validation with hash map matching
│   │
│   └── ML_Evaluation/
│       ├── diagnostic_report.py      # Multi-metric classification evaluation suite
│       └── threshold_analysis.py     # Threshold tuning and Precision-Recall tradeoffs
│
├── day16/
│   ├── DSA/
│   │   ├── circular_queue.py         # Fixed-buffer ring queue with modular arithmetic
│   │   ├── queue_via_stacks.py       # FIFO queue using two LIFO stacks
│   │   └── sliding_window_max.py     # Monotonic double-ended queue in O(n)
│   │
│   └── ML_Supervised/
│       ├── decision_tree_entropy.py  # Information Gain and Shannon Entropy splitting
│       └── svm_decision_boundary.py  # Linear SVM margin width and C-penalty analysis
│
├── day17/
│   ├── DSA/
│   │   ├── combination_sum.py        # Backtracking with branch pruning and element reuse
│   │   └── recursion_subsets.py      # Backtracking power set decision tree in O(2^n)
│   │
│   └── ML_Ensembles/
│       ├── grid_search_tuning.py     # Cross-validated hyperparameter grid sweep (GridSearchCV)
│       └── random_forest_builder.py  # Bagging & feature subsampling random forest from scratch
│
├── day18/
│   ├── DSA/
│   │   ├── combinations.py           # Combinatorial branch-pruning in O(C(n, k))
│   │   └── permutations.py           # State-space tree backtracking in O(n!) time
│   │
│   └── ML_Pipelines/
│       ├── column_transformer_prep.py # ColumnTransformer with StandardScaler & OneHotEncoder
│       └── reusable_pipeline.py      # End-to-end Pipeline training and leak-free cross-validation
│
├── day19/
│   ├── DSA/
│   │   ├── subsets_ii.py             # Backtracking with duplicate handling & sorting
│   │   └── word_search.py            # 2D Grid DFS backtracking with in-place visited tracking
│   │
│   └── Mini_Projects/
│       └── ml_pipeline_engine.py     # Milestone 2: Reusable tabular classification engine
│
├── day20/
│   ├── DSA/
│   │   ├── binary_tree_traversals.py # DFS Traversals: In-order, Pre-order, Post-order
│   │   └── max_depth_binary_tree.py  # Recursive depth computation & leaf invariants
│   │
│   └── Tensors/
│       ├── autograd_simulation.py    # Computational graph forward pass & manual backprop
│       └── tensor_mechanics.py       # Strides, memory layouts, rank, shape & device dispatch
│
├── day21/
│   ├── DSA/
│   │   ├── binary_tree_right_view.py # BFS tracking the rightmost node per layer
│   │   └── level_order_traversal.py  # BFS queue-based layer-by-layer traversal
│   │
│   ├── Mini_Projects/
│   │   └── task_scheduler.py         # Milestone 3: In-memory task scheduler & transaction engine
│   │
│   └── Optimizers/
│       ├── gradient_descent_engine.py# Gradient calculation & parameter updates in NumPy
│       └── loss_functions.py         # Vectorized MSE & Categorical Cross-Entropy
│
├── day22/
│   ├── DSA/
│   │   ├── bst_operations.py         # BST node insertion, search, and min/max lookup
│   │   └── validate_bst.py           # Strict monotonic range validation in O(n)
│   │
│   └── Deep_Learning/
│       ├── linear_neuron_classifier.py # Sigmoid perceptron with cross-entropy update rule
│       └── perceptron_scratch.py     # Binary step perceptron learning algorithm
│
├── day23/
│   ├── DSA/
│   │   ├── kth_largest_element.py    # Min-Heap of size k for O(n log k) stream ranking
│   │   └── top_k_frequent.py         # Frequency hash map combined with heap extraction
│   │
│   └── Deep_Learning/
│       ├── batch_data_loader.py      # Custom dataset batching, epoch shuffling, and drop_last logic
│       └── data_augmentation_ops.py  # Vectorized random cropping, flips, and normalization
│
├── day24/
│   ├── CNN_Foundations/
│   │   ├── conv2d_scratch.py         # Vectorized 2D cross-correlation kernel with stride and padding
│   │   └── max_pooling_scratch.py    # Spatial downsampling engine with 2D pooling windows
│   │
│   └── DSA/
│       ├── find_center_star_graph.py # Degree validation and center lookup in O(1) space
│       └── graph_representations.py  # Adjacency List vs. Adjacency Matrix conversions & vertex degree
│
├── day25/
│   ├── DSA/
│   │   ├── graph_bfs_shortest_path.py # Unweighted shortest path using queue & parent mapping
│   │   └── number_of_islands.py      # 2D grid BFS traversal with visited coordinate tracking
│   │
│   ├── Mini_Projects/
│   │   └── vision_feature_harness.py # Milestone 4: Multi-layer vision feature extractor & activation logger
│   │
│   └── Vision_Foundations/
│       └── activation_functions.py   # Vectorized ReLU, LeakyReLU, and analytical forward/backward derivatives
│
├── day26/
│   ├── DSA/
│   │   ├── course_schedule_cycle.py          # Directed cycle detection via 3-color DFS state
│   │   └── graph_dfs_connected_components.py # Undirected component counting & traversal
│   │
│   └── Vision_Foundations/
│       ├── cnn_layer_activation_maps.py      # Multi-filter activation logging & receptive field inspector
│       └── transfer_backbone_simulation.py   # Frozen feature-extractor simulation with trainable classifier head
│
├── day27/
│   ├── DSA/
│   │   ├── climbing_stairs.py        # Top-down memoization vs. bottom-up tabulation
│   │   └── coin_change_min.py        # Unbounded knapsack 1D tabulation in O(amount * n)
│   │
│   └── Model_Serving/
│       └── inference_dashboard.py    # Interactive web interface for tabular/vision model predictions
│
├── day28/
│   ├── DSA/
│   │   ├── longest_common_subseq.py  # Classical 2D DP LCS table construction in O(m * n)
│   │   └── unique_paths_grid.py      # 2D DP grid navigation with O(n) rolling-row space
│   │
│   └── Model_Deployment/
│       └── artifact_packager.py      # Deterministic model serialization, metadata bundling & validation
│
├── day29/
│   ├── DSA/
│   │   ├── knapsack_01.py                # Classical 0/1 knapsack with rolling 1D DP array
│   │   └── longest_increasing_subseq.py  # LIS via binary search patience sorting in O(n log n)
│   │
│   └── Production_Serving/
│       ├── app.py                        # Milestone 5 (Part 1): FastAPI microservice for batch & single prediction
│       └── telemetry_logger.py           # Latency profiling, request counter & drift metrics
│
└── day30/
    ├── DSA/
    │   ├── bit_manipulation_ops.py       # Bitwise manipulation invariants (Hamming weight & single number)
    │   └── min_cost_climbing_stairs.py   # Space-optimized bottom-up DP in O(1) auxiliary space
    │
    └── Production_Capstone/
        ├── inference_cache.py            # Milestone 5 (Part 2): LRU caching layer for deterministic model serving
        └── system_benchmark.py           # Latency profiling, throughput stress testing & telemetry report

```

---

## 🏆 Key Engineering Milestones Built From Scratch

| Milestone | Architecture & Module | Core Capabilities |
| :--- | :--- | :--- |
| **Milestone 1** (Day 07) | `SensorSignalProcessor` | Vectorized outlier filtering, statistical imputation, and logarithmic search via pure NumPy. |
| **Milestone 2** (Days 18–19) | `MLPipelineEngine` | Automated tabular ML training pipeline: zero-leakage custom scaling, train-test splitting, and threshold-tuned diagnostics. |
| **Milestone 3** (Days 20–21) | `TaskScheduler` & `TransactionEngine` | In-memory priority scheduling, level-order BFS dependency resolution, and dual-stack undo/redo rollback engine. |
| **Milestone 4** (Days 25–26) | `VisionFeatureHarness` | From-scratch computer vision engine: 2D cross-correlation kernels, spatial pooling, and layer-by-layer activation inspection. |
| **Milestone 5** (Days 29–30) | `ProductionServingEngine` | Asynchronous FastAPI inference microservice, in-memory LRU prediction caching, and live latency telemetry. |

---

## 🛠️ How to Run

Clone the repository and run any module directly:

```bash
git clone https://github.com/soumilichanda/python-learning-journey.git
cd python-learning-journey

# Example: Run Day 29 Production Serving API
python day29/Production_Serving/app.py

# Example: Run Day 30 Capstone System Benchmark
python day30/Production_Capstone/system_benchmark.py