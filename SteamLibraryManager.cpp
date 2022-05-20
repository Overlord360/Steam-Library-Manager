/*
* Steam File Manager
* Author: Simeon Pento
* Last Modified: 20/05/2022
*/

#include <iostream>
#include <string>
#include <fstream>
#include "ManifestList.h"

using namespace std;
int main() {
    string version = "ALPHA - v0.1";
    cout << "Steam Library Manager - " << version << endl;

    fstream file;
    file.open("./appmanifests/appmanifest_60.acf", ios::in);

    if(file.is_open()){
        string line;
         while ( getline (file, line) ){
            cout << line << endl;
        }
    } else {
        cout << "FILE FUCKY WUCKY NOT OPEN" << endl;
        return -1;
    }

    file.close();
    return 0;
}