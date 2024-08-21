def dijkstra(graph, start):
  # 최단 거리 테이블을 무한대로 초기화
  distances = {node: float('inf') for node in graph}
  distances[start] = 0  # 시작 노드의 거리는 0

  visited = []  # 방문한 노드를 기록
  nodes = list(graph.keys())  # 모든 노드 리스트

  while nodes:
      # 방문하지 않은 노드 중에서 최단 거리 노드 선택
      min_node = None
      for node in nodes:
          if node not in visited:
              if min_node is None:
                  min_node = node
              elif distances[node] < distances[min_node]:
                  min_node = node

      if min_node is None:
          break

      # 현재 노드의 이웃 노드들에 대해 거리 계산 및 갱신
      for neighbor, cost in graph[min_node].items():
          new_distance = distances[min_node] + cost
          if new_distance < distances[neighbor]:
              distances[neighbor] = new_distance

      # 현재 노드를 방문한 것으로 표시하고 리스트에서 제거
      visited.append(min_node)
      nodes.remove(min_node)

  return distances

# 그래프 표현 (딕셔너리)
graph = {
  'A': {'B': 5, 'C': 1},
  'B': {'A': 5, 'C': 2, 'D': 1},
  'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
  'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
  'E': {'C': 8, 'D': 3},
  'F': {'D': 6}
}

# 시작 노드 설정
start_node = 'A'
distances = dijkstra(graph, start_node)

# 결과 출력
for node, distance in distances.items():
  print(f"최단 거리: {start_node} -> {node} = {distance}")
