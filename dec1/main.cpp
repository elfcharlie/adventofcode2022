#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <math.h>
#include <vector>

int find_max_calories(std::vector<int> tot_calories);

int main(){
    std::ifstream data_file{"input.txt"};
    std::string current_line{""};
    int current_line_int;
    std::vector<int> num_elves;
    int elves_count = 0;
    std::vector<int> tot_calories;
    int sum;
    int top_three_elves = 0;

    while(std::getline(data_file, current_line)){
        if(current_line == ""){
            tot_calories.push_back(sum);
            elves_count++;
            num_elves.push_back(elves_count);
            sum = 0;
            continue;
        }
        current_line_int = std::stoi(current_line);
        sum += current_line_int;
    }
    std::sort(tot_calories.begin(), tot_calories.end(), std::greater<int>());
    for(int i = 0; i < 3; i++){
        top_three_elves += tot_calories[i];
    }
    
    std::cout << top_three_elves << std::endl;
}