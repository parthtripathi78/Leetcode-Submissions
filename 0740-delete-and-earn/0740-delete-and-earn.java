
class Solution {
    int[] t = new int[20001];
    int solve(int[] arr, int i) {
        if (i >= arr.length) {
            return 0;
        }
        if (t[i] != -1) {
            return t[i];
        }
        int currValue = arr[i];
        int currSum = arr[i];
        int index = i + 1;
        while (index < arr.length && arr[index] == currValue) {
            currSum += arr[i];
            index++;
        }
        while (index < arr.length && arr[index] == currValue + 1) {
            index++;
        }
        
        return t[i] = Math.max(
            currSum + solve(arr, index),
            solve(arr, i + 1)
        );
    }
    public int deleteAndEarn(int[] arr) {
        int n = arr.length;
        Arrays.fill(t, -1);

        Arrays.sort(arr);

        return solve(arr, 0);
    }
}