def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list)//2
        left_half = unsorted_list[:mid]
        right_half = unsorted_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i += 1
            else:
                unsorted_list[k] = right_half[j]
                j += 1
            k +=1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i+=1
            k+=1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j+=1
            k+=1

unsorted_list = [1, 98, 36, 48, 29, 4, 2]
merge_sort(unsorted_list=unsorted_list)
print(unsorted_list)