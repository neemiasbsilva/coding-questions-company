########################################################################
# return a new sorted merged list from k sorted list, each with size N #
########################################################################
import heapq

def merge(lists):

    merged_list = []
    
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        
        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind + 1)
            
            heapq.heappush(heap, next_tuple)

    return merged_list

def main():
    lists = [[2, 3, 1], [50, 32, 123], [33, 45, 50]]
    print("Original list: ", lists)
    print("Merged list: " , merge(lists))

if __name__ == "__main__":
    main()
