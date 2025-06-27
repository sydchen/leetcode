class TopVotedCandidate
=begin
    :type persons: Integer[]
    :type times: Integer[]
=end
    def initialize(persons, times)
        @times   = times
        @leaders = Array.new(persons.size)
        counts   = Hash.new(0)
        current_leader = nil
        max_votes      = 0

        persons.each_with_index do |p, i|
        counts[p] += 1
        if counts[p] >= max_votes
            max_votes = counts[p]
            current_leader = p
        end
        @leaders[i] = current_leader
        end
    end

=begin
    :type t: Integer
    :rtype: Integer
=end
    def q(t)
        # bsearch_index 找到第一個 times[idx] > t 的位置
        idx = @times.bsearch_index { |time| time > t }
        # 若找到，就往前一格；若找不到（t ≥ 最後時間），就用最後一筆投票
        idx = idx ? idx - 1 : (@times.size - 1)
        # 若 t < 第一次投票時間，idx 會成為 -1，此時回 nil 或拋錯依需求
        return nil if idx < 0
        @leaders[idx]
    end
end

obj = TopVotedCandidate.new([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
[[3],[12],[25],[15],[24],[8]].flatten.each do |t|
  puts "time #{t} => #{obj.q(t)}"
end
