# UBC PATHFINDER

Docunmentation in Latex: https://www.overleaf.com/project/6797ddf38935c4c858bb556c

## Authors
Autumn Cheung, JJ Kim, Ege Gures, Oliver Shen  
B.Sc. The University of British Columbia  

## Course Information
MATH441_V 201 2024W2  
Dr. Patrick Walls  

Faculty of Science  
Department of Mathematics  

**Date:** February 10, 2025  

## Abstract
hello  

## Table of Contents
- [Introduction](#introduction)
- [Problems](#problems)
  - [Shortest Path Between Two Classes](#shortest-path-between-two-classes)
  - [Best Dining Option Between Two Classes](#best-dining-option-between-two-classes)
  - [Median Shortest Path](#median-shortest-path)
- [Methodology](#methodology)
- [Results](#results)
- [Discussion](#discussion)
- [References](#references)

## Introduction
The UBC Vancouver campus covers over 400 acres of land. Our group aims to use linear programming to optimize the path between classes. Subsequently, we want to find the best dining hall on campus that minimizes the distance from the first class to the dining hall and from the dining hall to the second class.

## Problems

### Shortest Path Between Two Classes
By definition, a flow network is a directed graph that consists of nodes and edges, each of which has a capacity and receives a flow. Although network flow problems are typically associated with combinatorial linear programming, they can also be formulated as linear programming problems.

#### Variables:
- **N**: The set of all buildings, road intersections, and endpoints (nodes of the graph).
- **E**: The set of all edges from node $i$ to $j$.
- **Flow generation:**

 $$ 
  b_k = 
  \begin{cases} 
  b_o=1, & \text{if origin node} \\
  b_d=-1, & \text{if destination node} \\
  b_k=0, & \text{otherwise}
  \end{cases} 
  $$

- **$d_{i,j}$**: Distance between nodes $i$ and $j$ (edge weight).
- **$x_{i,j}$**: Flow from node $i$ to $j$:

 $$ 
  x_{i,j} = 
  \begin{cases} 
  1, & \text{if edge } (i, j) \text{ is part of the shortest path} \\
  0, & \text{otherwise}
  \end{cases} 
  $$

- **$u_{i,j} = 1$**: Capacity constraint from node $i$ to $j$.

#### Linear Programming Formulation:
```math
\text{minimize} \sum_{i\in N}\sum_{j\in N}d_{ij}x_{ij}
```
```math
\text{subject to}
```
```math
\sum_{i \in N}x_{oi} - \sum_{j\in N}x_{jo} = b_0  \\
\sum_{i \in N}x_{di} - \sum_{j\in N}x_{jd} = b_d  \\
\sum_{i \in N}x_{ki} - \sum_{j\in N}x_{jk} = b_k  \\
0 \leq x_{ij} \leq u_{ij}  \\
d_{ij} > 0  \\
x_{ij} \in {0,1}  
```

### Best Dining Option Between Two Classes
This problem incorporates **multi-objective optimization** by balancing **travel distance** with **dining satisfaction**.

#### Objective Functions:
- **Minimize travel distance:**
  ```math
  \min \sum_{i,j \in E} d_{ij}x_{ij}
  ```
- **Maximize utility:**
  ```math
  \max \sum_{r \in R} u_r y_r
  ```

#### Constraints:
- Flow balance:
  ```math
  \sum_{j \in N} x_{ij} - \sum_{j \in N} x_{ji} = \begin{cases}
  1, & \text{if } i=A\\
  -1, & \text{if } i=B\\
  0, & \text{otherwise}
  \end{cases}
  ```
- Exactly **one** restaurant must be chosen:
  ```math
  \sum_{r\in R} y_r =1
  ```

The final **multi-objective function** is rewritten as:
```math
\min \sum_{(ij)\in E}d_{ij}x_{ij} - (1-\lambda)\sum_{r \in R} y_r
```

### Median Shortest Path
The **median shortest path problem (MSPP)** determines an optimal meeting point minimizing total distance traveled by multiple people.

#### Objective Function:
```math
\min \sum_{s \in S} \sum_{(i,j)\in E} d_{ij} x^s_{ij}
```

#### Constraints:
- Flow balance equation:
  ```math
  \sum_{j \in N} x^s_{ij} - \sum_{j \in N} x^s_{ji} = \begin{cases}
  1, & \text{if } i=s\\
  -1, & \text{if } i=m\\
  0, & \text{otherwise}
  \end{cases}
  ```
- One meeting node is chosen:
  ```math
  \sum_{k \in N} m_k =1
  ```

## Methodology
UBC's network graph was created using the **UBC Geospatial Open Data** repository:  
[UBC Geospatial Open Data](https://github.com/UBCGeodata/ubc-geospatial-opendata)

1. **Road Network Data:** `ubcv_routes.geojson` defines all UBC roads.
2. **Building Data:** `ubcv_buildings_simple.csv` and `ubcv_poi.csv` list building details and locations.
3. **Graph Construction:**
   - Buildings connect to **3 nearest roads**.
   - Roads are linked to **form continuous paths**.
   - Roads also connect to **3 nearest roads or buildings** to ensure connectivity.

## Results
(*To be added*)

## Discussion
(*To be added*)

## References
- Mason, A., & Roy, A. (Year). *Title of Reference Book or Paper.*  
- UBC Geospatial Data: [GitHub Repository](https://github.com/UBCGeodata/ubc-geospatial-opendata)

