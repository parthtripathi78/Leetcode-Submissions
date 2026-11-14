class Solution {
    public List<Integer> partitionLabels(String s) {

        int[] lastOccurence = new int[26];

        for(int i = 0; i < s.length(); i++) {
            lastOccurence[s.charAt(i) - 'a'] = i;
        }

        int partitionStart = 0;
        int partitionEnd = 0;

        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < s.length(); i++) {
            int lastIndex = lastOccurence[s.charAt(i) - 'a'];
            partitionEnd = Math.max(partitionEnd, lastIndex);

            if(i == partitionEnd) {
                result.add(partitionEnd - partitionStart + 1);
                partitionStart = i + 1;
            }
        }

        return result;
    }
}