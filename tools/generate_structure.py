"""
Script to generate the complete folder and file structure for Striver's A2Z DSA Sheet
Creates all source (.cpp) and documentation (.md) files with proper numbering
"""

import os
from pathlib import Path


def create_structure():
    """Create the complete project structure"""
    
    base_dir = Path(__file__).parent
    
    # Define the complete structure
    structure = {
        # 01. Learn the Basics
        "01_basics": {
            "01_things_to_know": [
                "user_input_output",
                "data_types",
                "if_else_statements",
                "switch_statement",
                "arrays_strings",
                "for_loops",
                "while_loops",
                "functions_pass_by_reference_value",
                "time_complexity",
                "space_complexity"
            ],
            "02_logical_thinking": [
                "rectangular_star_pattern",
                "right_angled_triangle_pattern",
                "right_angled_number_pyramid",
                "right_angled_number_pyramid_ii",
                "inverted_right_pyramid",
                "inverted_numbered_right_pyramid",
                "star_pyramid",
                "inverted_star_pyramid",
                "diamond_star_pattern",
                "half_diamond_star_pattern",
                "binary_number_triangle_pattern",
                "number_crown_pattern",
                "increasing_number_triangle_pattern",
                "increasing_letter_triangle_pattern",
                "reverse_letter_triangle_pattern",
                "alpha_ramp_pattern",
                "alpha_hill_pattern",
                "alpha_triangle_pattern",
                "symmetric_void_pattern",
                "symmetric_butterfly_pattern",
                "hollow_rectangle_pattern",
                "the_number_pattern"
            ],
            "03_stl_collections": [
                "cpp_stl",
                "comparators"
            ],
            "04_basic_maths": [
                "count_digits",
                "reverse_number",
                "check_palindrome",
                "gcd_hcf",
                "armstrong_numbers",
                "print_all_divisors",
                "check_prime"
            ],
            "05_basic_recursion": [
                "understanding_recursion",
                "print_1_to_n_without_loop",
                "print_n_to_1_without_loop",
                "sum_of_first_n_natural_numbers",
                "factorial_of_n_numbers",
                "reverse_array",
                "check_string_palindrome",
                "fibonacci_number"
            ],
            "06_basic_hashing": [
                "hashing_theory",
                "counting_frequencies_array_elements",
                "find_highest_lowest_frequency_element"
            ]
        },
        
        # 02. Sorting Techniques
        "02_sorting": {
            "01_sorting_basic": [
                "selection_sort",
                "bubble_sort",
                "insertion_sort"
            ],
            "02_sorting_advanced": [
                "merge_sort",
                "recursive_bubble_sort",
                "recursive_insertion_sort",
                "quick_sort"
            ]
        },
        
        # 03. Arrays
        "03_arrays": {
            "01_easy": [
                "largest_element_in_array",
                "second_largest_element",
                "check_array_sorted",
                "remove_duplicates_sorted_array",
                "left_rotate_array_one_place",
                "left_rotate_array_d_places",
                "move_zeros_to_end",
                "linear_search",
                "union_two_sorted_arrays",
                "find_missing_number",
                "maximum_consecutive_ones",
                "number_appears_once",
                "longest_subarray_sum_k_positives",
                "longest_subarray_sum_k_mixed"
            ],
            "02_medium": [
                "2sum_problem",
                "sort_0_1_2",
                "majority_element_n_by_2",
                "kadanes_algorithm",
                "print_subarray_maximum_sum",
                "stock_buy_sell",
                "rearrange_array_by_sign",
                "next_permutation",
                "leaders_in_array",
                "longest_consecutive_sequence",
                "set_matrix_zeros",
                "rotate_matrix_90_degrees",
                "spiral_matrix",
                "count_subarrays_with_sum"
            ],
            "03_hard": [
                "pascals_triangle",
                "majority_element_n_by_3",
                "3sum_problem",
                "4sum_problem",
                "count_subarrays_xor_k",
                "merge_overlapping_intervals",
                "merge_sorted_arrays_no_extra_space",
                "find_repeating_missing_number",
                "count_inversions",
                "reverse_pairs",
                "maximum_product_subarray",
                "missing_repeating_numbers"
            ]
        },
        
        # 04. Binary Search
        "04_binary_search": {
            "01_bs_on_1d_arrays": [
                "binary_search_sorted_array",
                "implement_lower_bound",
                "implement_upper_bound",
                "search_insert_position",
                "floor_ceil_sorted_array",
                "first_last_occurrence",
                "count_occurrences",
                "search_rotated_sorted_array_i",
                "search_rotated_sorted_array_ii",
                "find_minimum_rotated_sorted_array",
                "array_rotation_count",
                "single_element_sorted_array",
                "find_peak_element"
            ],
            "02_bs_on_answers": [
                "sqrt_binary_search",
                "nth_root_binary_search",
                "koko_eating_bananas",
                "minimum_days_bouquets",
                "smallest_divisor",
                "capacity_ship_packages",
                "kth_missing_positive",
                "aggressive_cows",
                "allocate_books",
                "split_array_largest_sum",
                "painters_partition",
                "minimize_max_distance_gas_station",
                "median_2_sorted_arrays",
                "kth_element_2_sorted_arrays"
            ],
            "03_bs_on_2d_arrays": [
                "row_with_max_1s",
                "search_2d_matrix",
                "search_row_column_sorted_matrix",
                "find_peak_element_2d",
                "matrix_median"
            ]
        },
        
        # 05. Strings
        "05_strings": {
            "01_basic_easy": [
                "remove_outermost_parentheses",
                "reverse_words_palindrome_check",
                "largest_odd_number",
                "longest_common_prefix",
                "isomorphic_string",
                "string_rotation",
                "check_anagram"
            ],
            "02_medium": [
                "sort_characters_by_frequency",
                "maximum_nesting_depth",
                "roman_integer_conversion",
                "implement_atoi",
                "count_k_different_characters",
                "longest_palindromic_substring",
                "sum_beauty_substrings",
                "reverse_every_word"
            ]
        },
        
        # 06. LinkedList
        "06_linkedlist": {
            "01_single_ll": [
                "introduction_linkedlist",
                "inserting_node",
                "deleting_node",
                "find_length",
                "search_element"
            ],
            "02_doubly_ll": [
                "introduction_doubly_linkedlist",
                "insert_node_dll",
                "delete_node_dll",
                "reverse_dll"
            ],
            "03_medium_ll": [
                "middle_linkedlist",
                "reverse_linkedlist",
                "detect_loop",
                "find_starting_point_loop",
                "length_of_loop",
                "check_palindrome",
                "segregate_odd_even_nodes",
                "remove_nth_node_end",
                "delete_middle_node",
                "sort_0_1_2",
                "intersection_point_y_ll",
                "add_1_to_number",
                "add_2_numbers"
            ],
            "04_medium_dll": [
                "delete_occurrences_dll",
                "find_pairs_sum_dll",
                "remove_duplicates_sorted_dll"
            ],
            "05_hard_ll": [
                "reverse_ll_group_k",
                "rotate_ll",
                "flattening_ll",
                "clone_ll_random_pointer",
                "design_browser_history"
            ]
        },
        
        # 07. Recursion
        "07_recursion": {
            "01_strong_hold": [
                "recursive_atoi",
                "pow_x_n",
                "count_good_numbers",
                "sort_stack_recursion",
                "reverse_stack_recursion"
            ],
            "02_subsequences_pattern": [
                "generate_binary_strings",
                "generate_parentheses",
                "print_subsequences_power_set",
                "all_patterns_subsequences",
                "count_subsequences_sum_k",
                "check_subsequence_sum_k",
                "combination_sum",
                "combination_sum_ii",
                "subset_sum_i",
                "subset_sum_ii",
                "combination_sum_iii",
                "letter_combinations_phone"
            ],
            "03_hard_combos": [
                "palindrome_partitioning",
                "word_search",
                "n_queen",
                "rat_in_maze",
                "word_break",
                "m_coloring_problem",
                "sudoku_solver",
                "expression_add_operators"
            ]
        },
        
        # 08. Bit Manipulation
        "08_bit_manipulation": {
            "01_concepts": [
                "introduction_bit_manipulation",
                "check_ith_bit_set",
                "check_odd_number",
                "check_power_of_2",
                "count_set_bits",
                "set_unset_rightmost_bit",
                "swap_two_numbers",
                "divide_without_operators",
                "count_bits_flip_a_to_b",
                "number_appears_odd_times",
                "power_set",
                "xor_numbers_l_to_r",
                "two_numbers_odd_times"
            ],
            "02_interview_problems": [
                "prime_factors_number",
                "all_prime_factors",
                "all_divisors",
                "sieve_of_eratosthenes",
                "all_primes_up_to_n"
            ]
        },
        
        # 09. Stack and Queues
        "09_stack_queues": {
            "01_learning": [
                "stack_using_arrays",
                "queue_using_arrays",
                "stack_using_queue",
                "queue_using_stack",
                "balanced_parentheses",
                "min_stack",
                "infix_to_postfix",
                "prefix_to_infix",
                "prefix_to_postfix",
                "postfix_to_prefix",
                "postfix_to_infix",
                "infix_to_prefix"
            ],
            "02_monotonic_stack_queue": [
                "next_greater_element",
                "next_greater_element_ii",
                "next_smaller_element",
                "number_nges_right",
                "trapping_rainwater",
                "sum_subarray_minimum",
                "stock_span_problem",
                "asteroid_collision",
                "sum_subarray_ranges",
                "remove_k_digits",
                "largest_rectangle_histogram",
                "maximal_rectangles"
            ],
            "03_implementation": [
                "sliding_window_maximum",
                "stock_span_problem",
                "celebrity_problem",
                "lru_cache",
                "lfu_cache"
            ]
        },
        
        # 10. Sliding Window & Two Pointer
        "10_sliding_window": {
            "01_medium": [
                "longest_substring_no_repeat",
                "max_consecutive_ones_iii",
                "fruit_into_baskets",
                "longest_repeating_char_replacement",
                "binary_subarray_sum",
                "count_nice_subarrays",
                "substring_all_three_characters",
                "maximum_points_from_cards"
            ],
            "02_hard": [
                "longest_substring_k_distinct",
                "subarray_k_different_integers",
                "minimum_window_substring",
                "minimum_window_subsequence"
            ]
        },
        
        # 11. Heaps
        "11_heaps": {
            "01_learning": [
                "priority_queues",
                "min_max_heap_implementation",
                "check_array_heap",
                "convert_min_to_max_heap"
            ],
            "02_medium": [
                "kth_largest_element",
                "kth_smallest_element",
                "sort_k_sorted_array",
                "merge_m_sorted_lists",
                "replace_element_by_rank",
                "task_scheduler",
                "hands_of_straights"
            ],
            "03_hard": [
                "design_twitter",
                "connect_ropes_min_cost",
                "kth_largest_stream",
                "maximum_sum_combination",
                "find_median_data_stream",
                "k_most_frequent_elements"
            ]
        },
        
        # 12. Greedy Algorithms
        "12_greedy": {
            "01_easy": [
                "assign_cookies",
                "fractional_knapsack",
                "min_coins",
                "lemonade_change",
                "valid_parenthesis_checker"
            ],
            "02_medium_hard": [
                "n_meetings_one_room",
                "jump_game",
                "jump_game_ii",
                "min_platforms_railway",
                "job_sequencing",
                "candy",
                "shortest_job_first",
                "lru_page_replacement",
                "insert_interval",
                "merge_intervals",
                "non_overlapping_intervals"
            ]
        },
        
        # 13. Binary Trees
        "13_binary_trees": {
            "01_traversals": [
                "introduction_trees",
                "binary_tree_representation",
                "binary_tree_traversals",
                "preorder_traversal",
                "inorder_traversal",
                "postorder_traversal",
                "level_order_traversal",
                "iterative_preorder",
                "iterative_inorder",
                "postorder_2_stack",
                "postorder_1_stack",
                "all_traversals_in_one"
            ],
            "02_medium": [
                "height_binary_tree",
                "check_height_balanced",
                "diameter_binary_tree",
                "maximum_path_sum",
                "check_identical_trees",
                "zigzag_traversal",
                "boundary_traversal",
                "vertical_order_traversal",
                "top_view",
                "bottom_view",
                "right_left_view",
                "symmetrical_trees",
                "root_to_node_path",
                "lowest_common_ancestor",
                "maximum_width",
                "children_sum_property"
            ],
            "03_hard": [
                "nodes_distance_k",
                "burn_tree_min_time",
                "count_nodes_complete_tree",
                "unique_binary_tree_theory",
                "construct_from_preorder_inorder",
                "construct_from_postorder_inorder",
                "serialize_deserialize",
                "morris_preorder",
                "morris_inorder",
                "flatten_to_linkedlist"
            ]
        },
        
        # 14. Binary Search Trees
        "14_bst": {
            "01_concepts": [
                "introduction_bst",
                "search_bst",
                "find_min_max_bst",
                "ceil_bst",
                "floor_bst",
                "insert_node_bst",
                "delete_node_bst",
                "kth_smallest_largest"
            ],
            "02_practice": [
                "check_bst",
                "lca_bst",
                "construct_bst_preorder",
                "inorder_successor_predecessor",
                "merge_two_bst",
                "two_sum_bst",
                "recover_bst",
                "largest_bst_binary_tree"
            ]
        },
        
        # 15. Graphs
        "15_graphs": {
            "01_learning": [
                "graph_types",
                "graph_representation",
                "connected_components",
                "bfs",
                "dfs"
            ],
            "02_bfs_dfs_problems": [
                "number_of_provinces",
                "number_of_islands",
                "flood_fill",
                "rotten_oranges",
                "cycle_undirected_bfs",
                "cycle_undirected_dfs",
                "distance_nearest_1",
                "replace_os_with_xs",
                "number_of_enclaves",
                "distinct_islands",
                "bipartite_bfs",
                "bipartite_dfs",
                "cycle_directed_dfs",
                "cycle_directed_bfs",
                "eventual_safe_states",
                "topological_sort_dfs",
                "kahns_algorithm",
                "cycle_topological_sort",
                "course_schedule",
                "safe_states_topological",
                "alien_dictionary"
            ],
            "03_shortest_path": [
                "shortest_path_ug_unit_weights",
                "shortest_path_dag",
                "dijkstras_algorithm",
                "priority_queue_dijkstra",
                "shortest_path_binary_maze",
                "path_minimum_effort",
                "cheapest_flights_k_stops",
                "network_delay_time",
                "minimum_multiplications",
                "ways_arrive_destination",
                "bellman_ford",
                "floyd_warshall",
                "city_threshold_distance"
            ],
            "04_other_algorithms": [
                "minimum_spanning_tree",
                "prims_algorithm",
                "disjoint_set_union_rank",
                "disjoint_set_union_size",
                "kruskals_algorithm",
                "network_connected",
                "stones_removed",
                "accounts_merge",
                "islands_ii",
                "large_island",
                "swim_rising_water",
                "articulation_point",
                "bridges_graph",
                "kosarajus_algorithm"
            ]
        },
        
        # 16. Dynamic Programming
        "16_dp": {
            "01_introduction": [
                "introduction_dp",
                "dp_introduction",
                "climbing_stairs",
                "frog_jump",
                "frog_jump_k_distances"
            ],
            "02_1d_dp": [
                "max_sum_non_adjacent",
                "house_robber",
                "house_robber_ii"
            ],
            "03_2d_3d_grids": [
                "ninjas_training",
                "grid_unique_paths",
                "grid_unique_paths_2",
                "minimum_path_sum",
                "max_path_sum_matrix",
                "triangle",
                "falling_path_sum",
                "3d_dp"
            ],
            "04_subsequences": [
                "subset_sum_target",
                "partition_equal_subset",
                "partition_min_absolute_diff",
                "count_subsets_sum_k",
                "count_partitions_difference",
                "target_sum",
                "01_knapsack",
                "minimum_coins",
                "target_sum",
                "coin_change_2",
                "unbounded_knapsack",
                "rod_cutting"
            ],
            "05_strings": [
                "longest_common_subsequence",
                "print_lcs",
                "longest_common_substring",
                "longest_palindromic_subsequence",
                "min_insertions_palindrome",
                "min_insertions_deletions",
                "shortest_common_supersequence",
                "distinct_subsequences",
                "edit_distance",
                "wildcard_matching"
            ],
            "06_stocks": [
                "buy_sell_stocks",
                "buy_sell_stock_ii",
                "buy_sell_stocks_iii",
                "buy_sell_stock_iv",
                "buy_sell_cooldown",
                "buy_sell_transaction_fee"
            ],
            "07_lis": [
                "longest_increasing_subsequence",
                "printing_lis",
                "longest_increasing_subsequence_alt",
                "largest_divisible_subset",
                "longest_string_chain",
                "longest_bitonic_subsequence",
                "number_of_lis"
            ],
            "08_mcm_partition": [
                "matrix_chain_multiplication",
                "min_cost_cut_stick",
                "burst_balloons",
                "evaluate_boolean_expression",
                "palindrome_partitioning_ii",
                "partition_array_max_sum"
            ],
            "09_squares": [
                "max_rectangle_area_1s",
                "count_square_submatrices"
            ]
        },
        
        # 17. Tries
        "17_tries": {
            "01_theory": [
                "implement_trie",
                "implement_trie_2"
            ],
            "02_problems": [
                "longest_string_all_prefixes",
                "distinct_substrings",
                "bit_prerequisites",
                "max_xor_two_numbers",
                "max_xor_with_element"
            ]
        },
        
        # 18. Advanced Strings
        "18_advanced_strings": {
            "01_hard_problems": [
                "min_bracket_reversals",
                "count_and_say",
                "hash_function_string",
                "rabin_karp",
                "z_function",
                "kmp_lps_array",
                "shortest_palindrome",
                "longest_happy_prefix"
            ]
        }
    }
    
    # Create all folders and files
    total_files = 0
    total_folders = 0
    
    for section, subsections in structure.items():
        for subsection, files in subsections.items():
            # Create source directory
            source_dir = base_dir / "source" / section / subsection
            source_dir.mkdir(parents=True, exist_ok=True)
            total_folders += 1
            
            # Create documentation directory
            doc_dir = base_dir / "documentation" / section / subsection
            doc_dir.mkdir(parents=True, exist_ok=True)
            total_folders += 1
            
            # Create files with numbering
            for idx, file_name in enumerate(files, start=1):
                # Create .cpp file with template
                cpp_file = source_dir / f"{idx:02d}_{file_name}.cpp"
                cpp_template = """#include<iostream>
using namespace std;

int main() {
    
    return 0;
}"""
                cpp_file.write_text(cpp_template)
                total_files += 1
                
                # Create .md file
                md_file = doc_dir / f"{idx:02d}_{file_name}.md"
                md_file.touch()
                total_files += 1
            
            print(f"Created: {section}/{subsection} ({len(files)} files)")
    
    print(f"\n{'='*60}")
    print(f"Structure created successfully!")
    print(f"Total folders created: {total_folders}")
    print(f"Total files created: {total_files}")
    print(f"{'='*60}")


if __name__ == "__main__":
    print("Starting structure generation...")
    print(f"{'='*60}\n")
    create_structure()
