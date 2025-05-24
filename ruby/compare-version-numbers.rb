def split_string(version)
  version.split('.').map(&:to_i)
end

def compare_version(version1, version2)
  list1 = split_string(version1)
  list2 = split_string(version2)

  max_len = [list1.length, list2.length].max
  list1 += [0] * (max_len - list1.length)
  list2 += [0] * (max_len - list2.length)

  for i in 0...max_len do
    if list1[i] > list2[i]
      return 1
    elsif list1[i] < list2[i]
      return -1
    elsif list1[i] == list2[i] && i == max_len - 1
      return 0
    end
  end
end
