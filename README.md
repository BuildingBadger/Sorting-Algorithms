# Sorting Algorithms

A collection of sorting algorithm implementations designed to support learning, experimentation, and comparison of common approaches to ordering data.

## Overview

Sorting is a fundamental computer science problem. Different algorithms offer different trade-offs in terms of runtime, memory usage, stability, and suitability for particular kinds of input.

This repository provides a place to explore those trade-offs through readable implementations and practical examples.

## Contents

The project files are organised in the `Sorting Algorithms` directory. Each implementation can be studied independently to understand:

- How the algorithm operates
- How data is rearranged during execution
- Its time and space complexity
- Whether it is stable or performed in place
- The types of input for which it is most suitable

## Algorithms

The repository is intended to contain implementations of common sorting techniques, such as:

- Bubble sort
- Selection sort
- Insertion sort
- Merge sort
- Quick sort
- Heap sort
- Counting sort
- Radix sort

> The available algorithms depend on the files currently included in the repository. Add or remove items from this list as the project develops.

## Complexity Summary

| Algorithm | Best Case | Average Case | Worst Case | Extra Space | Stable |
|---|---:|---:|---:|---:|:---:|
| Bubble sort | $$O(n)$$ | $$O(n^2)$$ | $$O(n^2)$$ | $$O(1)$$ | Yes |
| Selection sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n^2)$$ | $$O(1)$$ | No |
| Insertion sort | $$O(n)$$ | $$O(n^2)$$ | $$O(n^2)$$ | $$O(1)$$ | Yes |
| Merge sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n)$$ | Yes |
| Quick sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n^2)$$ | $$O(\log n)$$* | Usually no |
| Heap sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(1)$$ | No |
| Counting sort | $$O(n + k)$$ | $$O(n + k)$$ | $$O(n + k)$$ | $$O(n + k)$$ | Yes** |
| Radix sort | $$O(d(n + k))$$ | $$O(d(n + k))$$ | $$O(d(n + k))$$ | $$O(n + k)$$ | Yes** |

\* Depends on the partition strategy and recursion behaviour.

\*\* Stability depends on the implementation.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/BuildingBadger/Sorting-Algorithms.git
cd Sorting-Algorithms
```

Open the `Sorting Algorithms` directory and follow the instructions provided by the relevant source files or project configuration.

## Using an Algorithm

A typical workflow is:

1. Prepare an unsorted collection of values.
2. Pass the collection to the selected sorting implementation.
3. Compare the result with the expected sorted order.
4. Test the implementation with different input sizes and patterns.

Useful test cases include:

- An empty collection
- A single-element collection
- Already sorted data
- Reverse-sorted data
- Duplicate values
- Negative values, where supported
- Large randomly generated inputs

## Learning Goals

This project can be used to practise:

- Algorithm design and implementation
- Big-O complexity analysis
- Recursion and divide-and-conquer techniques
- In-place versus out-of-place processing
- Stable versus unstable sorting
- Testing and comparing algorithm performance
