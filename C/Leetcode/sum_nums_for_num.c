#include <stdio.h>
#include <stdlib.h>

struct Solution {
    int* (*twoSum)(struct Solution*, int*, int, int, int*);
};

int* twoSum(struct Solution* this, int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

int main() {
    struct Solution solution;
    solution.twoSum = twoSum;

    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;

    int* result = solution.twoSum(&solution, nums, sizeof(nums)/sizeof(nums[0]), target, &returnSize);

    if (result != NULL) {
        printf("Indices: [%d, %d]\n", result[0], result[1]);
        free(result); // Don't forget to free the allocated memory
    } else {
        printf("No solution found.\n");
    }

    return 0;
}
