#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <math.h>
#include <vector>


int main(){
    int size_of_message{14};
    char char_array[size_of_message];
    std::ifstream data_file{"input.txt"};
    std::string input{""};
    std:getline(data_file, input);
    
    bool marker = false;
    int marker_num{0};
    int duplicate{0};
    for (int i = 0; i < input.size(); i++){
        for(int j = 0; j < size_of_message; j++){
            char_array[j] = input[i+j];
        }
        
        for (int x = 0; x < size_of_message; x++){
            for (int y = 0; y < size_of_message; y++){
                if(char_array[x] == char_array[y]){
                    duplicate++;
                }
            }
        }
        if(duplicate < size_of_message + 1){
            std::cout << "Marker found: " << i + size_of_message << std::endl;
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
