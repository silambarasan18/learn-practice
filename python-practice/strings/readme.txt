# Problem: Expand Letters Based on Numbers

## Problem Statement
Given an input string in the format `a1b3`, expand it so that each letter is repeated based on the number following it.  
Example:  
- Input: `a1b3`  
- Output: `abbb`

## Approach
1. Loop through the input string.
2. Identify letters and the numbers following them.
3. Repeat the letters based on the number.
4. Combine the repeated letters into the final output.

## Edge Cases
- Empty input string: Return an empty string.
- Invalid format (e.g., `abc`, `a2b`): Handle gracefully.

## Lessons Learned
- String parsing and handling mixed characters.
- Using loops and conditional logic effectively.
