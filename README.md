# UBC Pathfinder

## Authors
**Not Displayed for privacy reasons** 

## Table of Contents
- [Introduction](#introduction)
- [Problems](#problems)
  - [Shortest Path Between Two Classes](#shortest-path-between-two-classes)
  - [Best Dining Option Between Two Classes](#best-dining-option-between-two-classes)
  - [Median Shortest Path](#median-shortest-path)
- [Methodology](#methodology)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction
The University of British Columbia (UBC) Vancouver campus spans over 400 acres, making efficient navigation a significant challenge. Students frequently travel between buildings, requiring optimal routing strategies to minimize travel time.  

Our group applies **linear programming** to solve pathfinding problems at UBC. We implement a **graph-based model** where buildings are represented as **nodes**, and roads are **edges** weighted by distance.  

Additionally, we address various sub-problems such as **finding the best dining hall** that minimizes the travel distance between two classes.

---

## Problems

### Shortest Path Between Two Classes
A **flow network** is a directed graph consisting of nodes and edges, each with a capacity and flow. While network flow problems are often solved using combinatorial methods, they can also be formulated as **linear programming (LP) problems**.  

#### Variables:
- **$N$**: Set of all buildings, road intersections, and endpoints (nodes)
- **$E$**: Set of all edges between nodes
- **$b_k$**: Flow generated by node $k$
  - **$b_o = 1$** (origin node)
  - **$b_d = -1$** (destination node)
  - **$b_k = 0$** (otherwise)
- **$d_ij$**: Distance between nodes $i$ and $j$ (edge weight)
- **$x_ij$**: Flow variable
  - **$1$** if edge **$(i,j)$** is part of the shortest path
  - **$0$** otherwise
- **$u_ij = 1$**: Capacity constraint

#### Linear Programming Formulation:
Minimize:
```math
\sum_{i \in N} \sum_{j \in N} d_{ij} x_{ij}
```

Subject to:
```math
\sum_{i \in N} x_{oi} - \sum_{j \in N} x_{jo} = b_0, \quad \forall i,j \in N
```

```math
\sum_{i \in N} x_{di} - \sum_{j \in N} x_{jd} = b_d, \quad \forall i,j \in N
```

```math
\sum_{i \in N} x_{ki} - \sum_{j \in N} x_{jk} = b_k, \quad \forall i,j,k \in N
```

```math
0 \leq x_{ij} \leq u_{ij}, \quad d_{ij} > 0, \quad x_{ij} \in \{0,1\}
```

The objective function minimizes total distance, and constraints ensure flow conservation across nodes.

---

### Best Dining Option Between Two Classes
This problem can be solved using two methods:
1. **Shortest Path Method**
2. **Utility Score Method**

#### Additional Variables:
- **$R$**: Set of all dining halls
- **$r_i$**: Binary variable for dining hall selection

The LP problem formulation follows the shortest path problem, ensuring exactly **$one$** dining hall is included in the path.

For **utility-based selection**, we introduce:
- **$u_r$**: Utility score for restaurant $r$
- **$y_r$**: Binary variable ($1$ if restaurant $r$ is chosen)

The objective function optimizes:
```math
\min \sum_{i,j \in E} d_{ij} x_{ij} - \sum_{r \in R} u_r y_r
```

---

### Median Shortest Path
The **Median Shortest Path Problem (MSPP)** determines an optimal meeting point minimizing the total travel distance for multiple individuals.  

#### Variables:
- **$x^s_ij$**: Binary variable for student $s$ traveling along edge $(i,j)$
- **$m_k$**: Binary variable indicating if node $k$ is the meeting point

Objective:
```math
\min \sum_{s \in S} \sum_{(i,j)\in E} d_{ij} x^s_{ij}
```

Subject to:
```math
\sum_{j \in N} x^s_{ij} - \sum_{j \in N} x^s_{ji} = \begin{cases}
1, & i=s\\
-1, & i=m\\
0, & \text{otherwise}
\end{cases}
```

```math
\sum_{k \in N} m_k = 1
```

```math
x^s_{ij} \in \{0,1\}, \quad m_k \in \{0,1\}
```

This ensures each student follows an optimal route to the common meeting point.

---

## Methodology
All code can be found in our [GitHub Repository](https://github.com/MisShenanigans/UBC-Pathfinder).  

To construct the UBC **graph model**, we used data from the [UBC Geospatial Open Data](https://github.com/UBCGeodata/ubc-geospatial-opendata). Key datasets include:
- **Roads Dataset** (`ubcv_roads_simple.geojson`)
- **Buildings Dataset** (`ubcv_buildings_simple.csv`)
- **Points of Interest Dataset** (`ubcv_poi.csv`)
- **Building Entrances Dataset** (`ubcv_building_entrances.geojson`)

Nodes and edges were structured to ensure a **connected network**, allowing continuous paths.

---

## Results

### Shortest Path Between Classes
Example: **Crescent West (CRSW) to Leonard S. Klinck (LSK)**
- **Computed Distance**: **2594.02 meters**
- **Google Maps Distance**: **2700 meters**

![Shortest Path](shortest_path_results.png)

![Shortest Path](google_maths_shortest_path.png)

### Best Dining Option
Example: **Student Recreation Centre (SRC) to LSK**
- **Optimal Dining Hall**: **Orchard Commons**
- **Computed Distance**: **620.83 meters**

### Median Shortest Path
Using **Dijkstra’s Algorithm**, we determined an optimal **meeting point** that minimizes total travel costs.

---

## Discussion

### Shortest Path Problem
- Our computed shortest paths were often **shorter** than Google Maps’ suggestions.
- However, **real-time factors** (construction, road conditions) are not accounted for.

### Best Dining Option
- The **shortest path method** does not consider previously traveled paths.
- The **utility-based method** provides a **more flexible** solution.

### Median Shortest Path
- Our **heuristic approach** (Dijkstra’s Algorithm) returned **reasonable results**.
- The **LP formulation** faced **infeasibility issues**, requiring further refinement.

---

## Conclusion
This project successfully applied **linear programming** to **pathfinding problems** at UBC. We implemented models for:
1. **Shortest paths** between classes
2. **Optimal dining hall selection**
3. **Median shortest path meeting point**

Future improvements could include:
- **Incorporating real-time data** (traffic, walking conditions)
- **Improving computational efficiency** in large-scale networks

---

## References
1. Palifka, B. (2024). [Google Maps Shortest Route](https://www.linkedin.com/pulse/ever-wondered-how-google-maps-finds-shortest-route-secret-palifka-ih8ee/)
2. UBC Geospatial Open Data. [GitHub Repository](https://github.com/UBCGeodata/ubc-geospatial-opendata)
3. B. Roy and K. Mason. (draft) formulation and analysis of linear programs, September 2005. Accessed: Feb 10, 2025.
