from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        pass

    def get_graph(self) -> GraphInterface:
        super().get_graph()

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass