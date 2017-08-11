#include <iostream>
#include <vector>
#include <string>

void printBoard(std::vector<std::vector<int> > board, int size){
	std::string header = "";
	for(int i = 0; i < size; i++){
		header += "+-";
	}
	header += "+";
	for(int i = 0; i < size; i++){
		std::cout << header << "\n|";
		for(int j = 0; j < size; j++){
			std::cout << board[i][j] << "|";
		}
		std::cout << '\n';
	}
	std::cout << header;
}

int main(int argc, char** argv){
	int size;
	std::cout << "Enter Side Length of Board: ";
	std::cin >> size;
	std::vector<std::vector<int> > board(size, std::vector<int>(size));
	printBoard(board, size);
	return 0;
}
