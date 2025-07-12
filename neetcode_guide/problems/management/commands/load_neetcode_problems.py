from django.core.management.base import BaseCommand
from problems.models import Problem

class Command(BaseCommand):
    help = 'Load NeetCode 150 problems into the database'

    def title_to_url(self, title):
        '''Convert problem title to LeetCode URL'''
        url_slug = title.lower().replace(' ', '-')
        
        import re
        url_slug = re.sub(r'[^a-z0-9\-]', '', url_slug)
        
        url_slug = re.sub(r'-+', '-', url_slug)
        
        url_slug = url_slug.strip('-')
        
        return f'https://leetcode.com/problems/{url_slug}/'

    def handle(self, *args, **options):
        problems_data = [
            # Arrays & Hashing
            {'number': 217, 'title': 'Contains Duplicate', 'difficulty': 'Easy', 'topic': 'Arrays & Hashing'},
            {'number': 242, 'title': 'Valid Anagram', 'difficulty': 'Easy', 'topic': 'Arrays & Hashing'},
            {'number': 1, 'title': 'Two Sum', 'difficulty': 'Easy', 'topic': 'Arrays & Hashing'},
            {'number': 49, 'title': 'Group Anagrams', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            {'number': 347, 'title': 'Top K Frequent Elements', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            {'number': 271, 'title': 'Encode and Decode Strings', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            {'number': 238, 'title': 'Product of Array Except Self', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            {'number': 36, 'title': 'Valid Sudoku', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            {'number': 128, 'title': 'Longest Consecutive Sequence', 'difficulty': 'Medium', 'topic': 'Arrays & Hashing'},
            
            # Two Pointers
            {'number': 125, 'title': 'Valid Palindrome', 'difficulty': 'Easy', 'topic': 'Two Pointers'},
            {'number': 167, 'title': 'Two Sum II - Input Array Is Sorted', 'difficulty': 'Medium', 'topic': 'Two Pointers'},
            {'number': 15, 'title': '3Sum', 'difficulty': 'Medium', 'topic': 'Two Pointers'},
            {'number': 11, 'title': 'Container With Most Water', 'difficulty': 'Medium', 'topic': 'Two Pointers'},
            {'number': 42, 'title': 'Trapping Rain Water', 'difficulty': 'Hard', 'topic': 'Two Pointers'},
            
            # Stack
            {'number': 20, 'title': 'Valid Parentheses', 'difficulty': 'Easy', 'topic': 'Stack'},
            {'number': 155, 'title': 'Min Stack', 'difficulty': 'Medium', 'topic': 'Stack'},
            {'number': 150, 'title': 'Evaluate Reverse Polish Notation', 'difficulty': 'Medium', 'topic': 'Stack'},
            {'number': 22, 'title': 'Generate Parentheses', 'difficulty': 'Medium', 'topic': 'Stack'},
            {'number': 739, 'title': 'Daily Temperatures', 'difficulty': 'Medium', 'topic': 'Stack'},
            {'number': 853, 'title': 'Car Fleet', 'difficulty': 'Medium', 'topic': 'Stack'},
            {'number': 84, 'title': 'Largest Rectangle in Histogram', 'difficulty': 'Hard', 'topic': 'Stack'},

            # Binary Search
            {'number': 704, 'title': 'Binary Search', 'difficulty': 'Easy', 'topic': 'Binary Search'},
            {'number': 74, 'title': 'Search a 2D Matrix', 'difficulty': 'Medium', 'topic': 'Binary Search'},
            {'number': 875, 'title': 'Koko Eating Bananas', 'difficulty': 'Medium', 'topic': 'Binary Search'},
            {'number': 153, 'title': 'Find Minimum in Rotated Sorted Array', 'difficulty': 'Medium', 'topic': 'Binary Search'},
            {'number': 33, 'title': 'Search in Rotated Sorted Array', 'difficulty': 'Medium', 'topic': 'Binary Search'},
            {'number': 981, 'title': 'Time Based Key-Value Store', 'difficulty': 'Medium', 'topic': 'Binary Search'},
            {'number': 4, 'title': 'Median of Two Sorted Arrays', 'difficulty': 'Hard', 'topic': 'Binary Search'},

            
            # Sliding Window
            {'number': 121, 'title': 'Best Time to Buy and Sell Stock', 'difficulty': 'Easy', 'topic': 'Sliding Window'},
            {'number': 3, 'title': 'Longest Substring Without Repeating Characters', 'difficulty': 'Medium', 'topic': 'Sliding Window'},
            {'number': 424, 'title': 'Longest Repeating Character Replacement', 'difficulty': 'Medium', 'topic': 'Sliding Window'},
            {'number': 567, 'title': 'Permutation in String', 'difficulty': 'Medium', 'topic': 'Sliding Window'},
            {'number': 76, 'title': 'Minimum Window Substring', 'difficulty': 'Hard', 'topic': 'Sliding Window'},
            {'number': 239, 'title': 'Sliding Window Maximum', 'difficulty': 'Hard', 'topic': 'Sliding Window'},
                        
            # Linked List
            {'number': 206, 'title': 'Reverse Linked List', 'difficulty': 'Easy', 'topic': 'Linked List'},
            {'number': 21, 'title': 'Merge Two Sorted Lists', 'difficulty': 'Easy', 'topic': 'Linked List'},
            {'number': 141, 'title': 'Linked List Cycle', 'difficulty': 'Easy', 'topic': 'Linked List'},
            {'number': 143, 'title': 'Reorder List', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 19, 'title': 'Remove Nth Node From End of List', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 138, 'title': 'Copy List with Random Pointer', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 2, 'title': 'Add Two Numbers', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 287, 'title': 'Find the Duplicate Number', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 146, 'title': 'LRU Cache', 'difficulty': 'Medium', 'topic': 'Linked List'},
            {'number': 23, 'title': 'Merge k Sorted Lists', 'difficulty': 'Hard', 'topic': 'Linked List'},
            {'number': 25, 'title': 'Reverse Nodes in k-Group', 'difficulty': 'Hard', 'topic': 'Linked List'},

            # Math & Geometry
            {'number': 202, 'title': 'Happy Number', 'difficulty': 'Easy', 'topic': 'Math & Geometry'},
            {'number': 66, 'title': 'Plus One', 'difficulty': 'Easy', 'topic': 'Math & Geometry'},
            {'number': 50, 'title': 'Pow(x, n)', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            {'number': 43, 'title': 'Multiply Strings', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            {'number': 2013, 'title': 'Detect Squares', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            {'number': 48, 'title': 'Rotate Image', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            {'number': 54, 'title': 'Spiral Matrix', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            {'number': 73, 'title': 'Set Matrix Zeroes', 'difficulty': 'Medium', 'topic': 'Math & Geometry'},
            
            # Bit Manipulation
            {'number': 136, 'title': 'Single Number', 'difficulty': 'Easy', 'topic': 'Bit Manipulation'},
            {'number': 191, 'title': 'Number of 1 Bits', 'difficulty': 'Easy', 'topic': 'Bit Manipulation'},
            {'number': 338, 'title': 'Counting Bits', 'difficulty': 'Easy', 'topic': 'Bit Manipulation'},
            {'number': 190, 'title': 'Reverse Bits', 'difficulty': 'Easy', 'topic': 'Bit Manipulation'},
            {'number': 268, 'title': 'Missing Number', 'difficulty': 'Easy', 'topic': 'Bit Manipulation'},
            {'number': 371, 'title': 'Sum of Two Integers', 'difficulty': 'Medium', 'topic': 'Bit Manipulation'},
            {'number': 7, 'title': 'Reverse Integer', 'difficulty': 'Medium', 'topic': 'Bit Manipulation'},
            
            # Trees
            {'number': 226, 'title': 'Invert Binary Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 104, 'title': 'Maximum Depth of Binary Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 543, 'title': 'Diameter of Binary Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 110, 'title': 'Balanced Binary Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 100, 'title': 'Same Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 572, 'title': 'Subtree of Another Tree', 'difficulty': 'Easy', 'topic': 'Trees'},
            {'number': 235, 'title': 'Lowest Common Ancestor of a Binary Search Tree', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 102, 'title': 'Binary Tree Level Order Traversal', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 199, 'title': 'Binary Tree Right Side View', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 1448, 'title': 'Count Good Nodes in Binary Tree', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 98, 'title': 'Validate Binary Search Tree', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 230, 'title': 'Kth Smallest Element in a BST', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 105, 'title': 'Construct Binary Tree from Preorder and Inorder Traversal', 'difficulty': 'Medium', 'topic': 'Trees'},
            {'number': 124, 'title': 'Binary Tree Maximum Path Sum', 'difficulty': 'Hard', 'topic': 'Trees'},
            {'number': 297, 'title': 'Serialize and Deserialize Binary Tree', 'difficulty': 'Hard', 'topic': 'Trees'},
            
            # Tries
            {'number': 208, 'title': 'Implement Trie', 'difficulty': 'Medium', 'topic': 'Tries'},
            {'number': 211, 'title': 'Design Add and Search Words Data Structure', 'difficulty': 'Medium', 'topic': 'Tries'},
            {'number': 212, 'title': 'Word Search II', 'difficulty': 'Hard', 'topic': 'Tries'},
                        
            # Backtracking
            {'number': 78, 'title': 'Subsets', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 39, 'title': 'Combination Sum', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 46, 'title': 'Permutations', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 90, 'title': 'Subsets II', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 40, 'title': 'Combination Sum II', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 79, 'title': 'Word Search', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 131, 'title': 'Palindrome Partitioning', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 17, 'title': 'Letter Combinations of a Phone Number', 'difficulty': 'Medium', 'topic': 'Backtracking'},
            {'number': 51, 'title': 'N-Queens', 'difficulty': 'Hard', 'topic': 'Backtracking'},
            
            # Heap / Priority Queue
            {'number': 703, 'title': 'Kth Largest Element in a Stream', 'difficulty': 'Easy', 'topic': 'Heap / Priority Queue'},
            {'number': 1046, 'title': 'Last Stone Weight', 'difficulty': 'Easy', 'topic': 'Heap / Priority Queue'},
            {'number': 973, 'title': 'K Closest Points to Origin', 'difficulty': 'Medium', 'topic': 'Heap / Priority Queue'},
            {'number': 215, 'title': 'Kth Largest Element in an Array', 'difficulty': 'Medium', 'topic': 'Heap / Priority Queue'},
            {'number': 621, 'title': 'Task Scheduler', 'difficulty': 'Medium', 'topic': 'Heap / Priority Queue'},
            {'number': 355, 'title': 'Design Twitter', 'difficulty': 'Medium', 'topic': 'Heap / Priority Queue'},
            {'number': 295, 'title': 'Find Median from Data Stream', 'difficulty': 'Hard', 'topic': 'Heap / Priority Queue'},

            # Graphs
            {'number': 200, 'title': 'Number of Islands', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 133, 'title': 'Clone Graph', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 695, 'title': 'Max Area of Island', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 417, 'title': 'Pacific Atlantic Water Flow', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 130, 'title': 'Surrounded Regions', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 994, 'title': 'Rotting Oranges', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 207, 'title': 'Course Schedule', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 210, 'title': 'Course Schedule II', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 684, 'title': 'Redundant Connection', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 286, 'title': 'Walls and Gates', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 261, 'title': 'Graph Valid Tree', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 323, 'title': 'Number of Connected Components in an Undirected Graph', 'difficulty': 'Medium', 'topic': 'Graphs'},            
            {'number': 127, 'title': 'Word Ladder', 'difficulty': 'Hard', 'topic': 'Graphs'},
                        
            # 1-D Dynamic Programming
            {'number': 70, 'title': 'Climbing Stairs', 'difficulty': 'Easy', 'topic': 'Dynamic Programming'},
            {'number': 746, 'title': 'Min Cost Climbing Stairs', 'difficulty': 'Easy', 'topic': 'Dynamic Programming'},
            {'number': 198, 'title': 'House Robber', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 213, 'title': 'House Robber II', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 5, 'title': 'Longest Palindromic Substring', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 647, 'title': 'Palindromic Substrings', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 91, 'title': 'Decode Ways', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 322, 'title': 'Coin Change', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 152, 'title': 'Maximum Product Subarray', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 139, 'title': 'Word Break', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 300, 'title': 'Longest Increasing Subsequence', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 416, 'title': 'Partition Equal Subset Sum', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            
            # Advanced Graphs
            {'number': 743, 'title': 'Network Delay Time', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 1584, 'title': 'Min Cost to Connect All Points', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 787, 'title': 'Cheapest Flights Within K Stops', 'difficulty': 'Medium', 'topic': 'Graphs'},
            {'number': 332, 'title': 'Reconstruct Itinerary', 'difficulty': 'Hard', 'topic' : 'Graphs'},
            {'number': 778, 'title': 'Swim in Rising Water', 'difficulty': 'Hard', 'topic': 'Graphs'},
            {'number': 269, 'title': 'Alien Dictionary', 'difficulty': 'Hard', 'topic': 'Graphs'},

            # Intervals
            {'number': 252, 'title': 'Meeting Rooms', 'difficulty': 'Easy', 'topic': 'Intervals'},
            {'number': 57, 'title': 'Insert Interval', 'difficulty': 'Medium', 'topic': 'Intervals'},
            {'number': 56, 'title': 'Merge Intervals', 'difficulty': 'Medium', 'topic': 'Intervals'},
            {'number': 435, 'title': 'Non-overlapping Intervals', 'difficulty': 'Medium', 'topic': 'Intervals'},
            {'number': 253, 'title': 'Meeting Rooms II', 'difficulty': 'Medium', 'topic': 'Intervals'},
            {'number': 1851, 'title': 'Minimum Interval to Include Each Query', 'difficulty': 'Hard', 'topic': 'Intervals'},

            # Greedy
            {'number': 53, 'title': 'Maximum Subarray', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 55, 'title': 'Jump Game', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 45, 'title': 'Jump Game II', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 134, 'title': 'Gas Station', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 846, 'title': 'Hand of Straights', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 1899, 'title': 'Merge Triplets to Form Target Triplet', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 763, 'title': 'Partition Labels', 'difficulty': 'Medium', 'topic': 'Greedy'},
            {'number': 678, 'title': 'Valid Parenthesis String', 'difficulty': 'Medium', 'topic': 'Greedy'},

            # 2-D Dynamic Programming
            {'number': 62, 'title': 'Unique Paths', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 1143, 'title': 'Longest Common Subsequence', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 309, 'title': 'Best Time to Buy and Sell Stock with Cooldown', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 518, 'title': 'Coin Change II', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 494, 'title': 'Target Sum', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 97, 'title': 'Interleaving String', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 72, 'title': 'Edit Distance', 'difficulty': 'Medium', 'topic': 'Dynamic Programming'},
            {'number': 329, 'title': 'Longest Increasing Path in a Matrix', 'difficulty': 'Hard', 'topic': 'Dynamic Programming'},
            {'number': 115, 'title': 'Distinct Subsequences', 'difficulty': 'Hard', 'topic': 'Dynamic Programming'},
            {'number': 312, 'title': 'Burst Balloons', 'difficulty': 'Hard', 'topic': 'Dynamic Programming'},
            {'number': 10, 'title': 'Regular Expression Matching', 'difficulty': 'Hard', 'topic': 'Dynamic Programming'}
        ]

        Problem.objects.all().delete()
        
        created_count = 0
        for problem_data in problems_data:
            problem_data['leetcode_url'] = self.title_to_url(problem_data['title'])
            problem, created = Problem.objects.get_or_create(
                number=problem_data['number'],
                defaults=problem_data
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created: {problem.number}. {problem.title}')
            else:
                self.stdout.write(f'Already exists: {problem.number}. {problem.title}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded {created_count} problems. Total problems in database: {Problem.objects.count()}'
            )
        )
