#include "Appmanifest.h"
#include <cstdlib>

//constructors
Appmanifest::Appmanifest(){
    ID = 0;
}

Appmanifest::Appmanifest(int ID_){
    ID = ID_;
}

// empty destructor
Appmanifest::~Appmanifest(){

}

//getters
int Appmanifest::getID() const {return ID;}

//setters
void Appmanifest::setID(const int ID_) {ID = ID_;}

ostream& operator <<(ostream& out, const Appmanifest& value){
    out << "(" << value.getID() << ")";
    return out;
}