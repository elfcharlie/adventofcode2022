#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <math.h>
#include <vector>


int main(){
    char dummy_char;
    std::ifstream data_file{"input.txt"};
    int total_overlap{0};
    int bound[] = {0, 0 ,0, 0};

    while(data_file >> bound[0]) {
        
        data_file >> bound[1];
        data_file >> dummy_char;
        data_file >> bound[2];
        data_file >> bound[3];
        if ((bound[0] >= bound[2]) && (abs(bound[1]) <= abs(bound[3]))) {
                for (int num : bound){
                std::cout << num <<" ";
            }
            total_overlap++;

            std::cout <<  " Right overlap left" << std::endl;
        }
        else if ((bound[0] <= bound[2]) && (abs(bound[1]) >= abs(bound[3]))) {
            for (int num : bound){
                std::cout << num <<" ";
            }
            std::cout << " Left overlap right" << std::endl;
            total_overlap++;
        }
        else if ((bound[0] >= bound[2]) && (bound[0] <= abs(bound[3]))) {
                for (int num : bound){
                std::cout << num <<" ";
            }
            total_overlap++;

            std::cout <<  " Right partly overlap left" << std::endl;
        }
        else if ((bound[2] >= bound[0]) && (bound[2] <= abs(bound[1]))) {
            for (int num : bound){
                std::cout << num <<" ";
            }
            std::cout << " Left partly overlap right" << std::endl;
            total_overlap++;
        }
        
    }
    std::cout << "Total Overlap: " << total_overlap << std::endl;
}