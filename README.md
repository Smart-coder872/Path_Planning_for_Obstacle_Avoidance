# Path Planning for Obstacle Aviodance

## Milestone 1
### Goals

- Setup inital files and structure and ensure there are no stuck points

- Start with 2-3 algorithms to plan to compare and implement at least one of them

- Implement at least one of the algorithms

### Progress
I have completed most of the setup but am I bit behind where I want to be. However, I do still feel good about my progress. I found the path planning source on the course website, https://github.com/comprobo25/recitation_examples/tree/main/path_planning, to be helpful as a starting point for implementing the path planning algorithms. From literature, I had investaged Dijkstra’s, A Star, D Star, D Star Lite, LPA Star, RRT Star, HIPP, and C Star (using star instead of the asteriks symbol for markdown). In terms of choosing algorithms to focus on, I decided on D Star Lite, RRT Star, and C Star. The decision for D Star Lite was based on the fact that some of these algorithms are designed as modified, more efficient versions of older, more established algorithms. For example, the derivation for D Star Lite and LPA Star is Dijkstra’s → A Star → D Star → D Star Lite and LPA Star. The main difference between D Star Lite and LPA Star is that D Star Lite, like most of these algorithms, searches from the end point while LPA Star searches from the start point. To build a foundational place to start from and requiring less lines of codce, I decided to start with implementing D Star lite as one of the inital algorithms. Additionally, I chose RRT Star and C Star over HIPP for now since these are more established and have more information available. However, I might revisit HIPP later.

#### Repo and Package Setup
- (**Completed**) Create repo and remote add
- (**Completed**) Setup and build package called planning and control
- (**Completed**) Add .gitignore
- (**Completed**) Create a planning node and a control node and add to setup.py

- (**In Progress**) Add dependencies: I feel pretty comfortable adding dependencies to the package but am not sure how to add to regular python files. Would this just be a -r requirements.txt file?

- (**Not started**) Fill out the package description and licence to-dos in setup.py: I deprioritized this to focus on the areas of the project that could potentially have stuck points
- (**Not started**) Setup publishing and subscription between nodes: I deprioritized this since I feel relatively familar with this process and to focus on implementing and testing the algorithms

#### Algorithm Setup:
- (**Completed**) Decide on 2-3 algorithms as a starting place
- (**Completed**) Setup planning algorithms folder and create a file for each of the algorithms

- (**In progress**) Conduct literature research
- (**In progress**) Write psuedocode for one of the algorithms (rrt)

- (**Not Started**) Implement the actual code based on the pseudo code (rrt)
- (**Not Started**) Test code (rrt)

### Risks
- **Implementing C Star**: Because this algorithm is still experimental, it may be more difficult to implement. I plan to prioritize the algorithms in order from most information to least information. 
- **Closed Loop System/Reactive Algorithms** While this is exciting to me, I'm not entirely sure how to go about this. 

### MVP Updates
- To be on the safe side, I have updated my MVP to account for only one of the algorithms.

## Milestone 2

### Goals
- Write psuedocode for dstarlite and cstar

- Wrap up the in progress algorithm setup tasks

### Progress

#### Path Planning Algorithms
- (**TBD**) Write psuedocode for dstarlite
- (**TDB**) Implement actual code for dstarlite and test
- (**TBD**) Write psuedocode for cstar
- (**TBD**) Implement actual code for cstar and test

#### ROS2 
- (**TBD**) Import path planning files
- (**TBD**) Write psuedocode for both ros nodes
- (**TBD**) Write actual code for both nodes
- (**TBD**) Test nodes
