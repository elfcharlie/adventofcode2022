#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <math.h>
#include <vector>


int main(){
    char char_array[4];
    std::ifstream data_file{"input.txt"};
    std::string input{""};
    std:getline(data_file, input);
    
    bool marker = false;
    int marker_num{0};
    int duplicate{0};
    for (int i = 0; i < input.size(); i++){
        char_array[0] = input[i];
        char_array[1] = input[i+1];
        char_array[2] = input[i+2];
        char_array[3] = input[i+3];
        
        for (int x = 0; x < 4; x++){
            for (int y = 0; y < 4; y++){
                if(char_array[x] == char_array[y]){
                    duplicate++;
                }
            }
        }
        if(duplicate < 5){
            std::cout << "Marker found: " << i + 4 << std::endl;
            marker = true;
            std::cout << char_array << std::endl;
            break;
        }
        else {
            duplicate = 0;
        }
        if (marker==true){
            break;
        }
    }
}
