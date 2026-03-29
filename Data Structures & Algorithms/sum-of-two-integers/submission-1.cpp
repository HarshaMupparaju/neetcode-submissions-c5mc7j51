class Solution {
public:
    int getSum(int a, int b) {
        int and_shifted = (a & b) << 1;
        int exclusive_or = a ^ b;

        int temp;

        while((and_shifted & exclusive_or) != 0) {
            temp = and_shifted;
            and_shifted = (and_shifted & exclusive_or) << 1;
            exclusive_or = temp ^ exclusive_or;
        }

        return and_shifted | exclusive_or;
    }
};

// class Solution:
//     def getSum(self, a: int, b: int) -> int:
        
//         and_shifted = (a & b) << 1
//         xor = a ^ b
        
//         while((and_shifted & xor) != 0):
//             temp = and_shifted
//             and_shifted = (and_shifted & xor) << 1
//             xor = temp ^ xor
        
//         res = and_shifted | xor
//         return res