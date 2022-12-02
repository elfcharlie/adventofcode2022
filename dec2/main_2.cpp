#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <math.h>
#include <vector>

/* A = rock, B = paper, C = scissor
   X = rock, Y = paper, Z = scissor*/

void play_round(int &total_score, std::string opponent, std::string me);

int main(){
    std::ifstream data_file{"input.txt"};
    std::string opponent{""};
    std::string me{""};
    int total_score{0};

    while(data_file >> opponent){
        data_file >> me;
        play_round(total_score, opponent, me);
        
    }
    std::cout << "Total Score: " << total_score << std::endl;
}

void play_round(int &total_score, std::string opponent, std::string me){
    int round_score{0};
    if(opponent == "A"){
            if(me == "X"){
                round_score = 3;
            }
            else if (me == "Y"){
                round_score += 1 + 3;
            }
            else {
                round_score += 2 + 6;
            }
        }
    else if(opponent == "B"){
            if(me == "X"){
                round_score = 1;
            }
            else if (me == "Y"){
                round_score = 2 + 3;
            }
            else {
                round_score = 3 + 6;
            }
        }
    else if(opponent == "C"){
            if(me == "X"){
                round_score = 2;
            }
            else if (me == "Y"){
                round_score = 3 + 3;
            }
            else {
                round_score = 1 + 6;
            }
    }
    total_score += round_score;
}