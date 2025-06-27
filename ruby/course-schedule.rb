# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)

  adj = Array.new(num_courses) { [] }
  indegree = Array.new(num_courses, 0)

  prerequisites.each do |u, v|
    adj[v] << u
    indegree[u] += 1
  end

  queue = []
  (0...num_courses).each { |i| queue << i if indegree[i].zero? }

  taken = 0
  while !queue.empty?
    c = queue.shift
    taken += 1

    adj[c].each do |nc|
      indegree[nc] -= 1
      queue << nc if indegree[nc].zero?
    end
  end

  taken == num_courses
end

p can_finish(2, [[1,0]]) # true
p can_finish(2, [[1,0],[0,1]]) # false
