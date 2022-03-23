class Graph:
    def __init__(self, node_num):
        self.graph = [False] * node_num
        self.wei = [None] * node_num
        for i in range(node_num):
            self.graph[i] = [False] * node_num
            self.wei[i] = [None] * node_num
    
    def insert(self, v, u, weight, is_indirect):
        if is_indirect:
            # v → u and u → v
            self.graph[v][u] = True
            self.graph[u][v] = True
            self.wei[v][u] = weight
            self.wei[u][v] = weight
        else:
            # v → u
            self.graph[v][u] = True
            self.wei[v][u] = weight
    
    def print_graph(self):
        print("--- 현재 그래프 배열 ---")
        for idx in range(len(self.graph)):
            print(self.graph[idx])
        print("--- 현재 그래프 가중치 ---")
        for idx in range(len(self.wei)):
            print(self.wei[idx])
# 노드 수 입력
node_num = int(input("노드 수를 입력하세요: "))
# 초기 그래프 생성
graph = Graph(node_num)
graph.insert(0,1,1,1)
graph.insert(0,3,1,1)
graph.insert(1,2,1,1)
graph.insert(1,3,1,1)
graph.insert(2,3,1,1)
graph.print_graph()