from heapq import heappush, heappop
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f


class MuseumEvacuation:
    def __init__(self):
        self.layout = [
            ['0', '0', '1', '0', 'E'],
            ['0', '1', '0', '1', '0'],
            ['P', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def find_person_and_exits(self) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
        """Find person's position and all emergency exits"""
        person = None
        exits = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == 'P':
                    person = (i, j)
                elif self.layout[i][j] == 'E':
                    exits.append((i, j))
        return person, exits

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two points"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        neighbors = []
        row, col = position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.layout[new_row][new_col] != '1':
                neighbors.append((new_row, new_col))
        return neighbors

    def find_evacuation_path(self) -> Optional[List[Tuple[int, int]]]:
        """Find shortest path to nearest emergency exit"""
        person, exits = self.find_person_and_exits()
        if not person or not exits:
            return None # No person or exits found

        open_list = []
        heappush(open_list, Node(person))
        closed_set = set()

        while open_list:
            current_node = heappop(open_list)
            closed_set.add(current_node.position)

            # Check if we reached an exit
            if current_node.position in exits:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]  # Reverse the path to get start-to-end order

            for neighbor in self.get_neighbors(current_node.position):
                if neighbor in closed_set:
                    continue

                g_cost = current_node.g + 1
                h_cost = min(self.manhattan_distance(neighbor, exit_pos) for exit_pos in exits)
                f_cost = g_cost + h_cost

                neighbor_node = Node(neighbor, current_node)
                neighbor_node.g = g_cost
                neighbor_node.h = h_cost
                neighbor_node.f = f_cost

                # Avoid duplicates in the open list
                if all(neighbor != node.position for node in open_list):
                    heappush(open_list, neighbor_node)

        return None  # No path found

    def display_path(self, path: List[Tuple[int, int]]):
        """Display the evacuation path on the museum layout"""
        if not path:
            print("No path found.")
            return
        for i, j in path:
            if self.layout[i][j] == '0':
                self.layout[i][j] = '*'
        for row in self.layout:
            print(' '.join(row))

    def visualize(self, path: List[Tuple[int, int]] = None):
        """
        Visualize the museum layout with matplotlib.
        If path is provided, it will be shown in green.
        """
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.cm.colors.ListedColormap(['#FFFFFF', '#404040', '#FF4444', '#4444FF', '#FFCC00'])

        numeric_layout = np.zeros((self.rows, self.cols))
        text_annotations = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == '1':
                    numeric_layout[i][j] = 1
                elif self.layout[i][j] == 'E':
                    numeric_layout[i][j] = 2
                    text_annotations.append((i, j, 'EXIT'))
                elif self.layout[i][j] == 'P':
                    numeric_layout[i][j] = 3
                    text_annotations.append((i, j, 'P'))

        if path:
            for row, col in path[1:-1]:
                numeric_layout[row][col] = 4

        im = ax.imshow(numeric_layout, cmap=cmap)
        for i in range(self.rows + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(self.cols + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)

        for i, j, text in text_annotations:
            ax.text(j, i, text, ha='center', va='center', color='white', fontweight='bold', fontsize=10)

        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()


if __name__ == "__main__":
    evacuation = MuseumEvacuation()
    path = evacuation.find_evacuation_path()
    if path:
        evacuation.display_path(path)
        evacuation.visualize(path)
    else:
        print("No evacuation path found.")
