class Solution {
public:
    int search(int A[], int n, int target);
    int index_of_first_element_in_group_two(int vector[], int left, int right);
    int binary_search(int vector[], int value, int left, int right);
    int find_index_by_value(int vector[], int value, int left, int right);
};

int Solution::index_of_first_element_in_group_two(int vector[], int left, int right)
{
    if(left == right)
  	  return left;

  	int mid = left + (right - left) / 2;
    if(vector[mid] >= vector[0]) {
      return index_of_first_element_in_group_two(vector, mid + 1, right);
    }
    else {
      return index_of_first_element_in_group_two(vector, left, mid);
    }
}

int Solution::binary_search(int vector[], int value, int left, int right)
{
    if(right < left)
  	  return -1;

  	int mid = left + (right - left) / 2;
	int midpoint_value = vector[mid];

    if(midpoint_value > value) {
      return binary_search(vector, value, left, mid - 1);
    }
    else if(midpoint_value < value) {
      return binary_search(vector, value, mid + 1, right);
    }
    else {
        return mid;
    }
}


int Solution::find_index_by_value(int vector[], int value, int left, int right)
{
    int index = index_of_first_element_in_group_two(vector, left, right);
    if(value >= vector[0]) {
      return binary_search(vector, value, left, index - 1);
 	}
    else {
      return binary_search(vector, value, index, right);
    }
}

int Solution::search(int vector[], int n, int target)
{
    int left = 0, right = n - 1;
    int index = -1;
    if(left <= right) {
        if(vector[0] <= vector[n-1]) {
          index =  binary_search(vector, target, left, right);
        }
        else {
          index =  find_index_by_value(vector, target, left, right);
        }
    }
    return index;
}

