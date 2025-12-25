# Advent of Code 2025 - Level Five Submission

## Progress

**Part One: Complete**
  - Determine how many available ingredient IDs are fresh

**Part Two: In-progress**
  - Find How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges

## Problem Summary

A cafeteria inventory system tracks fresh ingredient ID ranges (inclusive, overlapping allowed). Given a list of fresh ranges and available ingredient IDs, determine which ingredients are fresh.

| Part | Task | Answer |
|------|------|--------|
| One | Count fresh ingredient IDs from available list | 821 |
| Two | Count how many IDs are considered fresh according to the fresh ingredient ID ranges | TBD |

## Key Challenge

- **Range checking**: Check if each ingredient ID falls within any fresh range
- **Overlapping ranges**: Ranges can overlap; an ID is fresh if it's in ANY range
- **Inclusive bounds**: Range `3-5` includes 3, 4, AND 5
- **Efficient lookup**: With many ranges and IDs, need efficient comparison method
